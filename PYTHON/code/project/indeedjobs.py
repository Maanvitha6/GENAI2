import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # optional: hide browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Define search URL for Data Analyst jobs in USA
base_url = "https://www.indeed.com/jobs?q=data+analyst&l=USA&start={}"

jobs = []

# Loop over multiple pages (each page = 10 jobs, so for 1000 -> 100 pages)
for page in range(0, 1000, 10):
    url = base_url.format(page)
    driver.get(url)
    time.sleep(3)

    job_cards = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")
    for card in job_cards:
        try:
            title = card.find_element(By.CSS_SELECTOR, "h2.jobTitle").text
            company = card.find_element(By.CLASS_NAME, "companyName").text
            location = card.find_element(By.CLASS_NAME, "companyLocation").text
            summary = card.find_element(By.CLASS_NAME, "job-snippet").text
            link = card.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

            jobs.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "Summary": summary,
                "Link": link
            })
        except:
            continue

    print(f"✅ Scraped page: {page // 10 + 1} | Total jobs: {len(jobs)}")

    if len(jobs) >= 1000:
        break

driver.quit()

# Save to CSV
with open("indeed_data_analyst_jobs.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=jobs[0].keys())
    writer.writeheader()
    writer.writerows(jobs)

print(f"\n✅ Done! Saved {len(jobs)} jobs to indeed_data_analyst_jobs.csv")
