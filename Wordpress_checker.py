#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from xlwt import Workbook

path=input("Enter the path of the chromiumdriver.exe File: ")
driver=webdriver.Chrome(executable_path=path)
url=input("Enter the url of the Wordpress Website admin page:")
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)
file_path=input("Enter the Excel file path having Username and password combos: ")
num=int(input("Enter number of username-password combos in the file: "))
df = pd.read_excel (file_path) #for an earlier version of Excel, you may need to use the file extension of 'xls'
username=df["Username"]
password=df["Password"]
result=[]
wb=Workbook()
print("In Progress...")
time_taken=num*int(10);
print("It will take approximate "+ str(time_taken)+" seconds")
for i in range (num):
    k=int(i)
    usr=username[k]
    psd=password[k]
    driver.find_element_by_xpath("//*[@id='user_login']").send_keys(usr)
    driver.find_element_by_xpath("//*[@id='user_pass']").send_keys(psd)
    driver.find_element_by_xpath("//*[@id='wp-submit']").click()
    time.sleep(3)    
    
    if(driver.current_url==url):
        result.append("Fail")
        time.sleep(3) 
        
    else:
        time.sleep(8) 
        #print("yes")
        result.append("Pass")
        time.sleep(4)
        admin=driver.find_element_by_xpath("//*[@id='wp-admin-bar-my-account']/a/img")
        logout=driver.find_element_by_xpath("//*[@id='wp-admin-bar-logout']/a")
        actions=ActionChains(driver)
        actions.move_to_element(admin).perform()
        time.sleep(4)
        actions.move_to_element(logout).click().perform()
        time.sleep(8)

df['Result']=result        
df.to_excel("desktop/Result.xlsx")
driver.close()
print("Process Successfully Completed!")


# In[ ]:





# In[ ]:




