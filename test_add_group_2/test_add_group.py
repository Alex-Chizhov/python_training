# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from group import Group
import  unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)


    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def group_creator(self, wd, group):
        # open_gp
        wd.find_element_by_link_text("groups").click()
        # init_group_creator
        wd.find_element_by_name("new").click()
        # fill_group_form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # sumbit_creation_group
        wd.find_element_by_name("submit").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_hp(self, wd):
        wd.get("http://localhost/addressbook/")



    def test_add_group(self):
        wd = self.wd
        self.open_hp(wd)
        self.login(wd, username="admin", password="secret")
        self.group_creator(wd, Group(name="123", header="123", footer="123"))
        self.return_to_group_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_hp(wd)
        self.login(wd, username="admin", password="secret")
        self.group_creator(wd, Group(name="", header="", footer=""))
        self.return_to_group_page(wd)
        self.logout(wd)







    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
