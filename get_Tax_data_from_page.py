from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import messagebox
import time
import csv
import os

url = "https://12366.chinatax.gov.cn/sszyfw/bulletinBoard/main"
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(15)
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='common']/div[2]/span").click()
driver.find_element(By.XPATH, "//*[@id='common']/div[2]/ul/li[1]").click()
driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div[2]/div[2]/div[2]/div/a[1]").click()

for page_count in range(100):
    try:
        element =  driver.find_element(By.XPATH, "//*[@id='dialog-win']")
        while element:
            print("请输入图片中的数字，并且点击确认键！！！")
            time.sleep(20)
            element = driver.find_element(By.XPATH, "//*[@id='dialog-win']")
    except:
        for index in range(2, 17):
            com_name = driver.find_element(By.XPATH, f"/html/body/div/div[4]/div/div[1]/div/div[2]/table/tbody/tr[{index}]/td[1]").text
            law_name = driver.find_element(By.XPATH, f"/html/body/div/div[4]/div/div[1]/div/div[2]/table/tbody/tr[{index}]/td[2]").text
            address = driver.find_element(By.XPATH, f"/html/body/div/div[4]/div/div[1]/div/div[2]/table/tbody/tr[{index}]/td[3]").text
            header = ['机构名称', '法定代表人', '机构地址']
            current_directory = os.getcwd()
            file_name = f"{current_directory}\\log.csv"
            with open(file_name, 'a', newline='') as file:
                writer = csv.writer(file)
                if file.tell() == 0:
                    writer.writerow(header)
                writer.writerow(
                    [com_name, law_name, address])
        driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div[1]/div/div[2]/div/div/div[8]/a").click()
    time.sleep(10)
