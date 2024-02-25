# this scrapes indeed's site and calls the parseJSON script
# input: search string
# processing: finding job titles and links to do with the search string
# output: json file containing job descriptions

# author: Colin Maggard

import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from parseJSON import *

# outputs to json and calls process_json in the parseJSON script
def outputJSON(indeed_posts, driver, category):
    output = []

    # iterate through each post and check their full page
    for post in indeed_posts:
        job_title = post['job_title']
        link = post["link"]
        driver.get(link)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'jobDescriptionText')))
        description = ""

        # copy the entire page, pretty much
        try:
            description_fields = driver.find_elements(By.CSS_SELECTOR, 'p')
            for d in description_fields:
                description += d.text + " "
        except Exception as e:
            pass
        try:
            description_fields = driver.find_elements(By.CSS_SELECTOR, 'ul li')
            for d in description_fields:
                description += d.text + " "
        except Exception as e:
            pass

        output.append({'job_title': job_title, 'description': description})

    # get current time and add to json file, this will be deleted later and is intermediary
    now = datetime.now()
    current_date_time = now.strftime("%Y-%m-%d %H-%M-%S")
    with open(f"./output/{category}{current_date_time}.json", 'w') as file:
        json.dump(output, file, indent = 4)
    the_final_file = process_json(f"./output/{category}{current_date_time}.json", category)
    return the_final_file

# this is called by main file
def searchJobs(job_title: str):    

    print("Now scanning job descriptions matching \"" + job_title + "\". Please wait, this may take ~30 seconds or longer.")

    # TODO make work with headless, currently times out when you try to do that
    headless = True

    if headless:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        # to make sure it is allowed to run headless
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-logging')
        chrome_options.add_argument('--log-level=3')
        # suppresses DevTools message
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options = chrome_options)
    else:
        driver = webdriver.Chrome()

    indeed_posts = []

    driver.get(f"https://www.indeed.com/jobs?q={job_title}&l=")
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.visibility_of_element_located((By.ID, 'mosaic-provider-jobcards')))
        job_cards = driver.find_elements(By.CLASS_NAME, 'css-5lfssm')
        
        indeed_posts = []
        for card in job_cards:

            # Extracting job title, company name, and link to the job posting
            try:
                job_title_element = card.find_element(By.CSS_SELECTOR, 'span').text
            except:
                pass
            try:
                link = card.find_element(By.CLASS_NAME, 'jcs-JobTitle').get_attribute('href')
            except:
                pass
            
            indeed_posts.append({'job_title': job_title_element, 'link': link})
        
        the_final_file = outputJSON(indeed_posts, driver, job_title)
    except TimeoutException:
        print("Timeout while waiting for job postings to load.")
    finally:
        driver.quit()
    return the_final_file