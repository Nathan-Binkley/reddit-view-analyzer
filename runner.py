from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import keys
import json
import csv

driver = webdriver.Chrome()
driver.implicitly_wait(15)

def safety_wait(timer=2):
    time.sleep(timer)

def login():

    driver.get("https://new.reddit.com/")
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/header/div/div[2]/div/div[1]/a[1]').click()
    driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/div/iframe'))
    safety_wait()
    driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div/div/form/fieldset[1]/input').send_keys(keys.username)
    driver.find_element(By.NAME, "password").send_keys(keys.password)
    safety_wait()
    driver.find_element(By.CLASS_NAME, "AnimatedForm__submitButton").click()
    driver.switch_to.default_content()
    safety_wait()
    print("Logged In -- Hopefully")
    


def get_urls():
    with open('urls.txt', 'r') as f:
        return f.read().splitlines()



def write_data(data):
    with open('out.json', 'w') as f:
        json.dump(data, f, indent=4)

info = []

login()

urls = get_urls()

for i, v in enumerate(urls):

    website = "https://new.reddit.com" + v
    if driver.current_url != website:
        driver.get(website)
    print("WANT TO GO:", website)
    print("CURRENT URL:", driver.current_url)
    print("Waiting for content to load... (15 seconds)")
    safety_wait(5)
    site = {}
    site['url'] = v
    try:
        site['views'] = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]').text #Views in insights
    except:
        site['views'] = "N/A"
    try:
        site['upvote_ratio'] = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]').text #Upvote ratio in insights
    except:
        site['upvote_ratio'] = "N/A"
    try:
        site['shares'] = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div[4]/div[1]').text #Shares in insights
    except:
        site['shares'] = "N/A"
    try:
        site['current_score'] = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[1]/div/div[1]/div/div').text #current score
    except:
        site['current_score'] = "N/A"

    info.append(site)
    write_data(info)
    print('done with ', i, "out of", len(urls))




