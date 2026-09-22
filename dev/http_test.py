
from extract.shared.http import get_soup

soup = get_soup("https://www.peachyden.co.uk")
print(soup.title)