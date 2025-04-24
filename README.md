WebScraper Main
===============

This project is a web scraper designed to extract job postings from the CV Keskus website and save them as an HTML file.

Requirements
------------
- Python 3.7 or higher
- Playwright
- BeautifulSoup (part of the `bs4` package)

Installation
------------
1. Install the required Python packages:
    ```
    pip install playwright beautifulsoup4
    ```
2. Install Playwright browsers:
    ```
    playwright install
    ```

Usage
-----
1. Run the script:
    ```
    python /home/kerdon/Desktop/WebScraper\ Main/Main
    ```
2. The script will:
    - Open the CV Keskus website.
    - Scrape job postings.
    - Save the job postings to an HTML file named `IT.html`.

Output
------
- The `IT.html` file will contain a list of job postings with titles, companies, locations, and links.

Notes
-----
- The script currently waits for a long timeout (`page.wait_for_timeout(500000000)`) which should be adjusted or replaced with proper event-based waiting.
- Ensure the website structure (CSS selectors) matches the code, as changes to the website may break the scraper.

License
-------
This project is for educational purposes only. Scraping websites may violate their terms of service. Use responsibly.

