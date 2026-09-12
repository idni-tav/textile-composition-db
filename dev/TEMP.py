import requests
from bs4 import BeautifulSoup
import json



def get_soup(url):

    headers={"User-Agent": "Mozilla/5.0"} #to prevent me being blocked

    response=requests.get(url,headers=headers)  #send HTTP request
    html=response.text   #store the server's reply 
    response.raise_for_status()
    soup=BeautifulSoup(html, "html.parser")
   
    return soup

def extract_json_block(soup):
    
    
    script_tag=soup.find("script", type="application/ld+json")
    json_data=json.loads(script_tag.string)   #convert it to Python dict

    return json_data



def extract_materials(soup,materials_locator):

    material_blocks=soup.find_all("span",class_=materials_locator)
    
    for block in material_blocks:
        text=block.get_text(separator=" ", strip=True)
        if "%" in text:
            materials_raw=text
            return materials_raw
            
    return None




def normalize_links(base_url,raw_urls): 
    
    full_links=[]
    for url in raw_urls:
        if url.startswith("http"):
            full_links.append(url)
        else:
            full_links.append(base_url + url)


    return list(set(full_links))


def extract_product_url(soup,locator):
    
    nav_links=soup.find_all("a", href=True)
    urls=[]
    for link in nav_links:
        if locator in link['href']:
            urls.append(link['href'])

    return list(set(urls))




def crawler(config):

    category_links=normalize_links(config['base_url'],config['category_locators'])

    all_product_links=[]
    for link in category_links:

        soup=get_soup(link)
        product_urls=extract_product_url(soup,config['product_locator'])[:8]
        product_links=normalize_links(config['base_url'],product_urls)
        
        all_product_links.extend(product_links)


    return all_product_links



def aym_scraper(product_url,materials_locator="metafield-multi_line_text_field"):

    product_soup=get_soup(product_url)
    json_data=extract_json_block(product_soup)
    materials=extract_materials(product_soup,materials_locator)
    
    return {
        'brand':json_data["brand"]["name"],
        'category':json_data["category"],      
        'product_name':json_data["name"] ,       
        'price':json_data["hasVariant"][0]["offers"]["price"],
        'currency':json_data["hasVariant"][0]["offers"]["priceCurrency"],
        'product_url':json_data["hasVariant"][0]["offers"]["url"],
        'materials_raw':materials
        
    }


