# -*- coding: utf-8 -*-
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
#import argparse
#import getpass
import re
import random

class InstaBidwe2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_insta_bidwe2(self):
        driver = self.driver
        username = "put_username_here"
        pwd = "put_password_here"
        #Adjectives
        adjectives = ['Amazing', 'Awesome', 'Blithesome', 'Excellent', 'Fabulous', 'Fantastic', 'Favorable', 'Fortuitous',\
             'Gorgeous', 'Incredible', 'Ineffable', 'Mirthful', 'Outstanding', 'Perfect', 'Propitious', 'Remarkable'\
                'Rousing', 'Spectacular', 'Splendid', 'Stellar', 'Stupendous', 'Super', 'Upbeat', 'Unbelievable', \
             'Wondrous']
        driver.get("https://www.instagram.com/")
        #log in
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(pwd)
        #click on profile
        driver.find_element_by_xpath(
            "//div[@id='react-root']/section/main/article/div[2]/div/div/form/div[4]/button/div").click()
        driver.find_element_by_xpath("(//img[@alt=\"" + str(username) + ""'s profile picture\"])[2]").click()
        #click on post
        driver.find_element_by_xpath("//div[@id='react-root']/section/main/div/div/a/span/span").click()
        driver.find_element_by_xpath(
            "//div[@id='react-root']/section/main/div/div[2]/article/div/div/div/div/a/div[2]/ul").click()
        #highlight text
        text = driver.find_element_by_xpath("//li/div/div/div[2]").text
        hash_tags = re.findall("#\w+", text)
        #print(text)
        print("Finding hash tags")
        print(hash_tags)
        print("Proceed to the first 10 tags")
        for i in range(10):
            driver.get("https://www.instagram.com/explore/tags/" + str(hash_tags[i][1:]) +"/")
        #click on hash tag
        #driver.find_element_by_link_text("#food").click()
        #new link for hash tag
            driver.find_element_by_xpath(
            "//div[@id='react-root']/section/main/article/div/div/div/div/div/a/div[2]/ul").click()
            driver.find_element_by_xpath("//textarea").click()
            driver.find_element_by_xpath("//textarea").clear()
            driver.find_element_by_xpath("//textarea").send_keys(random.choice(adjectives))
            driver.find_element_by_xpath("//button[@type='submit']").click()
        #driver.find_element_by_xpath("//img[@alt=\"patrick_test_bidwe's profile picture\"]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
