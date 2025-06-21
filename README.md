# Amharic E-commerce Data Extractor

This project is a web scraper designed to extract data from Amharic e-commerce websites.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Amharic-E-commerce-Data-Extractor
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the scraper, execute the `main.py` script:

```bash
python main.py
```

The scraped data will be saved in the `data` directory in both JSON (`output.json`) and CSV (`output.csv`) formats.

## TODO

-   [ ] Implement the scraping logic in `src/scraper.py`.
-   [ ] Configure the target URL in `main.py`.
-   [ ] Add more robust error handling.
-   [ ] Write comprehensive tests.