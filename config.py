# script
base_url = 'https://www.v2ex.com'
BROWSER_HEADER = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Referer': 'https://www.v2ex.com/'
}

LOGIN_URL = base_url + '/signin'
DAILY_URL = base_url + '/mission/daily'
REDEEM_URL = DAILY_URL + '/redeem?once='

base_pattern = r'class="sl" name="([a-f0-9]+)"'
USER_PATTERN = r'type="text" ' + base_pattern
PASS_PATTERN = r'type="password" ' + base_pattern
ONCE_PATTERN = r'type="hidden" value="(\w+)" name="once"'
REDEEM_PATTERN = r'onclick="location.href = .\/mission\/daily\/redeem\?once=(\w+).;"'


# user
LOGIN_NAME=''
LOGIN_PASS=''
