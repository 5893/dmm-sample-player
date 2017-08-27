# -*- coding: utf-8 -*-
import socket

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException

import time

def check_finished_play(browser):
    try:
        browser.find_element_by_id("sample-after")    # サンプル再生後の広告の取得を試みる
        return True     # 広告を取得できているので再生完了
    except NoSuchElementException:
        return False    # 再生が完了していない


def close_sample_box(brower):
    while True:
        try:
            # サンプルビデオの表示領域を閉じる
            code = """$("#fn-close").click();"""
            browser.execute_script(code)
            break
        except WebDriverException:
            pass    # 読み込みの都合でうまくいかない場合があるので、繰り返し
    return True


# url = "http://www.dmm.co.jp/digital/videoa/-/list/=/article=actress/id=1038706/"  # 水卜さくら
url = "http://www.dmm.co.jp/digital/videoa/-/list/=/article=actress/id=26225/"  # 波多野結衣
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get(url)

ul = browser.find_element_by_id("list")                     # 作品のリストを内包するul取得
sample_links = ul.find_elements_by_class_name("sample")     # サンプルビデオへのリンクを取得
for sample_link in sample_links:
    sample_link.click()
    while True:
        if check_finished_play(browser):
            if close_sample_box(browser):
                time.sleep(0.5)
                break
