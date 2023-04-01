import getUserToken

def verify_file_exist(filename):
    try:
        with open(filename) as userInfoFile:
            pass
    except FileNotFoundError:
        print('Current file is not found')
        print('Please update your information...')
        
        user_name, user_bearer_token = getUserToken.get_name_and_token()
        getUserToken.write_data_into_file(user_name, user_bearer_token)
