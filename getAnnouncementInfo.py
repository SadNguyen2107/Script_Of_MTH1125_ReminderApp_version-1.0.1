import requests
import json
import os
from datetime import datetime
import openWebBrowser
import verifyUserToken
import getUserToken

# Verify User_token first
verifyUserToken.verify_user_token('UserData/UserInfo.json')  # ! For Dev

# Read the User Bearer Token from UserInfo.json file


def get_bearer_token(filename):
    with open(filename, 'r') as userInfoFile:
        user_data = json.load(userInfoFile)
        user_bearer_token = user_data['Bearer Token']
        headers = {
            'Authorization': 'Bearer {user_bearer_token}'.format(user_bearer_token=user_bearer_token),
        }
        return headers



# If the wifi connection isn't connect
# Then load the previous data
try:
    #! Emergency
    while True:
        # URL and Beaer Token
        url = 'https://troy.instructure.com/api/v1/announcements?context_codes[]=course_87909'
        headers = get_bearer_token('UserData/UserInfo.json')
        
        # Send a GET request
        response = requests.get(url, headers=headers)
        
        if response.status_code == 401:
            print('Invalid Token')
            
            user_name, user_bearer_token = getUserToken.get_name_and_token()
            getUserToken.write_data_into_file(user_name, user_bearer_token)
            
        elif response.status_code == 404:
            print('Resource Not Found')
            
            user_name, user_bearer_token = getUserToken.get_name_and_token()
            getUserToken.write_data_into_file(user_name, user_bearer_token)
            
        elif response.status_code == 200:
            break
    #! Emergency
    
except requests.exceptions.ConnectionError as error_message:  # If the wifi connection is unstable
    print('Wifi Error!')
    openWebBrowser.openWebBrowser()

else:
    data = response.json()
    if data == []:
        openWebBrowser.openWebBrowser()

        # * Will get rid of this in the future
        print('Cannot retrieve the data currently')
    else:

        for index in range(0, 11):
            message_data = data[index].get('message', 'Wait A Minute !!!')
            print(f'Trial {index}: {message_data}')
            if message_data is not None:
                break

        # Write data into Json file
        def fetch_announcement_data_json(json_filename):
            with open(json_filename, 'w') as announcement_file:
                json.dump({'message': message_data}, announcement_file)
                print(f'Successfully dump data in the file {json_filename}')

        # Write data into HTML file
        def fetch_announcement_data_html(html_filename):
            current_time = datetime.now()
            date_string = datetime.strftime(current_time, "%B %d, %Y: %H:%M:%S")
            
            with open(html_filename, 'w') as announcement_file:
                announcement_file.write(f'Last Update: {date_string}')
                announcement_file.write(message_data)
                print(f'Successfully dump data in the file {html_filename}')

        def write_data_into_file():
            # Make a directory named OutputData with all the file in there
            try:
                # Directory to put all the file in there
                directory = 'OutputData'

                # Parent Directory path
                parent_dir = os.getcwd()
                
                # Path to the Folder
                path = os.path.join(parent_dir, directory)
                
                # Create a directory
                os.mkdir(path)
            except OSError as error_message:
                # Dump data into HTML file
                fetch_announcement_data_html('OutputData/announcementInfo.html')

                # Dump data into JSON file
                fetch_announcement_data_json('OutputData/homeworks.json')         
                fetch_announcement_data_json('OutputData/UserInfo.json')                 
            else:
                # Dump data into HTML file
                fetch_announcement_data_html('OutputData/announcementInfo.html')

                # Dump data into JSON file
                fetch_announcement_data_json('OutputData/homeworks.json')         
                fetch_announcement_data_json('OutputData/UserInfo.json')       

        write_data_into_file()
        # Open announcementInfo.html
        openWebBrowser.openWebBrowser()
