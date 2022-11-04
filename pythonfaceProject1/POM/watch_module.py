
import re
import time

from library.excel_lib import ReadExcel
from library.config import Config


class WatchModule:

    read_xl = ReadExcel()
    watch_locators = read_xl.read_locators(Config.WATCH_LOCATOR_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def user_name(self, username):
        if isinstance(username, float):
            username = int(username)
        locator = self.watch_locators["enter_username"]
        self.driver.find_element(*locator).send_keys(username)
        time.sleep(3)

    def pass_word(self, pwd):
        locator = self.watch_locators["enter_password"]
        self.driver.find_element(*locator).send_keys(pwd)
        time.sleep(3)

    def log_in(self):
        locator = self.watch_locators["login_1"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def watch_1(self):
        locator = self.watch_locators["watch"]
        self.driver.find_element(*locator).click()
        time.sleep(5)

    def setting_1(self):
        locator = self.watch_locators["setting"]
        self.driver.find_element(*locator).click()
        time.sleep(5)

    def not1_start(self):
        locator = self.watch_locators["not_start"]
        self.driver.find_element(*locator).click()
        time.sleep(5)

    def cus_not2(self):
        locator = self.watch_locators["custom _not"]
        self.driver.find_element(*locator).click()
        time.sleep(5)

    def allow_not3(self):
        locator = self.watch_locators["allow_video_not"]
        self.driver.find_element(*locator).click()
        time.sleep(5)

    def new1_not4(self):
        locator = self.watch_locators["new_video_not"]
        self.driver.find_element(*locator).click()
        time.sleep(8)

    def man_pag(self):
        locator = self.watch_locators["manage_page"]
        self.driver.find_element(*locator).click()
        time.sleep(5)

    def cro_butt(self):
        locator = self.watch_locators["cross_button"]
        self.driver.find_element(*locator).click()
        time.sleep(5)

    def liv_btn(self):
        locator = self.watch_locators["live_icon"]
        self.driver.find_element(*locator).click()
        time.sleep(5)

    def show_btn(self):
        locator = self.watch_locators["show_icon"]
        self.driver.find_element(*locator).click()
        time.sleep(5)







