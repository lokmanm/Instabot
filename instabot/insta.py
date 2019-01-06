from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(5)
        login_button = driver.find_element_by_xpath(
            "//a[@href='/accounts/login/?source=auth_switcher']")
        print("Going to login.")
        login_button.click()
        time.sleep(10)
        user_name_elem = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_name_elem.clear()
        print("Typing username.")
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_elem.clear()
        print("Typing password.")
        password_elem.send_keys(self.password)
        time.sleep(3)
        password_elem.send_keys(Keys.RETURN)
        print("Loging in.")
        time.sleep(3)
        activated_elem = driver.find_element_by_link_text("Not Now")
        activated_elem.click()
        print("Removing Not Now.")
        time.sleep(3)
        notnow_elem = driver.find_element_by_xpath(
            "//button[text()='Not Now']")
        notnow_elem.click()
        print("Removing Notifications.")
        time.sleep(5)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get(
            "https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)

        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href)
                 for href in hrefs_in_view if href not in pic_hrefs]
                print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

            # Liking photos
            unique_photos = len(pic_hrefs)
            for pic_href in pic_hrefs:
                driver.get(pic_href)
                time.sleep(2)
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                try:
                    time.sleep(random.randint(2, 4))

                    def like_button(): return driver.find_element_by_xpath(
                        '//span[@aria-label="Like"]').click()
                    like_button().click()
                    for second in reversed(range(0, random.randint(18, 28))):
                        print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                        + " | Sleeping " + str(second))
                        time.sleep(1)
                except Exception as e:
                    time.sleep(2)
                unique_photos -= 1
