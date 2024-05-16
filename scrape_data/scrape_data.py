import pandas as pd
from bs4 import BeautifulSoup
import requests
def scrape():
    url = "https://en.wikipedia.org/wiki/List_of_brightest_stars"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table with class 'wikitable'
    table = soup.find('table', {'class': 'wikitable'})
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    scraped_data = []
    
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        if len(cols) >= 5:  # Ensure there are enough columns
            scraped_data.append(cols[:5])  # Keep only the first 5 columns

    return scraped_data
if __name__ == "__main__":
    data = scrape()
    
    # Define the columns
    columns = ["Star Name", "Distance", "Mass", "Radius", "Luminosity"]

    # Create a DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Save to CSV
    df.to_csv('brightest_stars.csv', index=False)

    print("Data saved to brightest_stars.csv")
