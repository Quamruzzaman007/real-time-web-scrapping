import time
from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
url = "https://web.sensibull.com/option-chain?expiry=2022-03-17&tradingsymbol=NIFTY"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)


def scrape_data():
    oi_change = driver.find_elements(by=By.XPATH, value="//div[@id='tableContainer']/div/div/div[3]/div/div/div[@class='rt-td'][1]") if True else " "
    oi_lakh = driver.find_elements(by=By.XPATH,value="//div[@id='tableContainer']/div/div/div[3]/div/div/div[@class='rt-td'][2]/div/div/div[@class='style__OiprogressBarValue-sc-qybflf-2 klMzFf']") if True else " "
    ltp_change = driver.find_elements(by=By.XPATH,value="//div[@id='tableContainer']/div/div/div[3]/div/div/div[@class='rt-td'][3]/div/div/div") if True else " "
    strike = driver.find_elements(by=By.XPATH,value="//div[@id='tableContainer']/div/div/div[3]/div/div/div[@class='rt-td'][4]/span") if True else " "
    iv = driver.find_elements(by=By.XPATH,value="//div[@id='tableContainer']/div/div/div[3]/div/div/div[@class='rt-td'][5]") if True else " "
    ltp_change_2 = driver.find_elements(by=By.XPATH,value="//div[@id='tableContainer']/div/div/div[3]/div/div/div[@class='rt-td'][6]/div/div/div") if True else " "
    oi_lakh_2 = driver.find_elements(by=By.XPATH,value="//div[@id='tableContainer']/div/div/div[3]/div/div/div[@class='rt-td'][7]/div/div/div[@class='style__OiprogressBarValue-sc-qybflf-2 fdVZcI']") if True else " "
    oi_change_2 = driver.find_elements(by=By.XPATH,value="//div[@id='tableContainer']/div/div/div[3]/div/div/div[@class='rt-td'][8]") if True else " "
    
    result = []
    for i in range(len(oi_change)):
        temporary_data = {'OI_Change':oi_change[i].text,
                            'OI_Lakh':oi_lakh[i].text,
                            'LTP(Chg%)':ltp_change[i].text.replace("\n", ""),
                            'Strikr':strike[i].text,
                            'IV':iv[i].text,
                            'LTP(Chg%)_2':ltp_change_2[i].text.replace("\n", ""),
                            'OI_Lakh_2':oi_lakh_2[i].text,
                            'OI_Change_2':oi_change_2[i].text,    
                            }
        result.append(temporary_data)
    df_data=pd.DataFrame(result)
    print(df_data)



while True:
    scrape_data()
    time.sleep(30)