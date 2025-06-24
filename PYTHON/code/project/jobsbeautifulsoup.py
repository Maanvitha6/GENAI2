import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Get the webpage
url = "https://remoteok.com/remote-jobs-in-united-states"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Find all job rows
job_rows = soup.select("table#jobsboard tr.job")

# Step 3: Prepare a list to store jobs
all_jobs = []

# Step 4: Loop through each job row
for job in job_rows:
    job_id = job.get("data-id", "")
    title = job.find("h2").text.strip() if job.find("h2") else ""
    company = job.find("h3").text.strip() if job.find("h3") else ""
    location = job.get("data-location", "")
    tags = [tag.text.strip() for tag in job.select(".tag")]
    url = "https://remoteok.com" + job.get("data-href", "")

    all_jobs.append([job_id, title, company, location, ", ".join(tags), url])

# Step 5: Save to CSV
with open("remoteok_jobs.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Job ID", "Title", "Company", "Location", "Tags", "URL"])
    writer.writerows(all_jobs)

print("✅ Jobs saved to remoteok_jobs.csv")
