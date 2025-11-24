---
slug: github-project-web-scraping
title: Automated Real Estate Data Scraping and Management with Google Integration
repo: justin-napolitano/project-web-scraping
githubUrl: https://github.com/justin-napolitano/project-web-scraping
generatedAt: '2025-11-23T09:26:29.070337Z'
source: github-auto
summary: >-
  Technical overview of a modular, YAML-configured pipeline for scraping, processing, and managing
  real estate data with Google Sheets and Drive integration.
tags:
  - web-scraping
  - real-estate-data
  - google-sheets
  - google-drive
  - data-processing
seoPrimaryKeyword: real estate data scraping
seoSecondaryKeywords:
  - google sheets integration
  - web scraping pipeline
  - data cleaning
  - data merging
seoOptimized: true
---

# project-web-scraping: Technical Overview and Implementation Notes

## Motivation and Problem Statement

This project addresses the need for an automated, configurable pipeline to scrape, process, and manage real estate data from online sources. Real estate data is often scattered across multiple platforms and formats, making manual collection inefficient and error-prone. The project consolidates scraping from realtor.com and rew.ca, integrates with Google Sheets and Drive for storage and collaboration, and provides utilities for cleaning, filtering, and merging datasets.

## Architecture and Components

The application is structured around a YAML-driven configuration that defines tasks, directories, and file parameters. The `main.py` serves as the entry point, loading configurations and invoking the `program_skeleton.py` module which orchestrates the workflow.

### Credential Management

Google API credentials are managed in `get_creds.py`, which handles loading and refreshing tokens for Sheets and Drive API access. This is critical for authenticated interactions with Google services.

### Data Acquisition

- **Scraping Modules:** `realtor_scraper_sheets_4.py`, `rew_scraper.py`, and `rew_scraper3.py` handle scraping of real estate data. They use `requests` and `BeautifulSoup` to parse HTML content, extracting agent and listing information.
- **Batch Download:** `batch_download.py` and parts of `goog_sheets.py` manage batch retrieval of data from Google Sheets, enabling efficient data extraction from large spreadsheets.

### Data Processing

- **Cleaning:** `clean_df.py` contains functions to drop irrelevant columns and create new columns based on extracted data.
- **Filtering:** `df_filter.py` implements filtering logic based on listing counts and approximate values, although some parts are obsolete.
- **Merging:** `merge.py` provides batch merging of CSV files to consolidate data.
- **File Handling:** `fix_files.py` corrects file naming inconsistencies to maintain orderly datasets.

### Data Storage and Export

- `readwrite.py` offers utilities to export dataframes as CSV or JSON files, and to list files in directories.
- Google Drive integration (`google_drive.py`) supports folder creation and file management for organizing data.

### Logging and Maintenance

- `log.py` includes a garbage collector wrapper and functions to dump logs and JSON data.
- `confirm_drcts.py` ensures necessary directories exist before operations proceed.

## Implementation Details and Observations

- The project relies heavily on a centralized dictionary loaded from YAML configs, which is passed through functions to maintain state and configuration.
- Scrapers use specific user-agent headers to mimic browsers and avoid blocking.
- Some modules and functions appear to be works in progress or partially obsolete, indicating ongoing development.
- The use of Google Sheets and Drive APIs suggests a workflow that integrates scraping with collaborative data management.
- The code shows a preference for modularity, separating concerns like scraping, cleaning, merging, and exporting.
- Error handling is minimal in many places; future improvements could include robust exception management.
- Logging is basic and could be enhanced for better traceability.

## Practical Considerations

When returning to this project, focus first on:

- Reviewing and updating the configuration files to match current directory structures and credentials.
- Verifying Google API credentials and token validity.
- Testing individual scraping modules independently to ensure they still work against target websites.
- Cleaning up obsolete or incomplete code sections.
- Enhancing logging and error handling to facilitate debugging.

Understanding the flow from configuration loading, credential setup, scraping, data cleaning, merging, and exporting will be key to maintaining and extending this project.

## Conclusion

This project provides a foundation for automated real estate data scraping and management with integration into Google services. While functional, it requires refinement and modernization to improve robustness, maintainability, and extensibility. The modular design and configuration-driven approach offer flexibility for future enhancements and adaptation to new data sources.
