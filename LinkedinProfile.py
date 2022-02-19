import time
from selenium import webdriver
from bs4 import BeautifulSoup

default = "https://www.linkedin.com/in/"
username = input("Enter the username: ")
driver = webdriver.Chrome("C:/XDrivers/chromedriver.exe")
driver.get("https://www.linkedin.com/login")
driver.maximize_window()

driver.find_element_by_id("username").send_keys("rohanstomar11@gmail.com")
driver.find_element_by_id("password").send_keys("Linkedin@roh@n11")
driver.find_element_by_xpath("//button[@type='submit']").click()

profile_url = default+username
driver.get(profile_url)

start = time.time()

initialScroll = 0
finalScroll = 1000

while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")

    initialScroll = finalScroll
    finalScroll += 1000

    end = time.time()

    if round(end - start) > 20:
        break

src = driver.page_source

soup = BeautifulSoup(src, 'lxml')
name = soup.find('h1')
works = soup.find('div', {'class': 'text-body-medium break-words'})
location = soup.find(
    'span', {'class': 'text-body-small inline t-black--light break-words'})

print("Name: ", name.text)
print("Company: ", works.text.strip())
print("Location: ", location.text.strip())

driver.close()