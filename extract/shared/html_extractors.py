import json


def extract_json_block(soup,json_ld_type):

    scripts=soup.find_all("script", type="application/ld+json")

    for script in scripts:
        data=json.loads(script.string)

        #case 1: data is a list
        if isinstance(data, list):
            for item in data:
                if item.get("@type")==json_ld_type:
                    return item

        #case 2: data is a dict
        else:
            if data.get("@type")==json_ld_type:
                return data

    return None

def extract_materials(soup, materials_locator):

    tag=materials_locator.get("tag")
    class_name=materials_locator.get("class")

    blocks=soup.find_all(tag, class_=class_name)

    #safety check
    if not blocks:
        return None

    
    best_text=None
    max_percent_count=0

    
    for block in blocks:

        texts=[]

        for node in block.descendants:
            if node.name in ["script", "style"]:
                continue

            if node.string:
                txt=node.string.strip()
                if txt:
                    texts.append(txt)

        if not texts:
            continue

        full_text="\n".join(texts)

        percent_count=full_text.count("%")

        if percent_count>max_percent_count:
            max_percent_count=percent_count
            best_text=full_text

    return best_text



















def extract_materials_with_fabric_count(soup, materials_locator):

    tag=materials_locator.get("tag")
    class_name=materials_locator.get("class")

    blocks=soup.find_all(tag, class_=class_name)

    #safety check
    if not blocks:
        return None

    
    best_text=None
    max_score=0

    
    for block in blocks:

        texts=[]

        for node in block.descendants:
            if node.name in ["script", "style"]:
                continue

            if node.string:
                txt=node.string.strip()
                if txt:
                    texts.append(txt)

        if not texts:
            continue

        full_text="\n".join(texts)

        percent_count=full_text.count("%")
        fabric_count=full_text.lower().count("fabric")

        score=percent_count + fabric_count

        if score>max_score:
            max_score=score
            best_text=full_text

    return best_text











    










        









def extract_json_block_previous(soup):
    
    
    #script_tag=soup.find("script", type="application/ld+json")
    #json_data=json.loads(script_tag.string)   #convert it to Python dict
    
    script_tag=soup.find("script", type="application/ld+json")
    

    #lol chatgpt told me to do this to avoid errors
    if not script_tag or not script_tag.string:
        return None

    try:
        return json.loads(script_tag.string)
    except json.JSONDecodeError:
        return None





def extract_json_block_2(soup):

    scripts = soup.find_all("script", type="application/ld+json")

    for script in scripts:
        if not script.string:
            continue

        try:
            data = json.loads(script.string)
        except json.JSONDecodeError:
            continue

        # Case 1: list of schemas
        if isinstance(data, list):
            for item in data:
                if item.get("@type") in ["Product", "ProductGroup"]:
                    return item

        # Case 2: single schema
        elif data.get("@type") in ["Product", "ProductGroup"]:
            return data

    return None



def extract_json_block_3(soup):

    scripts=soup.find_all("script", type="application/ld+json")

    for script in scripts:
        data=json.loads(script.string)

        if data.get("@type") == "Product":
            return data

    return None



def extract_materials_unit(soup, materials_locator):

    tag = materials_locator.get("tag")
    class_name = materials_locator.get("class")
    block = soup.find(class_=class_name)

    if not block:
        return None

    texts = []

    for el in block.descendants:
        if el.name in ["script", "style"]:
            continue

        if el.string:
            txt = el.string.strip()
            if txt:
                texts.append(txt)

    return "\n".join(texts) if texts else None



def extract_materials_second_layer(soup, materials_locator):

    tag = materials_locator.get("tag")
    class_name = materials_locator.get("class")

    blocks = soup.find_all(tag, class_=class_name)

    if not blocks:
        return None

    all_blocks_text = []

    for block in blocks:

        texts = []

        for el in block.descendants:
            if el.name in ["script", "style"]:
                continue

            if el.string:
                txt = el.string.strip()
                if txt:
                    texts.append(txt)

        if texts:
            all_blocks_text.append("\n".join(texts))

    return all_blocks_text if all_blocks_text else None


def extract_materials_1(soup, materials_locator):

    tag = materials_locator.get("tag")
    class_name = materials_locator.get("class")

    block = soup.find(tag, class_=class_name)

    if not block:
        return None

    text = block.get_text(separator="\n", strip=True)

    return text if text else None
