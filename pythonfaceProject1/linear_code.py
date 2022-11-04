import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

c_path = R'C:\Users\HP\PycharmProjects\pythonProject\selenium_HTd12\driver\chromedriver.exe'
c_driver = webdriver.Chrome(executable_path=c_path)
c_driver.implicitly_wait(10)

a_obj = ActionChains


file_path = r'https://www.facebook.com/'
c_driver.get(file_path)
c_driver.maximize_window()

username = c_driver.find_element("xpath",'//input[@id="email"]')
username.click()
username.send_keys(8805550026)

password = c_driver.find_element("xpath","//input[@id='pass']")
password.click()
password.send_keys("Facebook12")
time.sleep(3)
c_driver.find_element("xpath","//button[text()='Log in']").click()  #(logiN)
time.sleep(3)
c_driver.find_element("xpath",'//a[@aria-label="Watch"]').click()  #(watch)
time.sleep(8)
c_driver.find_element("xpath","//div[@aria-label='Edit notification settings']").click()  #(setting)
time.sleep(5)
c_driver.find_element("xpath", "(//input[@aria-label='Show notification dots'])[1]").click() #(noti start)
time.sleep(5)
c_driver.find_element("xpath", "(//span[normalize-space()='Custom notifications'])[1]").click() #(custom noti)
time.sleep(5)
c_driver.find_element("xpath","(//input[@aria-label='Opted out all badge types'])[1]").click() #(allow video noti)
time.sleep(4)
c_driver.find_element("xpath",'(//i[@class="x1b0d499 xep6ejk"])[14]').click() #(new video noti)
time.sleep(8)

c_driver.find_element("xpath",'(//div[@class="x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1qughib x6s0dn4 xozqiw3 x1q0g3np"])[18]').click() #(manage page)
time.sleep(8)

obj = ActionChains(c_driver)
cross = c_driver.find_element("xpath","(//div[@aria-label='Close' and @role='button'])[2]")  #(cross button)
obj.click(cross).perform()
time.sleep(3)


#c_driver.find_element("xpath","(//input[@placeholder='Search videos'])[1]").click() #(search bar)
#c_driver.find_element("xpath","(//input[@placeholder='Search videos'])[1]").send_keys('cat funny video')


c_driver.find_element("xpath", "(//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft'][normalize-space()='Live'])[1]").click()  #(live)
time.sleep(3)
c_driver.find_element("xpath", '(//span[text()="Shows"])[1]').click()  #(show)
# #c_driver.find_element("xpath",'(//div[@role="presentation"])[2]').click()  #(start)
# #c_driver.find_element("xpath","(//i[@class='x1b0d499 xaj1gnb'])[2]").click()  #(pause)
# c_driver.find_element("xpath","(//input[@placeholder='Search videos'])[1]").click()  #(search)
#
#
c_driver.close()



#WebDriverWait(c_driver,20).until(EC.element_to_be_clickable((By.xpath,'(//div[@role="presentation"])[1]'))).click() #(start)
#time.sleep(2)
#a_obj = ActionChains(c_driver)
#start = c_driver.find_element("xpath","(//div[@data-pagelet='MainFeed'])[1]")
#a_obj.double_click(start).perform()
#time.sleep(3)

#a_obj = ActionChains(c_driver)
#start = c_driver.find_element("xpath","(//i[@class='x1b0d499 xaj1gnb'])[9]")
#a_obj.move_to_element(start).perform()

#c_driver.find_element("xpath","(//span[contains(text(),'Like')])[1]").click() #(like not work)
#c_driver.find_element("xpath","(//i[@class='x1b0d499 x1d69dk1'])[3]").click()  #(comment not work)


#c_driver.find_element("xpath", "(//input[@aria-label='Show notification dots'])[1]").click() #(noti pause)
#time.sleep(3)

#c_driver.find_element("xpath","(//i[@class='x1b0d499 x1d69dk1'])[11]").click() #(cross button)

#c_driver.find_element("xpath","(//i[@class='x1b0d499 xep6ejk'])[10]").click()   #(new video)



#(//i[@class='x1b0d499 xep6ejk'])[2] (setting)
#(//div[@class="__fb-light-mode x1qjc9v5 x9f619 x78zum5 xdt5ytf xl56j7k x1c4vz4f xg6iff7"]) (manage)