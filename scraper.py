import requests
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("./chromedriver")

desired_position = input('what job would you like search for?')

new_desired_position = desired_position.split(" ")
separator = "%20"

url_version_of_job = separator.join(new_desired_position)
# print(url_version_of_job)


URL = f'https://www.indeed.ca/jobs?q={url_version_of_job}&l=vancouver'
driver.get(URL)

def scrape_indeed():

  all_jobs = driver.find_elements_by_class_name('result')

  i = 1
  for job in all_jobs:
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
    print(link)

    message = f"{i}. the position is listed as '{title}' and is located at {location}"
    print(message)
    i = i + 1
  send_email()

def send_email():
  print("EMAIL HAS BEEN SENT")

scrape_indeed()

