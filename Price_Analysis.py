import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Adding headers to mimic a real browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

destination = input("Enter the specific destination at the location: ")
check_in = input("Enter the check-in date (YYYY-MM-DD): ")
check_out = input("Enter the check-out date (YYYY-MM-DD): ")


# URL of the search results page
url = f'https://www.booking.com/searchresults.en-gb.html?ss={destination}&checkin={check_in}&checkout={check_out}&group_adults=2&no_rooms=1&group_children=0&order=class'

hotel_names = []
hotel_prices = []
hotel_reviews = []
hotel_distances = []

# Sending the request to the URL
response = requests.get(url, headers=headers)
web_content = response.content

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')

# Finding the property cards using the data-testid attribute
property_cards = soup.find_all("div", attrs={"data-testid": "property-card"})

# Iterate over each property card and extract details
for card in property_cards:
    # Extract hotel name
    title_tag = card.find("div", attrs={"data-testid": "title"})
    if title_tag:
        title = title_tag.text.strip() 
    else: 
        title = "N/A"
    hotel_names.append(title)

    # Extract hotel price
    price_tag = card.find("span", attrs={"data-testid": "price-and-discounted-price"})
    if price_tag:
        price = price_tag.text.split()[-1]
    else:
        price = "N/A"
    hotel_prices.append(price)

    # Extract hotel review score
    reviews_tag = card.find("div", attrs={"data-testid": "review-score"})
    if reviews_tag:
        reviews = reviews_tag.text.split()[1]
    else:
        reviews = "N/A"
    hotel_reviews.append(reviews)

    # Extract hotel distance
    distance_tag = card.find("span", attrs={"data-testid": "distance"})
    if distance_tag:
        distance = distance_tag.text.split()[0]
    else:
        distance = "N/A"
    hotel_distances.append(distance)


# Creating the DataFrame
df = pd.DataFrame({
    "Hotel": hotel_names,
    "Price": hotel_prices,
    "Ratings": hotel_reviews,
    "Distance": hotel_distances
})

# Display the DataFrame
print(df)

# Replace "N/A" with NaN in 'Price' and 'Ratings' columns
df.loc[df['Price'] == 'N/A', 'Price'] = np.nan
df.loc[df['Ratings'] == 'N/A', 'Ratings'] = np.nan

# Drop rows with NaN values in 'Price' or 'Ratings' columns
df = df.dropna(subset=['Price', 'Ratings'])

# Convert 'Price' column to numeric (assuming it contains strings with currency symbols)
df['Price'] = pd.to_numeric(df['Price'].str.replace(',', ''), errors='coerce')

# Convert 'Ratings' column to numeric (assuming it contains strings with ratings)
df['Ratings'] = pd.to_numeric(df['Ratings'], errors='coerce')

# Convert 'Distance' column to numeric (assuming it contains strings with ratings)
df['Distance'] = pd.to_numeric(df['Distance'], errors='coerce')

# Sort hotels by Price, Ratings, and Distance
df_sorted = df.sort_values(by=['Distance'], ascending=[True])

# Select top 10 hotels with least Price, highest Ratings, and closest Distance
top_hotels = df_sorted.head(10)

# Create a bar chart for top hotels
plt.figure(figsize=(12, 8))

# Bar chart for Prices
plt.bar(top_hotels['Hotel'], top_hotels['Price'], color='b', alpha=0.7, label='Price')
plt.xlabel('Hotel Names')
plt.ylabel('Price (in INR)')
plt.title('Top 10 Hotels:')
plt.xticks(rotation=45, ha='right')

# Line plot for Ratings (on secondary y-axis)
ax2 = plt.twinx()
ax2.plot(top_hotels['Hotel'], top_hotels['Ratings'], color='g', marker='o', linestyle='-', linewidth=2, label='Ratings')
ax2.set_ylabel('Ratings')
ax2.tick_params(axis='y')

# Create a bar chart for hotel distances
plt.figure(figsize=(12, 8))

plt.bar(top_hotels['Hotel'], top_hotels['Distance'], color='b', alpha=0.7, label='Distance')
plt.xlabel('Hotel Names')
plt.ylabel('Distance (km)')
plt.title('Top 10 Hotels Closest to Destination')
plt.xticks(rotation=45, ha='right')

plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
