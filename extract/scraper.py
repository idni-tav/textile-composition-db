from extract.shared.http import get_soup
from extract.shared.links import normalize_links, extract_product_url
from extract.shared.html_extractors import extract_json_block, extract_materials
#from extract.sites.isabella_vrana.adapter import build_product_dict
#from extract.sites.isabella_vrana.config import CONFIG

def run_extraction(config,adapter,garment_per_category):

    base_url=config["base_url"]
    category_locators=config["category_locators"]
    product_locator=config["product_locator"]
    materials_locator=config["materials_locator"]
    json_ld_type=config["json_ld_type"]

    category_links=normalize_links(base_url,category_locators)                              

    product_links=[]
    for category_link in category_links:

        soup=get_soup(category_link)
        raw_urls=extract_product_url(soup,product_locator)[:garment_per_category]
        normalized_urls=normalize_links(base_url,raw_urls)
        category=category_link.rstrip("/").split("/")[-1]


        for url in normalized_urls:
            product_links.append((url,category))
    
    
    product_links=list(set(product_links))

    products=[]
    for link, category in product_links:
        product_soup=get_soup(link)
        json_data=extract_json_block(product_soup,json_ld_type)
        materials=extract_materials(product_soup,materials_locator)
        product=adapter(json_data,materials)
        product["category"]=category
        products.append(product)


    return products





















