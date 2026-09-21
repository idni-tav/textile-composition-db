def build_product_dict(json_data,materials):

    offers=json_data["offers"]

    if isinstance(offers, list):
        offer=offers[0]
    else:
        offer=offers
    print(offer)

    return {
        'brand': (json_data.get("brand") or {}).get("name"),
        #'category':parent_category,
        'sub_category': None,
        'product_name': json_data["name"],
        'price': offer["price"],
        'currency': offer["priceCurrency"],
        'product_url': offer["url"],
        'materials_raw': materials
    }

 
    

