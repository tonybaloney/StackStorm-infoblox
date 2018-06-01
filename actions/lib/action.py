try:
    from infoblox_client import connector
except ImportError:
    message = ('Missing "infoblox-client", please install it using pip:\n'
               'pip install infoblox-client')
    raise ImportError(message)

from st2common.runners.base_action import Action

__all__ = [
    'InfobloxBaseAction',
]


class InfobloxBaseAction(Action):
    def __init__(self, config):
        super(InfobloxBaseAction, self).__init__(config)
        _hostname = self.config['hostname']
        _username = self.config['username']
        _password = self.config['password']

        opts = {
            'host': _hostname, 
            'username': _username, 
            'password': _password,
            'ssl_verify': False,
            'silent_ssl_warnings': True
        }
        self.connection = connector.Connector(opts)
