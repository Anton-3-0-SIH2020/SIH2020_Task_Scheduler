import os
BASE_URL = None
if os.environ.get('BASE_URL', None):
    BASE_URL = os.environ.get('BASE_URL', '')
else:
    BASE_URL = 'http://127.0.0.1:8000/'
