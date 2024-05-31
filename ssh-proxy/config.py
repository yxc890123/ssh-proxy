import os

conf_file = f'{os.path.dirname(__file__)}/ssh-proxy.conf'


class Config(object):
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not self._initialized:
            self.PATH = None
            self.LOGIN_RETRY = 3
            self.LOGIN_TIMEOUT = 60.0
            self.SSH_PORT = 3000
            self.RSA_KEY = 'ssh_host_rsa_key'
            self.SFTP_CMD = '/usr/libexec/openssh/sftp-server'
            self.MAX_SESSIONS = 10

            self._initialized = True

    def load(self, path):
        if path is None:
            if os.access(conf_file, os.R_OK):
                print('[I] Loading config:', conf_file)
                open(conf_file)
        else:
            self.PATH = path
            try:
                print('[I] Loading config:', path)
                open(path)
            except Exception as e:
                print('[W] Failed to open config file:', e)
                print('[W] Start with default settings.')
                return

        # TODO: load config from file
        pass

    def reload(self, *_):
        if self.PATH is None:
            if os.access(conf_file, os.R_OK):
                print('[I] Reloading config:', conf_file)
                open(conf_file)
            else:
                print('[I] No config file specified, nothing happened.')
        else:
            try:
                print('[I] Reloading config:', self.PATH)
                open(self.PATH)
            except Exception as e:
                print('[W] Failed to open config file:', e)
                print('[W] Nothing happened.')
                return

        # TODO: load config from file
        pass
