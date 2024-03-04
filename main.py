import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
init(autoreset=True)
from urllib.parse import urljoin, urlparse
reset = Style.RESET_ALL

def print_info(msg):
  print("[" + Fore.GREEN + "+" + reset + "] " + msg)

def print_error(msg):
  print("[" + Fore.RED + "-" + reset + "] " + msg)

def print_warning(msg):
  print("[" + Fore.YELLOW + "!" + reset + "] " + msg)

def find_and_print_flags(url):
  try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    testo = soup.get_text()
    print_warning(f"Analyzing {url}")
    if search in testo.lower():
      print_info(f"Flag found in {url}: {testo}")
      exit()
  except requests.RequestException as e:
    print_error(f"Error during the connection on {url}: {e}")
    return

def is_valid_url(url, base_domain):
  parsed_url = urlparse(url)
  return bool(parsed_url.netloc) and parsed_url.netloc == base_domain

def crawl(url, base_domain, visited=set()):
  if url in visited:
    return
  visited.add(url)
  find_and_print_flags(url)
  try:
    response = requests.get(url)
    response.raise_for_status()
  except requests.RequestException as e:
    print_error(f"Error during request on {url}: {e}")
    return
  soup = BeautifulSoup(response.text, 'html.parser')
  links = [link.get('href') for link in soup.find_all('a', href=True)]
  for link in links:
    full_link = urljoin(url, link)
    if is_valid_url(full_link, base_domain):
      crawl(full_link, base_domain, visited)

start_url = input("Enter the starting URL: ")
search = input("Enter the flag to search for: (default is 'flag') ")
if search == "":
  search = "flag"
print("[+] Searching for", search, " in ", start_url)
parsed_url = urlparse(start_url)
base_domain = parsed_url.netloc


crawl(start_url, base_domain)
print_warning("Ending...")