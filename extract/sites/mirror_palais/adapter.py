def build_product_dict(json_data, materials):

    variant=json_data["hasVariant"][0]
    offer=variant["offers"]

    return {
        'brand': (json_data.get("brand") or {}).get("name"),
        'sub_category': json_data.get("category"),
        'product_name': json_data["name"],
        'price': offer["price"],
        'currency': offer["priceCurrency"],
        'product_url': offer["url"],
        'materials_raw': materials
    }