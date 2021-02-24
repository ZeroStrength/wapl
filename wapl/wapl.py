from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
    def goto_friends_list(self):
        pass
    def goto_rooms_list(self):
        pass
    def send_talk_msg_to_nth_room(self, msg, index):
        pass
    def quit(self):
        self.browser.quit()

