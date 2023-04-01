import json
import verifyFileExist
import getUserToken

def verify_file_info(filename):
    verifyFileExist.verify_file_exist(filename)
    
    with open(filename) as userInfoFile:
        try:
            user_data = json.load(userInfoFile)
        except json.JSONDecodeError:
            print('There is something wrong with the file')
            print('Please update your information....')
            
            user_name, user_bearer_token = getUserToken.get_name_and_token()
            getUserToken.write_data_into_file(user_name, user_bearer_token)


