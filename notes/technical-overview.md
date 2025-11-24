---
slug: github-project-web-scraping-note-technical-overview
id: github-project-web-scraping-note-technical-overview
title: Project Web Scraping
repo: justin-napolitano/project-web-scraping
githubUrl: https://github.com/justin-napolitano/project-web-scraping
generatedAt: '2025-11-24T18:43:22.259Z'
source: github-auto
summary: >-
  This repo is a general-purpose web scraping tool for collecting and managing
  real estate data. It pulls information from realtor.com and rew.ca, integrates
  with Google Sheets, and cleans the data for analysis.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

This repo is a general-purpose web scraping tool for collecting and managing real estate data. It pulls information from realtor.com and rew.ca, integrates with Google Sheets, and cleans the data for analysis.

### Key Features
- Scrapes agent and listing data
- Batch downloads from multiple sources
- Exports data in CSV and JSON
- Configurable via YAML files

### Tech Stack
- Python 3
- Libraries: BeautifulSoup, requests, pandas, google-api-python-client
- Google Sheets and Drive APIs

### Getting Started
1. **Clone the repo:**
    ```bash
    git clone https://github.com/justin-napolitano/project-web-scraping.git
    cd project-web-scraping
    pip install -r requirements.txt
    ```
2. **Configuration:**  
   Edit `config.yaml` to set up directories and API credentials.

3. **Run the application:**
    ```bash
    python main.py
    ```

### Gotchas
- Ensure your Google API credentials are in the project root as `credentials.json` and `token.json`.
- Some modules might need fixing as parts are marked obsolete.
