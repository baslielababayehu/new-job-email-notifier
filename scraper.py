import requests
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("./chromedriver")

# desired_position = input('what job would you like search for?')
desired_position = "software engineering intern"

new_desired_position = desired_position.split(" ")
separator = "%20"

url_version_of_job = separator.join(new_desired_position)
# print(url_version_of_job)


URL = f'https://www.indeed.ca/jobs?q={url_version_of_job}&l=vancouver'
driver.get(URL)

all_jobs = driver.find_elements_by_class_name('result')

def scrape_indeed():
  i = 1
  array_of_all_jobs = []
  for job in all_jobs:
    array_of_individual_jobs = []
    result_html = job.get_attribute('innerHTML')
    soup = BeautifulSoup(result_html, 'html.parser')

    # Finds the Title of the job 
    try:
      title = soup.find("a", class_="jobtitle").text.strip()
      # print(title)
    except:
      title ='No title Listed'

    # FInds the Location of the Job
    try:
      location = soup.find(class_="location").text.strip()
      # print(location)
    except:
      location = "No Location Listed"
    
    # link = soup.find("a", class_="jobtitle").href
    # print(link)

    job_summary_div = job.find_elements_by_class_name("summary")[0]

    try:
      job_summary_div.click()
    except:
      try:
        close_popover = driver.find_elements_by_class_name("popover-x-button-close")
        close_popover.click()
        job_summary_div.click()
      except:
        print("do something else")
    description = driver.find_element_by_id('auxCol')[1]
    print(description)
    # analyze_description()

    message = f"{i}. the position is listed as '{title}' and is located at {location}"
    # print(message)
    array_of_individual_jobs.append(title)
    array_of_individual_jobs.append(location)
    array_of_all_jobs.append(array_of_individual_jobs)


    i = i + 1
  # print(array_of_all_jobs)
  send_email()

def send_email():
  print("EMAIL HAS BEEN SENT")


def analyze_description():

  for description in all_jobs:
    result_html = description.get_attribute('innerHTML')
    soup = BeautifulSoup(result_html, 'html.parser')
    try:
      job_description = soup.find(id="jobsearch-SerpJobCard").text
    except:
      job_description= "nothing found"
  
    print(job_description)
    print("analyzing job description")
  # use selenium to find job description

  # search for a specified key word 

  # record the number of times a word appears 

  # Assign a score to the description 
scrape_indeed()

driver.close()