from extract.scraper import run_extraction
from transform.normalisation.normalise_category import run_category_normalisation
from transform.semantic.semantics import run_semantic_extraction


# step 1: run scraper 
products=run_extraction(2)

# step 2: normalise garment category names
products=run_category_normalisation(products)

# step 3: extract material info from product text
#material_info=run_semantic_extraction(products)


print(products)