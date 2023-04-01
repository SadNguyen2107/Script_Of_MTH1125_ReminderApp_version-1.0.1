import json
import os


def get_name_and_token():
    # Prompt to get the user Name
    user_name = input('Name: ')

    # Prompt to get the user Token
    user_bearer_token = input('Bearer Token: ').strip(' ').strip('\n')
    return user_name, user_bearer_token

# If this file run it will get the user_info
if __name__ == '__main__':
    user_name, user_bearer_token = get_name_and_token()

def write_data_into_txtFile(filename, user_name, user_bearer_token):
    with open(filename, 'w') as userInfoFile:
        userInfoFile.writelines(f'Username: {user_name}\n')
        userInfoFile.writelines(f'User Bearer Token: {user_bearer_token}')
        
def dump_data_into_jsonFile(filename, user_name, user_bearer_token):
    user_info = {
        'Name': user_name,
        'Bearer Token': user_bearer_token,
    }
    
    with open(filename, 'w') as userInfoFile:
        json.dump(user_info, userInfoFile)

def write_data_into_file(user_name, user_bearer_token):
    # Make a directory named UserData with all the file in there
    try:
        # Directory to put all the file in there
        directory = 'UserData'

        # Parent Directory path
        parent_dir = os.getcwd()
        
        # Path to the Folder
        path = os.path.join(parent_dir, directory)
        
        # Create a directory
        os.mkdir(path)
    except OSError as error_message:
        # For internal purpose
        dump_data_into_jsonFile('UserData/UserInfo.json',user_name, user_bearer_token) 
        
        write_data_into_txtFile('UserData/UserInfo.txt', user_name, user_bearer_token)    
        

        # Final Result
        print('Successfully load the data!')
    else:
        # For internal purpose
        dump_data_into_jsonFile('UserData/UserInfo.json', user_name, user_bearer_token) 
        
        write_data_into_txtFile('UserData/UserInfo.txt', user_name, user_bearer_token)    
        

        # Final Result
        print('Successfully load the data!')        

if __name__ == '__main__':
    write_data_into_file()