
from typing import Text
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
import time
import pandas as pd
options = webdriver.ChromeOptions()
options.add_argument("--headless")
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
    f = open("scrape/data/output/format2.csv", "a")
    b.get("https://www.kdnuggets.com/2017/05/42-essential-quotes-data-science-thought-leaders.html")
    i = 1
    j = 5
    id = 1
    write = []
    while(True):
        try:
            xpathq =  '/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/ol['+str(i)+']/li'
                    #/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/ol[1]/li
            #p1
            #/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/ol[1]
            #/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/ol[2]
            quote = b.find_element(By.XPATH, xpathq).text
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/ol[2]/li
            auth = b.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/p["+str(j)+"]/a/em").text
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/p[1]/a
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/p[1]/a
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/p[7]/a
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/p[1]/a/em
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[3]/p[3]/a/em
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/p[32]/a/
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/p[5]/a
                                            #p1
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/p[5]/a
                                            #/html/body/div[1]/div[1]/div[3]/div[2]/div[2]/p[7]/a
            quote = quote.replace("“", "")
            quote =  quote.replace("”", "")
            quote = quote.replace("’", "'")
            quote = quote.replace("‘", "")

            print(quote, auth)
            i+=1
            j+=2
            # f.write(f'\n{id}, "{quote}", {auth}, Data Science,')
            write = [{"id": id, "quote": quote, "author": auth, "category": "Data Science"},]
            # write.append(write2)
            df = pd.DataFrame(write)
            df.to_csv('scrape/data/output/format2.csv', mode='a',index=False, header=False)
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
    cat = "AI/ML"
    id = 78 #+1
    # id = 53 #+1
    # qi = 5 #+2
    qi = 73 #+2
    ai = 74
    while(id<=85):
        try:
            quotex = "/html/body/div[1]/div/div/div[2]/div/article/div[2]/p["+str(qi)+"]"
            #/html/body/div[1]/div/div/div[2]/div/article/div[2]/p[73]
            authx = "/html/body/div[1]/div/div/div[2]/div/article/div[2]/p["+str(ai)+"]"
            #/html/body/div[1]/div/div/div[2]/div/article/div[2]/p[55]
            #/html/body/div[1]/div/div/div[2]/div/article/div[2]/p[74]
            quote = b.find_element(By.XPATH, quotex).text
            quote = quote.replace("“", "")
            quote =  quote.replace("”", "")
            quote = quote.replace("’", "'")
            quote = quote.replace("‘", "")
            auth = b.find_element(By.XPATH, authx).text
            auth = auth.replace("– ", "")

            print(quote, auth)
            qi+=2
            ai+=2
            id+=1
            write = [{"id": id, "quote": quote, "author": auth, "category": cat},]
            # write.append(write2)
            df = pd.DataFrame(write)
            df.to_csv('scrape/data/output/format2.csv', mode='a',index=False, header=False)
        except Exception as e:
            print("error at index qi=", qi, "ai=",ai)
            print(e)
            cn = input("y/n")
            if(cn == 'y'):
                qi+=2
                ai+=2
                id+=1
                pass
            else:
                break

def scuba():
    b.get("https://www.scuba.io/blog/48-analytics-quotes-experts")
    cat = "Analytics"
    auti = 1 #+1
    quoti = 9
    id = 87 
    wid = 1
    while (wid <=50):
        try:
            authx = '/html/body/div[3]/div/div[1]/div[2]/div/span/h3['+str(auti)+']/a'
            #/html/body/div[3]/div/div[1]/div[2]/div/span/h3[2]/a
            quotex = '/html/body/div[3]/div/div[1]/div[2]/div/span/p['+str(quoti)+']'
            #/html/body/div[3]/div/div[1]/div[2]/div/span/p[10]
            auth = b.find_element(By.XPATH, authx).text
            quote = b.find_element(By.XPATH, quotex).text
            quote = b.find_element(By.XPATH, quotex).text
            quote = quote.replace("“", "")
            quote =  quote.replace("”", "")
            quote = quote.replace("’", "'")
            quote = quote.replace("‘", "")
            auth = b.find_element(By.XPATH, authx).text
            auth = auth.replace("– ", "")
            auth = auth.split(",")[0]

            print(quote, auth)
            auti+=1
            quoti+=1
            id+=1
            wid+=1
            write = [{"id": id, "quote": quote, "author": auth, "category": cat},]
            # write.append(write2)
            df = pd.DataFrame(write)
            df.to_csv('scrape/data/output/format2.csv', mode='a',index=False, header=False)
        except Exception as e:
            print(e, "wid: ",wid)
            pass


# kd()
# alab()
scuba()

# time.sleep(100)