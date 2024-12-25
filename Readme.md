Selenium Web Scraping and Cross-Browser Testing Project

This repository contains a Selenium-based project that demonstrates skills in web scraping, API integration, and text processing, as well as cross-browser testing using BrowserStack. The project is structured to follow the requirements outlined in the technical assignment.

Project Overview

Key Objectives:
	1.	Web Scraping:
	•	Visit the El País Spanish news website.
	•	Ensure that the website’s text is displayed in Spanish.
	•	Navigate to the Opinion section and scrape the first five articles:
	•	Fetch and print the title and content of each article in Spanish.
	•	Download and save the cover image of each article (if available).
	2.	API Integration:
	•	Translate the titles of the articles to English using a translation API, such as the Google Translate API.
	•	Print the translated titles in English.
	3.	Text Processing:
	•	Analyze the translated headers to identify words repeated more than twice across all headers combined.
	•	Print the repeated words along with their counts.
	4.	Cross-Browser Testing:
	•	Validate the solution locally to ensure functionality.
	•	Execute the solution on BrowserStack across five parallel threads, testing a combination of desktop and mobile browsers.

Technologies Used
	•	Programming Language: Python
	•	Web Automation Framework: Selenium
	•	API Integration: Google Translate API
	•	Cross-Browser Testing: BrowserStack
	•	Other Libraries:
	•	os for file handling
	•	requests for API integration
	•	json for data processing
	•	collections for text processing

Prerequisites
	1.	Python: Ensure Python 3.x is installed on your system.
	2.	BrowserStack Credentials:
	•	Access your BrowserStack account and note the username and access key.
	3.	Selenium WebDriver:
	•	Tested using the Chrome driver locally.
	4.	Google Translate API Key:
	•	Sign up for the Google Translate API or an equivalent service.
	•	Store the API key in a configuration file or as an environment variable.
	5.	Dependencies:
Install all required libraries using:

pip install -r requirements.txt

Project Workflow

1. Setup and Initialization:
	•	Configure the Selenium WebDriver with BrowserStack capabilities.
	•	Initialize the WebDriverWait object to handle dynamic content on the website.

2. Web Scraping:
	•	Make sure the page is in Spanish
    •	Navigate to the Opinion section of the El País website.
	•	Scrape the title, content, and cover image for the first five articles.
	•	Save the cover images to a local folder (article_images).

3. API Integration:
	•	Translate the scraped article titles from Spanish to English using the Google Translate API.
	•	Print the translated headers.

4. Text Processing:
	•	Analyze the translated headers to identify repeated words.
	•	Print the repeated words along with their occurrence counts.

5. Cross-Browser Testing:
	•	Validate the solution locally.
	•	Execute the script on BrowserStack in five parallel threads, testing across desktop and mobile browsers.
	•	Report the session results to BrowserStack.

How to Run the Project
	1.	Local Execution:
	•	Run the script locally to validate functionality:

browserstack-sdk python automate.py

	2.	Cross-Browser Testing on BrowserStack:
	•	Modify the capabilities in the script to include desired browser and device configurations.
	•	Run the script using BrowserStack:

	3.	Saving Results:
	•	The scraped article details will be saved in a structured format.
	•	Cover images will be stored in the article_images folder.

Output
	•	Web Scraping:
	    •	Titles, content, and images (if available) of the first five articles in Spanish.
	•	API Integration:
	    •	Translated headers of the articles in English.
	•	Text Processing:
        •   Repeated words in the translated headers along with their counts.
	•	Cross-Browser Testing:
        •	Results of the test execution across different browser and device combinations, viewable in the BrowserStack dashboard.

Example Results

Spanish Titles:
	1.	El impacto del cambio climático en las economías locales
	2.	La tecnología como motor de cambio en la sociedad

Translated Titles:
	1.	The impact of climate change on local economies
	2.	Technology as a driver of change in society

Repeated Words:
	•	“of”: 3 occurrences
	•	“change”: 4 occurrences

Folder Structure

├── article_images/            # Folder for saving article cover images
├── automate.py                # Main script for running tests on BrowserStack
├── requirements.txt           # List of Python dependencies
├── README.md                  # Documentation
├── browserstack.yml           # browserstack-sdk congigurations
├── automate.exe               # executable file

Feel free to reach out for questions or feedback! Happy testing! 😊