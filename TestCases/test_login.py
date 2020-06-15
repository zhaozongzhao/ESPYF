import time
import unittest
import logging
import sys

from Common import logger2
from selenium import webdriver
from Common import config
from PageObjects import login_page
from testdata import COMM_DATA as CD
# from testdata import COMM_DATA as CD

class Test_login(unittest.TestCase):

    def setUp(self):
        logging.info("====================登录开始====================")
        options = webdriver.ChromeOptions()
        # options.binary_location = r"C:\Users\user\AppData\Local\Programs\erp-client\派药房.exe"
        options.binary_location = config.package_dir
        self.driver = webdriver.Chrome(chrome_options=options,
                                  executable_path=config.chrome_dir
                                  , port=9515)

        self.loginpage = login_page.Login_Page(self.driver)


    def tearDown(self):
        logging.info("========end test login=========")
        self.driver.close()
        self.driver.quit()

    def test_login_ok(self):
        logging.info("测试用例：正常登录")
        # 登陆
        self.loginpage.login(CD.login_username,CD.login_passwd)
