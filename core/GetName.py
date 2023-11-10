from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import csv
import sys
import time
import os

class GetOrderList:
    def get_order_lists(url, usename, us_password, start_time, end_time, path):
        # Open and Login in
        print("代码运行中，请千万不要动鼠标，不要操作浏览器，将持续几分钟，谢谢！")
        print("执行完毕后将自动关闭浏览器页面")
        sleep(2)
        driver = webdriver.Firefox()
        try:
            driver.get(url)
            driver.maximize_window()
            driver.implicitly_wait(10)
            username = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/label[1]/input")
            password = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/label[2]/input")
            username.send_keys(usename)
            password.send_keys(us_password)
            driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/p[1]").click()
            driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]").click()
            driver.implicitly_wait(15)
            # 点击订单列表
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/a[2]").click()
            # 点击搜索
            driver.implicitly_wait(15)
            driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/form/input").click()
            # 选择起始时间+确认
            driver.find_element(By.XPATH, "//*[@id='fieldDate1']").send_keys(start_time)
            driver.find_element(By.XPATH, "//*[@id='fieldDate2']").send_keys(end_time)
            driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/form/div[2]/div/label[1]/div/div/input").click()
            sleep(2)
            driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/form/div[2]/div/label[1]/div/dl/dd[1]").click()
            driver.implicitly_wait(15)
            # Loop through pages
            timestamp = time.time()
            time_struct = time.localtime(timestamp)
            formatted_time = time.strftime("%Y%m%d%H%M%S", time_struct)
            if not os.path.exists(path):
                os.mkdir(path)
            file_name = f"{path}\\order_info_{start_time}_{end_time}_{formatted_time}.csv"
            for i in range(1, 1000 + 1):
                sleep(15)
                count = len(driver.find_elements(By.XPATH, "//div[@id='orderList']/div")) + 1
                # Loop through elements on the page
                for index in range(1, count):
                    order_time = driver.find_element(By.XPATH,
                                                     f"/html/body/div[4]/div[1]/div[6]/div[{index}]/div[3]/div[2]/div[1]/div[1]").text
                    order_time = str(order_time).split("\n")[1]
                    order_status = driver.find_element(By.XPATH,
                                                       f"/html/body/div[4]/div[1]/div[6]/div[{index}]/div[3]/div[2]/div[2]/div[@class='text state layui-hide-xs']").text
                    order_status = str(order_status).split("\n")[1]
                    order_id = driver.find_element(By.XPATH,
                                                   f"/html/body/div[4]/div[1]/div[6]/div[{index}]/div[1]/div[1]").text
                    order_name_element = driver.find_element(By.XPATH,
                                                             f"/html/body/div[4]/div[1]/div[6]/div[{index}]/div[3]/div[2]/div[1]//div[@class='text']/span[text()='配送员：']/..").text
                    order_name_element = str(order_name_element).split("\n")[1]
                    if order_name_element == "无":
                        order_phone = "空"
                    else:
                        order_phone = driver.find_element(By.XPATH,
                                                          f"/html/body/div[4]/div[1]/div[6]/div[{index}]/div[3]/div[2]/div[1]/div[3]/div[2]/p").text if '无' not in order_name_element else ''
                    with open(file_name, 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([order_time, order_id, order_name_element, order_status, order_phone])

                val = driver.find_element(By.XPATH, "//div[@id='layui-laypage-1']/a[text()='下一页']").get_attribute("class")
                if val != 'layui-laypage-next':
                    break
                driver.find_element(By.XPATH, "//a[@class='layui-laypage-next']").click()
            print(f"您获取的信息已经写在此路径下：{file_name}")
        finally:
            driver.close()


url = "http://sf.myps188.com"
usename = sys.argv[1]
password = sys.argv[2]
start_time =  sys.argv[3]
end_time =  sys.argv[4]
path = sys.argv[5]

GetOrderList.get_order_lists(url, usename, password, start_time, end_time, path)
