import pandas as pd
from selenium import webdriver
import csv
import re
import time

df=pd.read_csv('./discount_meds/discount_meds/clincalc.csv')
drugs = list(df.name)
drugs = [drug.lower() for drug in drugs][0:100]
# List of URLs of interest
URL_list_goodrx=['https://www.goodrx.com/'+drug for drug in drugs]

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options);  

with open("GDiscountrx_Selenium_py.csv" , 'w', encoding = 'utf-8', newline = '') as csv_file:
    writer = csv.writer(csv_file)    
    # Will Run Selenium for each URL page 
    for URL in URL_list_goodrx:
        driver.get(URL)
        time.sleep(5)
        
        pages_dict={}
        # Create xpath variable for individual drug page
        try :
            pages_dict['med_name'] = driver.find_element_by_xpath('//h1[@id="uat-drug-title"]/a').text
            pages_dict['med_type'] = driver.find_element_by_xpath('//div[@class="label-1Z3f2 label_with_props_padding-3S2kf"]').text
            pages_dict['med_form'] = driver.find_element_by_xpath('//span[@class="labelText-34ve5 labelText_form-2cBDc labelText-34ve5"]').text
            pages_dict['med_dosage'] = driver.find_element_by_xpath('.//span[@class="labelText-34ve5 labelText_dosage-3Fpsw"]').text
            pages_dict['num_of_tablets'] = driver.find_element_by_xpath('//span[@class="labelText-34ve5"]').text
            pages_dict['price_table_drugstores'] = [l.text for l in driver.find_elements_by_xpath('//span[@class="goldAddUnderline-1CwEN"]')]
            pages_dict['price_table_savings']  = [l.text for l in driver.find_elements_by_xpath('//span[@class="savingsPercentage-3xoFU"]')]
            pages_dict['price_value'] = [l.text for l in driver.find_elements_by_xpath('//div[@class="display-2zakM"]')]
            writer.writerow(pages_dict.values())  
        except:
            print("missing data for"+URL)
                        
# Close csv and driver
csv_file.close()
driver.close() 