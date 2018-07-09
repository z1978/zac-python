# -*- coding: utf-8 -*-

import logging
import time

from bs4 import BeautifulSoup
import requests

import os.path
_dir = os.path.dirname(os.path.abspath(__file__))
print(_dir)
conf_dir = os.path.abspath('../../../info.conf')
print(conf_dir)

#访问用户文件,并把所有的用户名和密码用字典类型存储并返回这个列表
def user_all():
    user_dict = {}

    file_object = open(conf_dir)
    try:
        file_all_the_lines = file_object.readlines()

        for line in file_all_the_lines:
            user_dict[line.split(" ")[0]] = line.split(" ")[1].replace("\n", "")

    finally:
        file_object.close()

    return user_dict

def create_session():
    s = requests.Session()
    s.headers.update({
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "ja,en-US;q=0.7,en;q=0.3",
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"
    })
    return s


def yahoojp_session(target_url, users):
    print("11111")
    print(users)



    # headers = {
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    #     "Accept-Language": "ja,en-US;q=0.7,en;q=0.3",
    #     "Connection": "keep-alive",
    #     "User-Agent":
    #         "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"
    # }
    #
    # cap = webdriver.DesiredCapabilities.PHANTOMJS
    # for key, val in headers.items():
    #     cap["phantomjs.page.customHeaders." + key] = val
    # cap["phantomjs.page.settings.userAgent"] = headers["User-Agent"]
    #
    # try:
    #     # <class 'selenium.webdriver.phantomjs.webdriver.WebDriver'>
    #     driver = webdriver.PhantomJS()
    # except Exception as e:
    #     logging.error(e)
    #     return None
    #
    # # クッキーを先に取得する
    # driver.get(target_url)
    # bs4 = BeautifulSoup(driver.page_source, "html5lib")
    # login_url = bs4.find("a", attrs={"id": "msthdLogin"})["href"]
    #
    # driver.get(login_url)
    # time.sleep(1)
    #
    # driver.find_element_by_name("login").send_keys(login_id)
    # driver.find_element_by_name("btnNext").click()  # 次へボタン
    # time.sleep(1)
    #
    # driver.find_element_by_name("passwd").send_keys(password)
    # driver.find_element_by_name("btnSubmit").click()  # ログインボタン
    # time.sleep(1)
    # # driver.save_screenshot(_dir + "/login.png")   # ログイン済みを画像で確認できます
    #
    # # セッション情報をrequestsに移す
    # s = create_session()
    # for c in driver.get_cookies():
    #     s.cookies[c["name"]] = c["value"]
    #
    # driver.close()
    # return s


if __name__ == '__main__':
    #対象のURL
    my_url = 'https://yahoo.co.jp'
    user_list = user_all()
    # s = yahoojp_session("対象のURL", "ヤフーID", "ヤフーパスワード")
    s = yahoojp_session(my_url, user_list)