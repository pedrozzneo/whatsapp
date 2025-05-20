from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os

def set():
    # Create chrome options object
    chrome_options = Options()

    # Set the options for Chrome
    selenium_data_dir = os.path.join(os.path.expanduser('~'), 'selenium-chrome-data') 
    chrome_options.add_argument(f'user-data-dir={selenium_data_dir}')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-gpu')  
    chrome_options.add_argument('--start-maximized')

    return webdriver.Chrome(options=chrome_options)