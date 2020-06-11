import logging
import  time

from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
#元素导入
from PageElements import login_elenium

class Login_Page(BasePage):

    #登录功能
    def login(self, username, passwd):
        logging.info('登录操作： 用户名{} 密码 {}'.format(username,passwd))
        self.find_element(By.XPATH,login_elenium.user).send_keys(username)
        self.find_element(By.XPATH,login_elenium.password).send_keys(passwd)
        time.sleep(2)
        self.find_element(By.XPATH,login_elenium.button).click()



