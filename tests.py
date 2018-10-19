import re
import requests
import pytest


def get_proxies():
    url = 'http://www.proxy-pool.com/proxies/'
    r = requests.get(url, timeout=3)
    return r.json()


def check_proxy(ip):
    url = 'http://1212.ip138.com/ic.asp'
    pat = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    proxies = {'http': '{}:18118'.format(ip)}
    try:
        r = requests.get(url, proxies=proxies, timeout=3)
        ret_ip = re.search(pat, r.content).group()
    except:
        ret_ip = ''
    return ip == ret_ip


def check_all_roxies():
    proxies = get_proxies()
    for server, ip in proxies.iteritems():
        flag = check_proxy(ip)
        if flag:
            print '----{server}:{ip}-----ok!'.format(ip=ip, server=server)
        else:
            print '----{server}:{ip}-----error!'.format(ip=ip, server=server)


@pytest.mark.parametrize('ip, expected', [
    ('127.0.0.1', False),
])
def test_check_proxy(ip, expected):
    real = check_proxy(ip)
    assert expected == real


if __name__ == '__main__':
    print check_proxy('127.0.0.1')
    # check_all_roxies()
