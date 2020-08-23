from selenium import webdriver


class configure_dirvers:
    def __init__(self):
        self.chrome_driver = webdriver.Chrome("/Users/aayushbhargava/Downloads/chromedriver")

    def config_driver(self):
        self.chrome_driver.implicitly_wait(15)
        return self.chrome_driver

