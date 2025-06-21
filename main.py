from src.scraper import scrape_data
from src.utils import save_to_json, save_to_csv

def main():
    """
    Main function to run the scraper.
    """
    # TODO: Get the target URL from config or command line
    target_url = "https://www.example.com" # Placeholder URL
    
    print(f"Scraping data from: {target_url}")
    scraped_data = scrape_data(target_url)
    
    if scraped_data:
        print(f"Successfully scraped {len(scraped_data)} items.")
        # Define output filenames
        json_filename = 'data/output.json'
        csv_filename = 'data/output.csv'
        
        # Save data to JSON and CSV
        save_to_json(scraped_data, json_filename)
        save_to_csv(scraped_data, csv_filename)
    else:
        print("Failed to scrape data.")

if __name__ == "__main__":
    main() 