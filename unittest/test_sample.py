import unittest

import os
import time
from chrome_webdriver import ChromeDriver_AWSLambda
from chrome_webdriver import ChromeDriver_CircleCI
from chrome_webdriver import ChromeDriver_Local


class TestWepAccess(unittest.TestCase):

    def setUp(self):

        platform = os.getenv('PLATFORM')

        if platform == 'AWSLambda':
            self.webdriver = ChromeDriver_AWSLambda().create_driver()
        elif platform == 'CircleCI':
            self.webdriver = ChromeDriver_CircleCI().create_driver()
        else:
            self.webdriver = ChromeDriver_Local(True).create_driver()


    def test_access_amazon(self):
        self.webdriver.get('https://www.amzon.com')
        actual = self.webdriver.title
        time.sleep(1)

        expected = 'Amazon.com. Spend less. Smile more.'
        self.assertEqual(expected, actual)


    def test_access_google(self):
        self.webdriver.get('https://www.google.com')
        actual = self.webdriver.title
        time.sleep(1)

        expected = 'Google'
        self.assertEqual(expected, actual)
