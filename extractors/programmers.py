from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)

base_url = "https://career.programmers.co.kr/job?tags="
search = "Python"
browser.get(f"{base_url}{search}")

soup = BeautifulSoup(browser.page_source, "html.parser")
pagination = soup.find("ul", class_="pagination")
pages = pagination.find_all("li", recursive=False)
print(pages)
