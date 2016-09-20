import os
import yaml

class Config(object):
    def __init__(self):
        config_file = os.path.join(".", self.__class__.__name__) + ".yaml"
        print config_file
        if os.path.exists(config_file):
            with open(config_file) as f:
                param = yaml.load(f)

                for k, v in param.iteritems():
                    setattr(self, k, v)


class ProdConfig(Config):
    USER_NAME = "user"
    PASSWORD = "123456"

