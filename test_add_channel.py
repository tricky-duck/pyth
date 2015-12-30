# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_channel(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_add_channel(self):
        success = True
        wd = self.wd
        wd.get("http://seleniumbuilder.github.io/se-builder/")
        wd.get("http://192.168.139.147/accounts/login/?next=/main/")
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("1")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("1")
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        wd.find_element_by_css_selector("#main > table > tbody > tr > td").click()
        wd.find_element_by_link_text("Каналы").click()
        wd.find_element_by_link_text("Добавление канала").click()
        wd.find_element_by_id("id_name").click()
        wd.find_element_by_id("id_name").clear()
        wd.find_element_by_id("id_name").send_keys("qwerty")
        wd.find_element_by_id("id_programm").click()
        wd.find_element_by_id("id_programm").clear()
        wd.find_element_by_id("id_programm").send_keys("777")
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        wd.find_element_by_name("programm").click()
        wd.find_element_by_name("programm").clear()
        wd.find_element_by_name("programm").send_keys("777")
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
