from sep_swagger_client.configuration import Configuration


# There is a corresponding change in sep_swagger_client/api_client.py.
# The function update_params_for_auth method contains the additional line:
#         auth_settings = ['basic']
# corresponding to the key added to the auth settings dictionary here.

class SepAuthConfiguration(Configuration):
    def auth_settings(self):
        return {
            'basic': {
                # get_basic_auth_token() is populated by setting username and password on the configuration object
                'value': self.get_basic_auth_token(),
                'in': 'header',
                'key': 'Authorization'
            }
        }
