from goodrx.items import GoodRxItem
from scrapy import Spider, Request
import re
import pandas as pd

class ClinCalcSpider(Spider):

        name="clincalc_spider"
        allowed_urls=["https://clincalc.com"]
        start_urls=["https://clincalc.com/DrugStats/Top200Drugs.aspx"]

        def parse(self,response):
            drug_names=response.xpath('.//table[@id="tableTopDrugs"]//td/a/text()').extract()
            drug_rank= response.xpath('.//table[@id="tableTopDrugs"]//td[2]/text()').extract()
            drug_prescriptions=response.xpath('.//table[@id="tableTopDrugs"]//td[3]/text()').extract()
            drug_data={
                'name': drug_names,
                'prescriptions': drug_prescriptions

            }
            pd.DataFrame(drug_data).to_csv("clincalc.csv")
