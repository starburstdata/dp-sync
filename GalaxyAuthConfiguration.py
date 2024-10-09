from galaxy_swagger_client.configuration import Configuration


class GalaxyAuthConfiguration(Configuration):
    def auth_settings(self):
        return {
            "accessToken": {
                "key": "Authorization",
                "in": "header",
                "value": f'bearer {self.api_key["accessToken"]}'}}
