import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    userid = ReadConfig.getUseremail()
    userpass = ReadConfig.getPassword()


    def test_homePageTitle(self, settup):


        self.driver = settup
        self.driver.implicitly_wait(3)
        self.driver.get(self.baseURL)
        time.sleep(3)
        act_title = self.driver.title
        self.driver.close()
  #      if act_title == "Returning Customer":
   #         assert True
#
    #    else:
    #        assert False

    def test_login(self, settup):


        self.driver = settup
      #  self.driver.implicitly_wait(3)
        self.driver.get(self.baseURL)
        self.lp =LoginPage(self.driver)

        self.lp.clickID()

        self.lp.setUserID(self.userid)
        self.lp.clickPas()
        self.lp.setUserPass(self.userpass)

        self.lp.clickLogin()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div/a[text()='My Account']"))
        )
        time.sleep(5)