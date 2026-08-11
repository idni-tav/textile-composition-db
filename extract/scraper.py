from extract.shared.http import get_soup
from extract.shared.links import normalize_links, extract_product_url
from extract.shared.html_extractors import extract_json_block, extract_materials
from extract.sites.aym.parser import build_product_dict
from extract.sites.aym.config import CONFIG

base_url=CONFIG["base_url"]
category_locators=CONFIG["category_locators"]
product_locator=CONFIG["product_locator"]
materials_locator=CONFIG["materials_locator"]

category_links=normalize_links(base_url,category_locators)                              

product_links=[]
for link in category_links:

    soup=get_soup(link)
    raw_urls=extract_product_url(soup,product_locator)[:8]
    normalized_urls=normalize_links(base_url,raw_urls)

    for url in normalized_urls:
        product_links.append(url)
    
    
product_links=list(set(product_links))


products=[]
for link, category_name in product_links:
    product_soup=get_soup(link)
    json_data=extract_json_block(product_soup)
    materials=extract_materials(product_soup,materials_locator)
    product=build_product_dict(json_data,materials)
    products.append(product)
  












###############################################
#product_links=[]
#for link in category_links:

#    soup=get_soup(link)
#    raw_urls=extract_product_url(soup,product_locator)[:8]
#    normalized_urls=normalize_links(base_url,raw_urls)
#    product_links.extend(normalized_urls)
    
    
#product_links=list(set(product_links))


#products=[]
#for link in product_links:
#    product_soup=get_soup(link)
#    json_data=extract_json_block(product_soup)
#    materials=extract_materials(product_soup,materials_locator)
#    product=build_product_dict(json_data,materials)
#    products.append(product)
  


