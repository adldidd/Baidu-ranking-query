import io, sys, time, re, os
import winreg
import requests

# 表项路径
xpath = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"


def get_proxy():
    proxy = requests.get(
        'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=6&sb=0&pb=4&mr=1&regions=').text
    return proxy


# 设定代理,enable:是否开启,proxyIp:代理服务器ip及端口,IgnoreIp:忽略代理的ip或网址

def setProxy(enable, proxyIp, IgnoreIp):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, xpath, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, enable)
        winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, proxyIp)
        winreg.SetValueEx(key, "ProxyOverride", 0, winreg.REG_SZ, IgnoreIp)
    except Exception as e:
        print("ERROR: " + str(e.args))
    finally:
        None


# 开启，定义代理服务器ip及端口，忽略ip内容(分号分割)
def enableProxy():
    proxyIP = get_proxy()
    IgnoreIp = "172.16.62.15"
    print(" Setting proxy")
    setProxy(1, proxyIP, IgnoreIp)
    print("代理成功，当前ip：%s" % proxyIP)


# 关闭清空代理
def disableProxy():
    setProxy(0, "", "")
    print("清空代理")


def main():
    disableProxy()
    # enableProxy()


if __name__ == '__main__':
    main()
