import requests

from config import NOTIFIER_WEBHOOK_URL
from .. import NotifierInterface


class NullNotifier(NotifierInterface):

    def notify(self, message):
        pass


class SlackNotifier(NotifierInterface):

    def notify(self, message):
        requests.post(NOTIFIER_WEBHOOK_URL, json={"text": message, "username": "v2ex_redeem"})
