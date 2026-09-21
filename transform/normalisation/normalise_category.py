
from transform.normalisation.category_mapping import category_dictionary

def run_category_normalisation(products):


    for product in products:

        category=product['category'].lower()
        product['normalised category']=category_dictionary[category]
       

    return products