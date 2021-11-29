# pip install beautifulsoup4
# pip show beautifulsoup4
# pip install --upgrade beautifulsoup4
# pip uninstall beautifulsoup4
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<br>bad<i>HTML")
print(soup.prettify())