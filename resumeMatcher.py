from pdfminer.high_level import extract_text
import docx2txt
import nltk
import time
import os
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages')


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyresparser import ResumeParser





nltk.download('stopwords')
import warnings
warnings.filterwarnings("ignore")

def convertResumeToText(file):
    data = ResumeParser(file).get_extracted_data()
    return data['skills']


def getOccupation():  
    # Path to your ChromeDriver
    chrome_driver_path = '/Users/advikmareedu/Desktop/ResumeProject/chromedriver-mac-arm64/chromedriver'

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"download.default_directory": "/Users/advikmareedu/Desktop"})
    

    # Create a Service object for ChromeDriver
    service = Service(chrome_driver_path)

    # Initialize the ChromeDriver with the Service object and options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the specified URL
    driver.get("https://www.meta.ai/?utm_source=ai_meta_site&utm_medium=web&utm_content=MetaAI_page&utm_campaign=April_moment")

    # Minimize the browser window
    driver.maximize_window()
    time.sleep(2)

    textField = driver.find_element(By.XPATH, '//*[@id=":rh:"]')
    textField.send_keys("mank")
    textField.send_keys(Keys.ENTER)
    time.sleep(5)



    # Optionally, interact with the page
    # username = "advikhope@gmail.com"
    # userField = driver.find_element(By.XPATH, '//*[@id="email-input"]')
    # userField.send_keys(username)
    # continueButton = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/section/div[2]/button')
    # continueButton.click()
    # time.sleep(2)

    # password = "heritageoak"
    # passField = driver.find_element(By.XPATH, '//*[@id="password"]')
    # passField.send_keys(password)
    # submitButton = driver.find_element(By.XPATH,'/html/body/div[1]/main/section/div/div/div/form/div[2]/button')
    # submitButton.click()
    # time.sleep(5)


    


#passIntoGPT()
#jobName = getOccupation()
# Path to your ChromeDriver

def findLinkedIn():
    chrome_driver_path = '/Users/advikmareedu/Desktop/ResumeProject/chromedriver-mac-arm64/chromedriver'

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"download.default_directory": "/Users/advikmareedu/Desktop"})

    # Create a Service object for ChromeDriver
    service = Service(chrome_driver_path)

    # Initialize the ChromeDriver with the Service object and options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    

    # Open the specified URL
    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

    # Minimize the browser window
    driver.minimize_window()
    time.sleep(2)

    # Optionally, interact with the page
    username = "advikhope@gmail.com"
    userField = driver.find_element(By.XPATH, '//*[@id="username"]')
    userField.send_keys(username)
    time.sleep(2)

    password = "Heritageoak#1"
    passField = driver.find_element(By.XPATH, '//*[@id="password"]')
    passField.send_keys(password)
    submitButton = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
    submitButton.click()
    time.sleep(5)

    searchBar = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
    searchBar.send_keys("Dentist Internships and Jobs")
    searchBar.send_keys(Keys.ENTER)
    time.sleep(2)
    currentURL = driver.current_url
    return currentURL

def findIndeed():
    chrome_driver_path = '/Users/advikmareedu/Desktop/ResumeProject/chromedriver-mac-arm64/chromedriver'

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"download.default_directory": "/Users/advikmareedu/Desktop"})
    # Create a Service object for ChromeDriver
    service = Service(chrome_driver_path)

    # Initialize the ChromeDriver with the Service object and options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the specified URL
    driver.get("https://www.indeed.com/")

    # Minimize the browser window
    driver.minimize_window()
    time.sleep(1)



    searchBar = driver.find_element(By.XPATH, '//*[@id="text-input-what"]')
    searchBar.send_keys("Dentist Internships and Jobs")
    searchBar.send_keys(Keys.ENTER)
    time.sleep(2)
    currentURL = driver.current_url
    return currentURL

def findDice():
    chrome_driver_path = '/Users/advikmareedu/Desktop/ResumeProject/chromedriver-mac-arm64/chromedriver'

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"download.default_directory": "/Users/advikmareedu/Desktop"})

    # Create a Service object for ChromeDriver
    service = Service(chrome_driver_path)

    # Initialize the ChromeDriver with the Service object and options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the specified URL
    driver.get("https://www.dice.com/jobs?countryCode=US&radius=30&radiusUnit=mi&page=1&pageSize=20&language=en&eid=0345")

    # Minimize the browser window
    driver.minimize_window()
    time.sleep(2)

    # Optionally, interact with the page

    searchBar = driver.find_element(By.XPATH, '//*[@id="typeaheadInput"]')
    searchBar.send_keys("Dentist")
    searchBar.send_keys(Keys.ENTER)
    time.sleep(2)
    currentURL = driver.current_url
    return currentURL

def findSimplyHired():
    chrome_driver_path = '/Users/advikmareedu/Desktop/ResumeProject/chromedriver-mac-arm64/chromedriver'

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"download.default_directory": "/Users/advikmareedu/Desktop"})

    # Create a Service object for ChromeDriver
    service = Service(chrome_driver_path)

    # Initialize the ChromeDriver with the Service object and options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the specified URL
    driver.get("https://www.simplyhired.com/browse-jobs/titles")

    # Minimize the browser window
    driver.minimize_window()
    time.sleep(1)

    # Optionally, interact with the page
    searchBar = driver.find_element(By.XPATH, '//*[@id="field-:R3baikqlfbqm:"]')
    searchBar.send_keys("Dentist")
    searchBar.send_keys(Keys.ENTER)
    time.sleep(2)
    currentURL = driver.current_url
    return currentURL

def findGlassDoor():
    chrome_driver_path = '/Users/advikmareedu/Desktop/ResumeProject/chromedriver-mac-arm64/chromedriver'

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"download.default_directory": "/Users/advikmareedu/Desktop"})

    # Create a Service object for ChromeDriver
    service = Service(chrome_driver_path)

    # Initialize the ChromeDriver with the Service object and options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the specified URL
    driver.get("https://www.glassdoor.com/Job/index.htm")

    # Minimize the browser window
    driver.minimize_window()
    time.sleep(2)

    # Optionally, interact with the page
    searchBar = driver.find_element(By.XPATH, '//*[@id="searchBar-jobTitle"]')
    searchBar.send_keys("Dentist")
    searchBar.send_keys(Keys.ENTER)
    time.sleep(2)
    currentURL = driver.current_url
    return currentURL


def findUSAJobs():
    chrome_driver_path = '/Users/advikmareedu/Desktop/ResumeProject/chromedriver-mac-arm64/chromedriver'

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"download.default_directory": "/Users/advikmareedu/Desktop"})

    # Create a Service object for ChromeDriver
    service = Service(chrome_driver_path)

    # Initialize the ChromeDriver with the Service object and options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the specified URL
    driver.get("https://www.usajobs.gov/search?")

    # Minimize the browser window
    driver.minimize_window()
    time.sleep(2)

    # Optionally, interact with the page
    searchBar = driver.find_element(By.XPATH, '//*[@id="nav-keyword"]')
    searchBar.send_keys("Dentist")
    searchBtn = driver.find_element(By.XPATH, '//*[@id="usajobs-search-form"]/form/fieldset/div[3]/button')
    searchBtn.click()
    time.sleep(2)
    currentURL = driver.current_url
    return currentURL










#resumeText = extract_text('Advik_Mareedu_Resume.pdf')


 


