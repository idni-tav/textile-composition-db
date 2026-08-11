from urllib.parse import urljoin


def normalize_links(base_url,raw_urls): 
    
    full_links=[]
    for url in raw_urls:

        full_links.append(urljoin(base_url,url))

    return list(set(full_links))



def extract_product_url(soup,locator):
    
    nav_links=soup.find_all("a", href=True)
    urls=[]
    for link in nav_links:
        if locator in link['href']:
            urls.append(link['href'])

    return list(set(urls))
