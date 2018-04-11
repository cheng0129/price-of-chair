
# URL = "https://api.mailgun.net/v3/sandboxd96a45a568284c1e9c7d2b376278bbe5.mailgun.org/messages"
# API_KEY = "key-cdc5b6adbc885db7184620ecfe51b74e"
# FROM = "Mailgun Sandbox <postmaster@sandboxd96a45a568284c1e9c7d2b376278bbe5.mailgun.org>"
import os

URL = os.environ.get('MAILGUN_URL')
API_KEY = os.environ.get('MAILGUN_API_KEY')
FROM = os.environ.get('MAILGUN_FROM')

ALERT_TIMEOUT = 10
COLLECTION = "alerts"