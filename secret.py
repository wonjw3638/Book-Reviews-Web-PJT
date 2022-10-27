# settings.py 상단에 추가하세요.

import json

from django.core.exceptions import ImproperlyConfigured

with open("mysite/secret.json") as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f"set the {setting}"
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")