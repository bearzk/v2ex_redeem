#!/usr/bin/python

import re
from sys import exit

import requests

from config import *
if LOGIN_NAME == '' or LOGIN_PASS == '':
    print('Please set LOGIN_NAME and LOGIN_PASS in config.py.')
    exit(1)


class V2ex(object):

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(BROWSER_HEADER)

        self.auth_dict = {}
        self.redeem_code = ''


    def __prepare_login_data(self):
        r = self.session.get(LOGIN_URL)

        user_name = re.search(USER_PATTERN, r.text).groups()[0]
        pass_name = re.search(PASS_PATTERN, r.text).groups()[0]
        once_value = re.search(ONCE_PATTERN, r.text).groups()[0]

        self.auth_dict = {
            user_name: LOGIN_NAME,
            pass_name: LOGIN_PASS,
            'once': once_value
        }


    def __prepare_redeem_param(self):
        r = self.session.get(DAILY_URL)
        try:
            self.redeem_code = re.search(REDEEM_PATTERN, r.text).groups()[0]
        except:
            print('already redeemed for today.')
            exit(1)


    def login(self):
        self.__prepare_login_data()
        r = self.session.post(LOGIN_URL, self.auth_dict)


    def redeem(self):
        self.__prepare_redeem_param()
        r = self.session.get(REDEEM_URL + self.redeem_code)
        print('redeem works.')


if __name__ == '__main__':
    v2ex = V2ex()
    v2ex.login()
    v2ex.redeem()
