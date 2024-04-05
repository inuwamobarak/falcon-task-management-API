from app import api
import os
from gunicorn.app.base import BaseApplication

class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

options = {
    'bind': '127.0.0.1:8001',
    'workers': 2,
    'timeout': 120,
    'capture_output': True,
}

StandaloneApplication(api, options).run()



# from app import api

# if __name__ == '__main__':
#     import os
#     from gunicorn.app.base import BaseApplication

#     class StandaloneApplication(BaseApplication):
#         def __init__(self, app, options=None):
#             self.options = options or {}
#             self.application = app
#             super().__init__()

#         def load_config(self):
#             config = {key: value for key, value in self.options.items()
#                       if key in self.cfg.settings and value is not None}
#             for key, value in config.items():
#                 self.cfg.set(key.lower(), value)

#         def load(self):
#             return self.application

#     options = {
#         'bind': '127.0.0.1:8000',
#         'workers': 2,
#         'timeout': 120,
#         'capture_output': True,
#     }

#     StandaloneApplication(api, options).run()