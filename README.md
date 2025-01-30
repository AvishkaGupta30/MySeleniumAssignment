# Selenium Table Search Demo Automation
This project demonstrates the use of Selenium WebDriver to automate the process of searching and validating results on a web page. The script interacts with a table on the "Selenium Table Search Demo" website to search for specific entries and validate the number of results displayed.

# Table of Contents
Description
Installation
Usage
Expected Output
Contributing
License

# Description
This automation script is designed to search for "New York" on the Selenium Table Search Demo page, validate that 5 search results appear out of 24 total entries, and then print a result summary. This approach is useful for testing the search functionality and the handling of dynamic data in a table.
The script uses Selenium WebDriver for web automation and interacts with the HTML table to retrieve and validate the displayed entries.


# Installation
Requirements:
Python 3.x
Selenium
ChromeDriver (compatible with your version of Google Chrome)

# Steps to Install:
Clone the Repository: git clone https://github.com/YourUsername/YourRepo.git
Install Selenium: If you haven’t already, install Selenium using pip: pip install selenium
Download ChromeDriver: https://developer.chrome.com/docs/chromedriver/downloads#chromedriver_1140573590
Make sure to download the version that matches your installed version of Google Chrome.
Extract and note the path to the chromedriver.exe file.
Set up ChromeDriver Path: Ensure the chromedriver.exe is accessible from your script, either by placing it in the same directory as the script or by specifying its path in the script.

# Usage
Run the Script: After installing the dependencies and setting up ChromeDriver, you can run the Python script with the following command: python3 Selenium.py

# Script Overview:
The script opens the website (https://www.lambdatest.com/selenium-playground/table-sort-search-demo).
It enters the search term “New York” in the search box.
It validates that exactly 5 results are displayed out of 24 total entries.
The result of the validation is printed in the console.

# Expected Output
Total entries found: (Displays the number of rows found in the table after the search)
Test passed or failed: Based on the validation that 5 entries are found.

# Additional Setup Instructions
1. Setting up Local Environment
If you're setting up the environment on a fresh system, here are the basic steps to get everything up and running.

# Install Python:
Ensure you have Python 3.x installed on your system. If not, download and install it from Python's official website.

# Install Dependencies
You need to install Selenium and any other required dependencies. To do this, run the following command in the terminal (ensure your virtual environment is activated, if using one):
pip install selenium

