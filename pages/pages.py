from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import login_page_locators
from base import drivers
from utility_functions import data_cleaner, csv_handler, date_formattor
locators = login_page_locators.login_page_locators()
class pages(drivers.configure_dirvers):
    def __init__(self):
        super().__init__()


    # -----------------------------This Function Extracts all the Links associsted with top apps
    def extract_all_hrefs(self):
        self.chrome_driver.get(locators.main_link)  # load the page
        X = self.chrome_driver.find_element(By.XPATH, locators.get_data_xpath)  # get data by xpath
        child_elements = X.find_elements_by_xpath('.//*')  # get children of Xpath
        dataa = data_cleaner.data_cleaner(child_elements).clean()  # send data for cleaning
        print(dataa)
        return dataa


    # -----------------------------This function collects data form individual apps
    def get_data(self):
        wait = WebDriverWait(self.chrome_driver, 20)
        link_of_all_apps = self.extract_all_hrefs()
        print('Lets Collect All The Data')
        list_of_data = csv_handler.csv_handler().table
        for i in link_of_all_apps:
            self.chrome_driver.get(i)  # launch websites

            # ----------Get name, review numbers, date
            name = wait.until(EC.presence_of_element_located((By.CLASS_NAME, locators.app_name))).text
            review_number = int(self.chrome_driver.find_element_by_class_name(locators.reviews).text.replace(',', ''))
            text_date, days = date_formattor.date_formattor(self.chrome_driver)

            # ----------Calculate and store it in list
            score = review_number / days
            list_of_data.append([name, review_number, text_date, days, round(score, 3)])

        # -----------Helper to write to CSV file
        csv_handler.csv_handler().csv_writer(list_of_data)



