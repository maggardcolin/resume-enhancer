import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime

headless = False

def outputJSON(indeed_posts, driver, category):
    output = []

    for post in indeed_posts:
        job_title = post['job_title']
        #print(job_title)
        link = post["link"]
        #print(link)
        driver.get(link)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'jobDescriptionText')))
        description = ""
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

    # get current time and add to json file
    now = datetime.now()
    current_date_time = now.strftime("%Y-%m-%d %H-%M-%S")
    with open(f"{category}{current_date_time}.json", 'w') as file:
        json.dump(output, file, indent=4) 

def searchJobs(job_title: str):    

    if headless:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        driver = webdriver.Chrome()

    indeed_posts = []

    driver.get(f"https://www.indeed.com/jobs?q={job_title}&l=")
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.presence_of_element_located((By.ID, 'mosaic-provider-jobcards')))
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
        
        outputJSON(indeed_posts, driver, job_title)
    except TimeoutException:
        print("Timeout while waiting for job postings to load.")
    finally:
        driver.quit()

searchJobs("mechanical engineer")