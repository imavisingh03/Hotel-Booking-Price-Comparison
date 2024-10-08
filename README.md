# Hotel Price Analysis

This project scrapes hotel data such as prices, ratings, and distances for a specific destination, and visualizes the data using charts. It helps users make informed decisions when booking hotels by presenting key data in an easily understandable format.

## Contents
- About
- Setup
- Usage
- Visualization Guide
- Improvements & Future Work
- Acknowledgments

## About

The **Hotel Price Analysis** tool is designed to fetch hotel details for a given destination and display them in a structured format, enabling easy comparison of hotel prices, ratings, and proximity to the chosen location. The goal is to enhance the user’s ability to choose the best hotel based on their preferences.

The tool scrapes data using `BeautifulSoup` and organizes it into a `pandas` dataframe, which can then be visualized using `matplotlib` charts.

## Setup

To get started, follow these steps:

1. **Install Dependencies**: Ensure you have Python installed, then run the following command to install the required libraries:

    ```bash
    pip install -r install_requires.txt
    ```

   The required libraries include:
   - `requests`
   - `beautifulsoup4`
   - `pandas`
   - `numpy`
   - `matplotlib`

2. **Run the Application**: After installing the dependencies, execute the main program:

    ```bash
    Price_Analysis.py
    ```

## Usage

Once the program is running, follow these steps to perform a hotel price analysis:

1. **Input Destination and Dates**:
    - You will be prompted to enter the following:
      - **Destination** (e.g., "Mumbai")
      - **Check-in date** (e.g., "2024-10-10")
      - **Check-out date** (e.g., "2024-10-15")

2. **Data Extraction**:
    - The tool will scrape hotel details for your destination and create a dataframe with the following columns:
      - Hotel names
      - Prices
      - Ratings
      - Distances from the destination

3. **Data Visualization**:
    - After extracting the data, the tool generates visualizations for easy analysis. The charts show prices, ratings, and distances from the destination center.

## Visualization Guide

The tool provides the following visualizations based on the extracted data:

1. **Price and Ratings Chart**:
    - **Blue bars** represent hotel prices.
    - **Green line** represents hotel ratings.

2. **Distance Chart**:
    - **Blue bars** represent the distances of hotels from the destination center.

These visualizations provide a clear comparison between hotel prices, ratings, and distances, helping users make informed decisions.

## Improvements & Future Work

1. **Distance Improvements**:  
   The current distance data relies on proximity to the destination center. Future updates will include more refined location-based sorting and filtering, such as considering nearby landmarks.

2. **Additional Filters**:  
   Future versions could include the option to filter hotels based on price range, user ratings, or hotel amenities.

## Acknowledgments

- **BeautifulSoup**: For providing a robust tool to scrape HTML content.
- **Matplotlib**: For enabling intuitive visualizations.
- **Pandas**: For its powerful data manipulation capabilities, making it easy to work with large datasets.

