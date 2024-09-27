# Google Maps Business Data Scraper

This project is a Python-based web scraper that extracts business data from Google Maps using Selenium and BeautifulSoup. The scraped data is then stored in a CSV file for easy access and further analysis.

## Features

- **Automated Scraping**: Uses Selenium to automate browsing through Google Maps.
- **Data Extraction**: Extracts business details such as business name, address, timings, contact information.
- **BeautifulSoup Integration**: Utilizes BeautifulSoup for parsing and extracting HTML content.
- **CSV Output**: Stores the scraped data in a structured CSV file.
- **Error Handling**: Built-in error handling to manage timeouts and missing data fields.

## Requirements

- Python 3.10 +
- Google Chrome (compatible version)

### Python Packages:

You can install all the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

Here are the key dependencies:
- `selenium`
- `beautifulsoup4`
- `pandas` (for CSV export)

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Tapendrakaul/Google-Maps-Business-Data-Scraper.git
   cd Google-Maps-Business-Data-Scraper
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scraper**:

   To run the scraper, execute the following command:

   ```bash
   python google_map_scrapper.py
   ```

   The scraped data will be saved into a `data.csv` file in the same directory.

## Usage

This script automates the collection of business information by entering specific locations and keywords into Google Maps, and retrieving relevant data fields such as:

- Business Name
- Address
- Phone Number
- Website
- Timings


## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Tapendrakaul/Google-Maps-Business-Data-Scraper.git) if you have any questions or suggestions.
