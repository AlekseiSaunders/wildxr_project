import os
import pytest
import time
from faker import Faker
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium. webdriver.support import expected_conditions as EC
from page_objects.authentication.login_page import LoginPage
from utilities.screenshot_manager import ScreenshotManager
from utilities.utils import logger

class TestResults():
    
    def __init__(self, driver):
        self.results_list = []
        self.driver = driver
        
    def set_result(self, result, success_message, failure_message):
        try:
            if result is not None:
                if result:
                    self.results_list.append("PASS")
                    logger.info(f"Verification Successful :: {success_message}")
                else:
                    self.results_list.append("FAIL")
                    logger.warning(f"Verification Failed :: {failure_message}")
            else:
                self.results_list.append("RESULT WAS NONE - FAIL")
                logger.warning(f"Verification Failed :: result was None {failure_message}")
        except Exception as e:
            self.results_list.append("An Exception Occured - FAIL")
            logger.error(f"Verification Failed :: Exception occurred {failure_message}")
        
    def mark(self, result, success_message, failure_message):
        self.set_result(result, success_message, failure_message)
    
    
    def mark_final(self, test_name, result, success_message, failure_message):
        self.set_result(result, success_message, failure_message)
        if "FAIL" in self.results_list:
            logger.critical(f"Test name: {test_name} failed.")
            self.results_list.clear()
            assert False, f"Test {test_name} failed: {failure_message}" 
        else:
            logger.info(f"Test name: {test_name} has passed.")
            self.results_list.clear()
            assert True
    