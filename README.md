# Tööpakkumised ja Mälumäng

This project is a Python script that fetches job listings from CV Keskus based on the user's input for city and category, and displays the results in an HTML file. If no jobs are found, it activates a memory game as a backup.

Features
1. **Fetch Job Listings**: The script queries the CV Keskus website for job listings based on a specific city and job category.
2. **HTML Output**: It generates an HTML file with the job listings, displaying job titles, company names, locations, and links.
3. **Backup Memory Game**: If no job listings are found, a memory game is activated to entertain the user.

## Requirements
Before running this script, you need to install the following Python packages:

`playwright`
`beautifulsoup4`
`pygame`

You can install the necessary dependencies by running:

```bash
pip install playwright beautifulsoup4 pygame
Additionally, you'll need to install Playwright dependencies by running:

bash
Copy
Edit
python -m playwright install
Usage
Run the script:

After setting up the required dependencies, you can run the script directly.

bash
Copy
Edit
python <script_name>.py
Input:

The script will ask for the following user input:

Sisesta oma linn: Enter the city (e.g., Tallinn, Tartu).

Sisesta oma valdkond: Enter the job category (e.g., IT, Marketing).

Job Listings:

If job listings are found for the specified city and category, they will be fetched from CV Keskus, and an HTML file will be generated with the job information.

Backup Memory Game:

If no jobs are found, the script will activate a memory game, which you can play using the following rules:

The board has pairs of icons.

Click on the boxes to reveal the icons and try to match them.

The game ends when all pairs are matched.

How It Works
1. Fetching Jobs
The script queries CV Keskus for job listings based on the city and category input by the user. The query URL is adjusted dynamically based on the user's input.

City: The city is converted to lowercase and spaces are replaced with "+" for URL formatting.

Category: If a category is specified, it is also converted to lowercase.

2. Parsing Jobs
Once the job listings page is loaded, the script uses BeautifulSoup to extract:

Job Title

Company Name

Location

Job Listing Link

3. Saving Jobs to HTML
If jobs are found, they are saved to an HTML file. The filename is based on the city input and includes the list of job titles, companies, and locations with clickable links.

4. Backup Memory Game
If no jobs are found, a memory game is started as a backup. The game features a randomized board with pairs of icons that you need to match. The game continues until all pairs are found.

5. Error Handling
If the job listings cannot be fetched, the script will automatically try again, showing a message indicating the issue.

If no job listings are found after the retries, the memory game will be activated instead.

Example
Input:
yaml
Copy
Edit
Sisesta oma linn: Tallinn
Sisesta oma valdkond: IT
Output:
If job listings are found, an HTML file named toopakkumised_tallinn.html will be created.

If no job listings are found, the memory game will start.

Memory Game Controls
Click on the boxes to reveal icons.

Match pairs of icons by clicking on two boxes with the same icon.

The game ends when all pairs are matched.

Conclusion
This script provides a fun and interactive way to fetch job listings from CV Keskus and a memory game as a fallback if no jobs are found. Feel free to modify the script to suit your needs or expand the functionality.
