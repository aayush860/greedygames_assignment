import datetime
from locators import login_page_locators
locators = login_page_locators.login_page_locators()

def date_formattor(chrome_driver):
    try:
        if len(chrome_driver.find_element_by_class_name(locators.date_class).text.split(',')) == 2:
            text_date = chrome_driver.find_element_by_class_name(locators.date_class).text
            days = (datetime.datetime.utcnow() - datetime.datetime.strptime(text_date, "%B %d, %Y")).days
        else:
            text_date = chrome_driver.find_element_by_css_selector(locators.date).text
            days = (datetime.datetime.utcnow() - datetime.datetime.strptime(text_date, "%B %d, %Y")).days
    except:
        date = chrome_driver.find_element_by_css_selector(locators.date).text

    return [text_date, days]