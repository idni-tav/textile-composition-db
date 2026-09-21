from extract.scraper import run_extraction
from transform.normalisation.normalise_category import run_category_normalisation


# step 1: run scraper 
products=run_extraction(5)

#print("BEFORE:", products[0])

# step 2: normalise garment category names
products=run_category_normalisation(products)

#print("AFTER:", products[0])
print(products)