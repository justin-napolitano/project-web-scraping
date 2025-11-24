---
slug: github-project-web-scraping-writing-overview
id: github-project-web-scraping-writing-overview
title: 'Web Scraping Simplified: My Journey with project-web-scraping'
repo: justin-napolitano/project-web-scraping
githubUrl: https://github.com/justin-napolitano/project-web-scraping
generatedAt: '2025-11-24T17:49:49.707Z'
source: github-auto
summary: >-
  I've always been fascinated by data, especially when it comes from the web.
  That's why I created **project-web-scraping**—a general-purpose web scraping
  application. It extracts, cleans, and manages real estate data from various
  online sources. You can check it out here: [project-web-scraping on
  GitHub](https://github.com/justin-napolitano/project-web-scraping).
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: writing
entryLayout: writing
showInProjects: false
showInNotes: false
showInWriting: true
showInLogs: false
---

I've always been fascinated by data, especially when it comes from the web. That's why I created **project-web-scraping**—a general-purpose web scraping application. It extracts, cleans, and manages real estate data from various online sources. You can check it out here: [project-web-scraping on GitHub](https://github.com/justin-napolitano/project-web-scraping).

## Why This Project?

The real estate market is a sea of information. From agent listings on realtor.com to property details on rew.ca, I saw a chance to harness that data for analysis. My goal was simple: build a tool that can gather relevant information efficiently while integrating with Google Sheets for seamless data management.

## What It Does

In essence, the project accomplishes a few key tasks:

- **Data Extraction**: Scrapes real estate listings and agent details from specified sites.
- **Integration**: Uses Google Sheets and Drive APIs for data storage and management, making it super easy to access your info later.
- **Data Cleaning**: Filters out the noise and presents clean data ready for analysis.
- **Export Capabilities**: Outputs your scraped data in CSV and JSON formats.
- **Flexible Configuration**: Adjust settings via YAML files, making it easy to tweak as needed.

## Key Design Decisions

I wanted to keep things straightforward. This isn't just a scrappy web scraper; it’s designed with a couple of principles in mind:

- **Modularity**: The project structure reflects various functionalities. Each core task has its dedicated module. This decoupling helps with maintenance and allows for focused updates.
  
- **Ease of Use**: I used YAML for configuration, which is readable and allows users to customize the setup without digging into code.

- **Batch Processing**: I embraced batch downloads, which lets me merge data from multiple sources in one go. No one wants to individually scrape the same type of data from multiple websites.

## Tech Stack

The backbone of the project is primarily built with Python 3. I used several libraries and APIs that I found robust and reliable:

- **BeautifulSoup**: For parsing HTML and navigating through the document tree.
- **requests**: To handle HTTP requests with ease.
- **pandas**: To manage data operations efficiently.
- **Google API** libraries: For interaction with Google Sheets and Drive.
- **PyYAML**: To handle configuration files without a hassle.

## Trade-offs Made

Every project comes with its fair share of trade-offs. Here are a few I encountered:

- **Simplicity vs. Feature-richness**: I chose to keep it simple rather than include every possible configuration from the get-go. This was a conscious decision to not overwhelm users.
  
- **Data Duplication**: Some scraping modules may be partially implemented or obsolete, leading to duplicate logic in places. It's something I'm looking to clean up.

- **Error Handling**: While basic error handling is in place, there’s room for improvement. Right now, it’s not as robust as I’d like.

## What I'd Like to Improve Next

This project is a work in progress. Here’s a quick hit list of things I want to tackle soon:

- **Refactoring**: I plan to consolidate the scraping modules. A cleaner structure will make future modifications a breeze.
  
- **Better Logging**: Enhancing logging across the application will help both in debugging and in tracking usage.

- **Automate Credential Management**: I want to automate how credentials are refreshed. Dealing with APIs isn't always straightforward, and this should ease the pain.

- **Enhanced Validation**: Better data checks pre- and post-scraping are a must. It’s important to ensure the quality and integrity of the data.
  
- **Testing**: I want to write unit and integration tests. This will help me ensure that changes do not break existing functionality.

- **Documentation**: Finally, I aim to document all functions and classes thoroughly. Clear documentation is crucial, especially for open-source projects.

## Come Join Me

If you're interested in web scraping or gathering real estate data, this might be the tool you’re looking for. I’m continuously improving it, and I love feedback from fellow developers. You can catch updates on my progress on social media—I'm active on Mastodon, Bluesky, and Twitter/X. 

Happy scrapping!
