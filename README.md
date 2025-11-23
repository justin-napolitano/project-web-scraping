# project-web-scraping

General purpose webscraping application designed to extract, clean, and manage real estate and related data from various online sources including Google Sheets and realtor websites.

---

## Features

- Scrapes real estate agent and listing data from realtor.com and rew.ca.
- Integrates with Google Sheets and Google Drive APIs for data storage and management.
- Batch downloads and merges data from multiple sources.
- Cleans and filters scraped data for further analysis.
- Supports exporting data in CSV and JSON formats.
- Configurable via YAML files.

---

## Tech Stack

- Python 3
- Libraries: BeautifulSoup, requests, pandas, google-api-python-client, google-auth, PyYAML
- Google Sheets and Drive APIs

---

## Getting Started

### Prerequisites

- Python 3.6+
- Google API credentials (`credentials.json` and `token.json`) for Sheets and Drive access.

### Installation

```bash
git clone https://github.com/justin-napolitano/project-web-scraping.git
cd project-web-scraping
pip install -r requirements.txt  # Assumed requirements file
```

### Configuration

- Edit `config.yaml` to set directories, file names, and task flags.
- Place Google API credentials in the project root.

### Running

```bash
python main.py
```

This will load the configuration, initialize services, and run the scraping and data processing pipeline.

---

## Project Structure

- `main.py`: Entry point of the application.
- `program_skeleton.py`: Core workflow orchestrator managing tasks.
- `load_vars.py`: Loads and sets environmental variables and config.
- `get_creds.py`: Handles Google API credential loading.
- `goog_sheets.py`: Google Sheets API interactions.
- `google_drive.py`: Google Drive API interactions.
- `batch_download.py`: Batch download logic for Google Sheets data.
- `readwrite.py`: Utilities for reading and writing data files.
- `clean_df.py`: Data cleaning functions.
- `df_filter.py`: Data filtering logic (partially obsolete).
- `merge.py`: Functions to merge CSV data files.
- `download.py`: Downloads PDFs from URLs.
- `fix_files.py`: Fixes file naming inconsistencies.
- `confirm_drcts.py`: Ensures folder structure exists.
- `log.py`: Logging and garbage collection utilities.
- `rew_scraper.py` and `rew_scraper3.py`: Scrapers for rew.ca.
- `realtor_scraper_sheets_4.py`: Scraper for realtor.com integrated with Google Sheets.

---

## Future Work / Roadmap

- Refactor and unify scraping modules for better maintainability.
- Improve error handling and logging across all modules.
- Automate credential refresh and token management.
- Enhance configuration flexibility to support more data sources.
- Implement more robust data validation and deduplication.
- Add unit and integration tests.
- Document all functions and classes with detailed docstrings.

---

*Note: Some modules and functions are partially implemented or marked as obsolete and may require cleanup or rework.*