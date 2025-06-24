import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run browser in background
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Go to the website
driver.get("https://remoteok.com/remote-jobs-in-united-states")
time.sleep(5)  # Let content load fully

# Find all job rows
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

        jobs.append({
            "Job ID": job_id,
            "Title": title,
            "Company": company,
            "Location": location,
            "Tags": ", ".join(tags),
            "Date Posted": date_posted,
            "URL": link
        })
    except:
        continue  # Skip malformed rows

driver.quit()

# Save to CSV
with open("remoteok_all_us_jobs_results.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=jobs[0].keys())
    writer.writeheader()
    writer.writerows(jobs)

print(f"✅ Saved {len(jobs)} jobs to remoteok_all_us_jobs.csv")
