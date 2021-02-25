from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

SPACE_LIST_URL = 'https://wapl.ai/spaces'

class WAPL:
    def __init__(self, chrome_path, window_size=(1280, 1024)):
        self.browser = webdriver.Chrome(chrome_path)
        self.browser.set_window_size(window_size[0], window_size[1])
    def login(self, id, pw):
        self.browser.get(SPACE_LIST_URL)
        id_tag = self.browser.find_element_by_id("username")
        id_tag.send_keys(id)

        pw_tag = self.browser.find_element_by_id("password")
        pw_tag.send_keys(pw)

        self.browser.find_element_by_id("kc-login").click()
    def enter_space_by_name(self, name):
        spaces = self.browser.find_elements_by_class_name('space-title')
        for space in spaces:
            if space.text == name:
                space.click()
                return
    def click_nth_navbar(self, index):
        nav_list = self.browser.find_element_by_class_name('ant-tabs-nav-list')
        nav_list.find_elements_by_class_name('ant-tabs-tab')[index].click()
    def goto_friends_list(self):
        self.click_nth_navbar(0)
    def goto_rooms_list(self):
        self.click_nth_navbar(1)
    def goto_mail_list(self):
        self.click_nth_navbar(2)
    def goto_nth_room(self, index):
        left_panel = self.browser.find_element_by_id('rc-tabs-0-panel-s')
        left_panel.find_elements_by_class_name('ant-list-item-meta-title')[index].click()
    def send_talk_msg(self, msg):
        editor = self.browser.find_element_by_class_name('ql-editor')
        self.browser.execute_script("arguments[0].innerText = '"+msg+"'", editor)
        editor.send_keys(Keys.ENTER)
    def quit(self):
        self.browser.quit()
