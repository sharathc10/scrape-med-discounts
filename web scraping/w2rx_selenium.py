import pandas as pd
from selenium import webdriver
import time
import re
import csv 

df=pd.read_csv('./discount_meds/discount_meds/clincalc_with_dash.csv')
drugs = list(df.name)
drugs = [drug.upper() for drug in drugs]
URL_list_w2rx=['https://werx.org/price/'+drug+"/15217" for drug in drugs]
len(URL_list_w2rx)

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options); 
URL=""
with open("W2Discountrx_Selenium_py.csv" , 'w', encoding = 'utf-8', newline = '') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['drugstores', 'price']) 
    for URL in URL_list_w2rx:
        driver.get(URL)
        time.sleep(5)
        pages_dict={}
        try:
            pages_dict['drugstores'] = [l.text for l in driver.find_elements_by_xpath('.//div[@class="PharmacyDetails"]/div')]
            pages_dict['price'] = [l.text for l in driver.find_elements_by_xpath('.//div[@data-bind="text: DisplayCouponPrice"]')]
            pages_dict['drug URL']=URL
            writer.writerow(pages_dict.values())
        except:
            pages_dict['drug URL']=URL
            writer.writerow(pages_dict.values())
                
csv_file.close()
driver.close()
