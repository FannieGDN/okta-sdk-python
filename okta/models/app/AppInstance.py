from datetime import datetime
from okta.models.app.Accessibility import Accessibility
from okta.models.app.Visibility import Visibility
from okta.models.app.AppCredentials import AppCredentials
from okta.models.app.Settings import Settings
from okta.models.app.AppSettings import AppSettings
from okta.models.app.OAuthClientCredentials import OAuthClientCredentials
from okta.models.app.OAuthClientSettings import OAuthClientSettings
from okta.models.Link import Link


class AppInstance:

    types = {
        'id': str,
        'name': str,
        'label': str,
        'created': datetime,
        'lastUpdated': datetime,
        'status': str,
        'activated': datetime,
        'features': list,
        'signOnMode': str,
        'accessibility': Accessibility,
        'visibility': Visibility,
        'credentials': AppCredentials,
        'settings': Settings
    }

    dict_types = {
        '_links': Link
    }

    alt_names = {
        '_links': 'links'
    }

    def __init__(self):

        # unique key for app
        self.id = None  # str

        # unique key for app definition
        self.name = None  # str

        # unique user-defined display name for app
        self.label = None  # str

        # timestamp when app was created
        self.created = None  # datetime

        # timestamp when app was last updated
        self.lastUpdated = None  # datetime

        # status of app
        self.status = None  # enum

        # timestamp when transition to ACTIVE status completed
        self.activated = None  # datetime

        # enabled app features
        self.features = None  # enum

        # authentication mode of app
        self.signOnMode = None  # enum

        self.accessibility = None  # Accessibility

        self.visibility = None  # Visibility

        self.credentials = None  # AppCredentials

        self.settings = None  # Settings

    @staticmethod
    def build_bookmark(url, label=None, request_integration=False):
        app = AppInstance()
        app.name = "bookmark"
        app.label = label
        app.signOnMode = "BOOKMARK"
        app.settings = Settings()
        app.settings.app = AppSettings()
        app.settings.app.url = url
        app.settings.app.requestIntegration = request_integration
        return app

    @staticmethod
    def build_basic_auth(url, label, auth_url):
        app = AppInstance()
        app.name = 'template_basic_auth'
        app.label = label
        app.signOnMode = 'BASIC_AUTH'
        app.settings = Settings()
        app.settings.app = AppSettings()
        app.settings.app.url = url
        app.settings.app.authURL = auth_url
        return app

    @staticmethod
    def build_openid_connect(label, logo_uri=None, redirect_uris=None, response_types=None,
                             grant_types=None, application_type=None, token_endpoint_auth_method=None):
        if response_types is None:
            response_types = ['code']
        if grant_types is None:
            grant_types = ['authorization_code']
        if application_type is None:
            application_type = 'web'
        if token_endpoint_auth_method is None:
            token_endpoint_auth_method = 'client_secret_basic'
        app = AppInstance()
        app.name = 'oidc_client'
        app.label = label
        app.signOnMode = 'OPENID_CONNECT'
        app.credentials = AppCredentials()
        app.credentials.oauthClient = OAuthClientCredentials()
        app.credentials.oauthClient.token_endpoint_auth_method = token_endpoint_auth_method
        app.settings = Settings()
        app.settings.oauthClient = OAuthClientSettings()
        app.settings.oauthClient.logo_uri = logo_uri
        app.settings.oauthClient.redirect_uris = redirect_uris
        app.settings.oauthClient.response_types = response_types
        app.settings.oauthClient.grant_types = grant_types
        app.settings.oauthClient.application_type = application_type
        return app
