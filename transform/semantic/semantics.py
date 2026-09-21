
from transform.semantic.extractor import extract_semantics
from transform.semantic.validator import validate_composition

def run_semantic_extraction(products):

    material_info=[]
    for product in products:

        product_text=product["materials_raw"]
        product_semantics=extract_semantics(product_text)
        material_info.append(validate_composition(product_semantics))

    return material_info


