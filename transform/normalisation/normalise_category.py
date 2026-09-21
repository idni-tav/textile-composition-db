
from transform.normalisation.category_mapping import category_dictionary

def run_category_normalisation(products):


    for product in products:

        sub_category=product['sub_category'].lower()
        product['parent_category']=category_dictionary[sub_category]
       

    return products