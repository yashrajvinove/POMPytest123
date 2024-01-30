from selenium import webdriver
from selenium.webdriver.common.by import By


class   LoginPage:
    textbox_usermail_id="input-email"
    textbox_userpassword_id="input-password"
    button_xpath="//input[@value='Login']"

    def  __init__(self,driver):
          self.driver=driver

    def clickPas(self):
        self.driver.find_element("id",self.textbox_usermail_id).click()
    def clickID(self):
        self.driver.find_element("id",self.textbox_userpassword_id).click()
    def  setUserID(self,userid):
          self.driver.find_element("id",self.textbox_usermail_id).clear()
          self.driver.find_element("id",self.textbox_usermail_id).send_keys(userid)

    def  setUserPass (self,userpass):
          self.driver.find_element("id",self.textbox_userpassword_id).clear()
          self.driver.find_element("id",self.textbox_userpassword_id).send_keys(userpass)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_xpath).click()

