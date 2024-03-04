# zSpider

zSpider is a Python script designed for web crawling and searching for specific text (flags) on webpages within a given domain. The script uses `requests` for HTTP requests, `BeautifulSoup` for HTML parsing, and `colorama` for colored console output.

## Features

- **Web Crawling**: Recursively visits all pages within the specified domain starting from a given URL.
- **Text Search**: Searches for specified text (flags) on each visited page.
- **Colored Console Output**: Differentiates informational messages, warnings, and errors with colors:
  - Green: Success messages
  - Yellow: Warnings
  - Red: Errors
- **Link Validation**: Follows only the links that belong to the base domain to prevent navigating away from the target site.

## Requirements

The script requires Python 3 and these packages:
- `requests`
- `BeautifulSoup` (from `bs4`)
- `colorama`

Install dependencies with pip:
```bash
pip install requests beautifulsoup4 colorama
```
## Usage

To use this web crawler script, follow the steps below:

1. **Launch the Script**: 
   Open your terminal or command prompt, navigate to the directory containing the script, and execute it with Python by running:
	  ```sh
   python zSpider.py
	```
2.	**Enter Required Input:**
	After execution, the script will prompt you for two inputs:

	-   **Starting URL**: Enter the URL where the crawler should start its journey. This URL should be the entry point to the domain you wish to crawl.
	-   **Flag to Search For**: Enter the specific text or "**flag**" that you're looking for within the web pages. If you press Enter without specifying a flag, the script defaults to searching for "flag".

## Function Descriptions

Below are brief descriptions of the key functions within the script:

-   `print_info(msg)`: Displays informational messages in green, indicating successful operations or findings.
-   `print_error(msg)`: Shows error messages in red, alerting you to any issues that occurred during the crawling process.
-   `print_warning(msg)`: Outputs warnings in yellow, used for non-critical issues or notices.
-   `find_and_print_flags(url)`: Attempts to find the specified flag in the text of a web page fetched from the given URL.
-   `is_valid_url(url, base_domain)`: Checks if a URL belongs to the same domain as the base domain, ensuring the crawler doesn't venture outside the target website.
-   `crawl(url, base_domain, visited=set())`: The core function that recursively visits and processes web pages, starting from the given URL and exploring all valid links within the base domain.

## Important Notes

-   This script is designed for educational and **ethical use**, mainly for **CTF**. Always ensure you have permission to crawl and scrape content from websites.
-   The effectiveness and efficiency of the script can vary based on the structure of the target website and the network's performance. Adjustments may be necessary for optimal use.

By adhering to this guide and understanding the functionalities provided by the script, users can effectively employ and adapt it for their specific web crawling and content searching objectives.
