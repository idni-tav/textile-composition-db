def build_product_dict(json_data,materials):

    return {
        'brand': (json_data.get("brand") or {}).get("name"),
        #'category':parent_category,
        'sub_category': None,
        'product_name': json_data["name"],
        'price': json_data["offers"][0]["price"],
        'currency': json_data["offers"][0]["priceCurrency"],
        'product_url': json_data["offers"][0]["url"],
        'materials_raw': materials
    }




