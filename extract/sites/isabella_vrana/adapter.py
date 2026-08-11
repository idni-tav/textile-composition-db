
def build_product_dict(json_data, materials):

    variants=json_data.get("hasVariant") or []
    variant=variants[0] if len(variants) > 0 else {}

    offer=variant.get("offers") or {}

    return {
        'brand': (json_data.get("brand") or {}).get("name"),
        #'category': parent_category,
        'sub_category': json_data.get("category"),
        'product_name': json_data.get("name"),
        'price': offer.get("price"),
        'currency': offer.get("priceCurrency"),
        'product_url': offer.get("url"),
        'materials_raw': materials
    }


