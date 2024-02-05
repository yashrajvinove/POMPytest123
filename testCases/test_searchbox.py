from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utilities import XLUtils
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_002_Search:
    baseURL = ReadConfig.getApplicationURL()
    userid = ReadConfig.getUseremail()
    userpass = ReadConfig.getPassword()
    path = ".//TestData/SearchBoxData.xlsx"

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

        self.rows =XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows i a Excel:",self.rows)

        for r in range(2,self.rows+1):
            self.product = XLUtils.readData(self.path,'Sheet1',r,1)

            self.lp.clickSearchBox(self.product)

            self.lp.clickSearchicon()
            self.lp.clickAddtoCart()
            time.sleep(2)





