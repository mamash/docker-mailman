# -*- python -*-

from Defaults import *

MAILMAN_SITE_LIST = 'mailman'
IMAGE_LOGOS = '/mailman/images/mailman/'

DEFAULT_ARCHIVE = Off
DEFAULT_ARCHIVE_PRIVATE = 1
DEFAULT_ARCHIVE_VOLUME_FREQUENCY = 2
DEFAULT_DIGESTABLE = No
DEFAULT_LIST_ADVERTISED = No
DEFAULT_MAX_MESSAGE_SIZE = 0
DEFAULT_MAX_NUM_RECIPIENTS = 50
DEFAULT_MSG_FOOTER = ""
DEFAULT_SEND_GOODBYE_MSG = No
DEFAULT_SEND_REMINDERS = No
DEFAULT_SEND_WELCOME_MSG = No
DEFAULT_SERVER_LANGUAGE = 'cs'
DEFAULT_SUBSCRIBE_POLICY = 2

MTA='Manual'
SMTPHOST= 'postfix-mailcow'
DEFAULT_EMAIL_HOST = '%DEFAULT_EMAIL_HOST%'
DEFAULT_URL_HOST = '%DEFAULT_URL_HOST%'
DEFAULT_URL_PATTERN = 'https://%s/mailman/'
