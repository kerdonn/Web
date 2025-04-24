from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def get_tootukassa_jobs():
    url = "https://www.tootukassa.ee/toopakkumised"
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    jobs = []

    # Töötukassa tööpakkumised
    for job in soup.find_all('article', class_='job-item'):
        title = job.select_one('.job-title')
        company = job.select_one('.employer')
        location = job.select_one('.location')
        if title and company:
            jobs.append({
                'title': title.get_text(strip=True),
                'company': company.get_text(strip=True),
                'location': location.get_text(strip=True) if location else 'Asukoht puudub',
                'link': job.find('a')['href']
            })
    driver.quit()
    print(f"Leiti {len(jobs)} tööpakkumist Töötukassast")
    return jobs

def get_cvkeskus_jobs():
    url = "https://www.cvkeskus.ee/toopakkumised"
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    jobs = []

    # CV Keskuse tööpakkumised
    for job in soup.select('.classifieds__item'):
        title = job.select_one('.classifieds__header a')
        company = job.select_one('.classifieds__employer')
        location = job.select_one('.classifieds__location')
        if title and company:
            jobs.append({
                'title': title.get_text(strip=True),
                'company': company.get_text(strip=True),
                'location': location.get_text(strip=True) if location else 'Asukoht puudub',
                'link': "https://www.cvkeskus.ee" + title['href']
            })
    driver.quit()
    print(f"Leiti {len(jobs)} tööpakkumist CVKeskusest")
    return jobs

def save_as_html(jobs, filename="toopakkumised.html"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("<html><head><meta charset='UTF-8'><title>Tööpakkumised</title>")
        f.write("<style>body{font-family:Arial;} ul{list-style:none; padding:0;} li{margin-bottom:10px;}</style></head><body>")
        f.write("<h1>Tööpakkumised</h1><ul>")
        for job in jobs:
            f.write(f"<li><a href='{job['link']}' target='_blank'>{job['title']}</a> – {job['company']} ({job['location']})</li>")
        f.write("</ul></body></html>")

if __name__ == "__main__":
    tootukassa_jobs = get_tootukassa_jobs()
    cvkeskus_jobs = get_cvkeskus_jobs()

    all_jobs = tootukassa_jobs + cvkeskus_jobs
    print(f"Kokku leitud {len(all_jobs)} tööpakkumist.")

    if all_jobs:
        save_as_html(all_jobs)
        print("Töökuulutused salvestatud faili: toopakkumised.html")
    else:
        print("Töökuulutusi ei leitud.")
# This code scrapes job listings from Töötukassa and CV Keskus websites using Selenium and BeautifulSoup.
# It saves the listings in an HTML file with links to the job postings.
# The script uses headless Chrome for web scraping and handles dynamic content loading.
# The code is structured to fetch job listings, parse the HTML content, and save the results in a user-friendly format.
# The script is designed to be run as a standalone program, and it prints the number of job listings found.
# The script is modular, with separate functions for fetching job listings from each website and saving the results.            