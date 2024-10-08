# **Hotel Price and Distance Analyzer**

A Python-based tool that scrapes hotel data, including price, ratings, and distance to a specified destination, using **BeautifulSoup**, **Pandas**, and **Matplotlib**. It provides an analysis of the top 10 hotels closest to the destination with visual representations of prices and ratings.

---

## **Contents**
- [About](#about)
- [Setup](#setup)
- [Usage](#usage)
- [Visualization Guide](#visualization-guide)

---

## **About**

This project is a web scraper and analysis tool for hotel search results from **Booking.com**. It extracts hotel names, prices, ratings, and distances for a specified location and check-in/check-out dates. The data is processed to generate visual insights, helping users compare the top 10 hotels based on price, ratings, and proximity to the destination.

### **Features:**
- Scrapes hotel details: price, ratings, distance, and names.
- Filters top hotels based on proximity.
- Visualizes hotel prices, ratings, and distances using bar and line charts.
- Provides an easy-to-use command-line interface to input destination and dates.

---

## **Setup**
Install dependencies:

Make sure you have Python installed on your machine. Install the required libraries by running:

bash
Copy code
$ pip install -r install_requires.txt
The required libraries include:

requests
beautifulsoup4
pandas
numpy
matplotlib
Run the main script:

bash
Copy code
$ python main.py
Usage
Once you have the project set up, follow the instructions below to run the tool:

Input destination and dates:

You will be prompted to enter the destination and check-in/check-out dates in the following format:

Destination (e.g., "Mumbai")
Check-in date (e.g., "2024-10-10")
Check-out date (e.g., "2024-10-15")
Data extraction and analysis:

The tool will fetch hotel details for your destination and create a dataframe with columns for hotel names, prices, ratings, and distances.

Visualizations:

The program will generate:

A bar chart showing the prices of the top 10 hotels.
A line plot for ratings on the same graph as prices.
A second bar chart for the distances of the top 10 hotels.
Visualization Guide
Here are the visualizations created from the data:

Price and Ratings Chart:


Blue bars represent hotel prices.
Green line represents hotel ratings.
Distance Chart:


Blue bars represent the distances of hotels from the destination.
Improvements & Future Work
Distance Improvements: Current distance data relies on proximity to the destination. Future updates will include more refined location-based sorting and filtering.
Additional Filtering: The project could be expanded to allow filters based on price range or user ratings.
Acknowledgements
BeautifulSoup: For providing an excellent tool to scrape HTML content.
Matplotlib: For creating intuitive visualizations.
Pandas: For powerful data manipulation.


Follow the steps below to set up and run the project:

1. **Clone this repository:**

   ```bash
   $ git clone https://github.com/imavisingh03/Hotel-Price-Distance-Analyzer.git
