import time
from okta import UsersClient

from okta.models.user import User


# Tenant data.
'''
Setting up your enviroment where the script will run

Tenant: app your sudomain data to the {{url}}
::API_Token:: - Replace it with the token you create by following this link: https://developer.okta.com/docs/api/getting_started/getting_a_token
'''
usersClient = UsersClient("https://{{url}}.okta.com", "API_Token")


'''
Values that define the functionality of the script

Arguments:
        :user_index: => The index from where the script will start counting. Default value of 1
        :firstName_value: => Shared value between all users created. Default value of User
        :lastName_value: => Dinamyc value that will make sure that each user is unique as per Okta's request
        :email_domain: => The domain value for the email and login form. Default value of @example.com
'''
user_index = 1
firstName_value = "User"
lastName_value = 1
email_domain = "@example.com"


# While loop to create 1000 users. As the user_index has a default value of 1 we will need to run until 1001 in order to have 1000 users created. If instead we use 1000, then 999 user will be created.
# time.sleep is defined at 5 seconds in order to make sure that the rate limit is not reached.
# Okta Rate limit documentation: https://developer.okta.com/docs/api/getting_started/rate-limits

while user_index < 1001:

    user = User(login=firstName_value + str(lastName_value) + email_domain,

            email= firstName_value + str(lastName_value) + email_domain,

            firstName= firstName_value,

            lastName=lastName_value)
    

    user = usersClient.create_user(user, activate=True)
    user_index += 1
    lastName_value += 1
    time.sleep(5)
