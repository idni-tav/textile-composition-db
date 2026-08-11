def build_product_dict(json_data,materials):

    return {
        'brand': json_data["brand"]["name"],
        #'category':parent_category,
        'sub_category': json_data["category"],
        'product_name': json_data["name"],
        'price': json_data["hasVariant"][0]["offers"]["price"],
        'currency': json_data["hasVariant"][0]["offers"]["priceCurrency"],
        'product_url': json_data["hasVariant"][0]["offers"]["url"],
        'materials_raw': materials
    }

