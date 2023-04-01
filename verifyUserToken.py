import verifyFileInfo
import getUserToken
import json


def verify_user_token(filename):
    verifyFileInfo.verify_file_info(filename)
    
    with open(filename) as userInfoFile:
        user_data = json.load(userInfoFile)
        try:
            user_bearer_token = user_data['Bearer Token']
        except KeyError:
            print("There is some problem with the file")
            print('Please update your information...')
            
            user_name, user_bearer_token = getUserToken.get_name_and_token()
            getUserToken.write_data_into_file(user_name, user_bearer_token)
            
