import os

base_dir = os.path.split(os.path.realpath(__file__))[0].replace("Common","")

#日志目录
log_dir = base_dir + "Logs/"

#测试报告目录
report_dir = base_dir + "HtmlReport/"

#截图目录
image_dir = base_dir + "Images/"

#安装包位置
package_dir = r"C:\Users\user\AppData\Local\Programs\erp-client\派药房.exe"

#chromedriver
chrome_dir = r"C:\Users\user\AppData\Local\Google\Chrome\Application\chromedriver.exe"