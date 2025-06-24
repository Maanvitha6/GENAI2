import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Optional: run without opening a window
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Go to the website
driver.get("https://remoteok.com/remote-jobs-in-united-states")
time.sleep(5)  # Let content load

# Scrape job rows
job_rows = driver.find_elements(By.CSS_SELECTOR, "tr.job")
jobs = []

for job in job_rows:
    try:
        job_id = job.get_attribute("data-id")
        title = job.find_element(By.CSS_SELECTOR, "h2").text
        company = job.find_element(By.CSS_SELECTOR, "h3").text
        location = job.get_attribute("data-location")
        tags = [t.text for t in job.find_elements(By.CSS_SELECTOR, ".tag")]
        date_posted = job.find_element(By.TAG_NAME, "time").get_attribute("datetime")
        link = job.find_element(By.CSS_SELECTOR, "a.preventLink").get_attribute("href")

        jobs.append((job_id, title, company, date_posted, link))  # Location & Tags excluded
    except:
        continue

driver.quit()

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",                # Replace with your MySQL username
    password="Maanvitha@2002",    # Replace with your MySQL password
    database="jobdata"          # Use your existing database
)
cursor = conn.cursor()

# Create table (skip if already exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS remoteok_live_jobs (
    job_id VARCHAR(20),
    title VARCHAR(255),
    company VARCHAR(255),
    date_posted DATETIME,
    url TEXT
);
""")

# Insert job records
for job in jobs:
    cursor.execute("""
        INSERT INTO remoteok_live_jobs (job_id, title, company, date_posted, url)
        VALUES (%s, %s, %s, %s, %s)
    """, job)

conn.commit()
conn.close()

print(f"✅ Inserted {len(jobs)} jobs into MySQL table 'remoteok_live_jobs'")

# to view the data in mysql, run these commands in sql server
# USE jobdata;
 # SELECT * FROM remoteok_live_jobs LIMIT 1000;