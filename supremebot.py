from config import keys
from selenium import webdriver
import time 

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print((endTime - startTime)/1000, 's')
        return result
    return wrapper


@timeme
def order(k) :

    
    
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["number"])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"])
    
    #state
    # driver.find_elements_by_xpath('//*[@id="order_billing_state"]/option[52]').click()
    #credit card
    driver.find_element_by_xpath('//*[@id="nnaerb"]').send_keys(k["card_number"])
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k["ccv"])
    #month
    driver.find_elements_by_xpath('//*[@id="credit_card_month"]/option[8]')
    #year
    driver.find_elements_by_xpath('//*[@id="credit_card_year"]/option[4]')

    #terms and conditions
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()

    #confirm payment
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()


if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')

    driver.get(keys['product_url'])
    order(keys)