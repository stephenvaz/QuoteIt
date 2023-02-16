
from typing import Text
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
import time

options = webdriver.ChromeOptions()

options.add_argument('--log-level=1')
# options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
options.add_experimental_option ('excludeSwitches', ['enable-logging'])
options.add_experimental_option("excludeSwitches", ["enable-automation"])
#cloudflare bypass
options.add_experimental_option('useAutomationExtension', False) 
options.add_argument("--disable-blink-features=AutomationControlled")
b = webdriver.Chrome( options=options)

def kd():
    f = open("scrape/data/output/format.csv", "a")
    b.get("https://www.kdnuggets.com/2017/05/42-essential-quotes-data-science-thought-leaders.html/2")
    i = 1
    j = 1
    id = 23
    while(True):
        try:
            xpathq =  '/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/ol['+str(i)+']/li'
                    #/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/ol[1]/li

            quote = b.find_element(By.XPATH, xpathq).text
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/ol[2]/li
            auth = b.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/p["+str(j)+"]/a/em").text
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/p[1]/a
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/p[1]/a
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/p[7]/a
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/p[1]/a/em
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/p[3]/a/em
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/p[32]/a/
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/p[5]/a
            quote = quote.replace("“", "")
            quote =  quote.replace("”", "")
            quote = quote.replace("’", "'")
            quote = quote.replace("‘", "")
            print(quote, auth)
            i+=1
            j+=2
            f.write(f'\n{id}, "{quote}", {auth}, Data Science,')
            id+=1

        except:
            print("error at index i=", i, "j=",j)
            cn = input("y/n")
            if(cn == 'y'):
                i+=1
                j+=2
                id+=1
                pass
            else:
                break

def alab():
    f = open("scrape/data/output/format.csv", "a")
    b.get("https://www.analytixlabs.co.in/blog/40-best-artificial-intelligence-quotes/#Quotes_On_Humans_need_in_AI_evolution")
    cat = "AI Evolution"
    qi = 5 #+2
    ai = 6
    quotex = "/html/body/div[1]/div/div/div[2]/div/article/div[2]/p["+str(qi)+"]"
    authx = "/html/body/div[1]/div/div/div[2]/div/article/div[2]/p[6]"

    #/html/body/div[1]/div/div/div[2]/div/article/div[2]/p[8]
    #/html/body/div[1]/div/div/div[2]/div/article/div[2]/p[5]sd
    #/html/body/div[1]/div/div/div[2]/div/article/div[2]/p[7]

# kd()


time.sleep(100)