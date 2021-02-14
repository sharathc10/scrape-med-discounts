# scrape-med-discounts
<h1>Web Scraping Project for Drug Discount Coupon websites</h1>
This project analyzes data scraped from 3 websites which offer drug discount coupons.  The names of the sites have been kept anonymous and are referred to by the letters G, W1 and W2.  The steps for analysis were as follows:
<ol>
<li>scrape an anonymous site using scrapy to find the top 200 drugs based on number of prescriptions.  The scrapy code is in the folder <strong>web scraping/discount_meds</strong></li>
<li>the drug names were then used to scrape drug discount price information from each drug discount site using Selenium - in some cases the drug names had to be modified to meet the requirements of the site.  The code for the scrapers are in <strong>grx_selenium.py</strong> and <strong>w1rx_selenium.py</strong> and <strong>w2rx_selenium.py</strong></li>
<li>the scraped data were saved in the following files - GDiscountrx_Selenium.csv, W1Discountrx_Selenium.csv and W2Discountrx_Selenium.csv</li>
<li>Minor modifications were required in W1Discountrx_Selenium and W2Discountrx_Selenium and were renamed to W1Discountrx_Selenium2.csv and W2Discountrx_Selenium2.csv to avoid scrapping again</li>
<li>The files generated in steps 3 and 4 were then fed into cleaners.  The cleaner files are <strong>data manipulation and visualization/GDiscountrxClean</strong>,<strong>W1DiscountrxClean</strong> and <strong>W2DiscountrxClean</strong>.  The output of the cleaning were placed in GDiscountClean.csv, W1Discountrx_Selenium2_Clean.csv and W2Discountrx_Selenium2_Clean.csv</li>
<li>6.  The three csv files generated in step 5 were then fed into notebook <strong>DiscountrxAnalysis</strong> where additional cleaning related to analysis was performed and the plots were generated using seaborn</li>
</ol>