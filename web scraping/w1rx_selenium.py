import pandas as pd
from selenium import webdriver
import csv 
import re
import time

df=pd.read_csv('./discount_meds/discount_meds/clincalc.csv')
drugs = list(df.name)
drugs = [drug.lower() for drug in drugs]
URL_list_w1rx=['https://www.wellrx.com/prescriptions/'+drug+"/15217?freshSearch=true" for drug in drugs]
len(URL_list_w1rx)

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options); 

with open("W1Discountrx_Selenium_py.csv" , 'w', encoding = 'utf-8', newline = '') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['drug description', 'drugstores', 'price']) 
    for URL in URL_list_w1rx:
        driver.get(URL)
        time.sleep(5)
        pages_dict={}
        try:
            pages_dict['drug description'] = driver.find_element_by_xpath('//li[@class="qty"]').text
            pages_dict['drugstores'] = [l.text for l in driver.find_elements_by_xpath('.//p[@id="multipharm-loc-key"]/a')]
            pages_dict['price_drugstores'] = [l.text for l in driver.find_elements_by_xpath('.//span[@class="price price-large"]')]
            writer.writerow(pages_dict.values())
        except:
            print("could not find data for"+URL)
                
csv_file.close()
driver.close()