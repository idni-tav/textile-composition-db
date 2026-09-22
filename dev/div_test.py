from extract.shared.http import get_soup

#to run this script : python -m dev.div_test




URL="https://indigoluna.store/products/frida-skirt-masala"

soup = get_soup(URL)

blocks = []

for details in soup.find_all("details"):

    summary = details.find("summary")

    if summary and "Material & Care" in summary.get_text(" ", strip=True):
        blocks.append(details)


print(f"Found {len(blocks)} matching blocks\n")

for i, block in enumerate(blocks, start=1):

    print(f"--- Block {i} ---")
    print(block.get_text(" ", strip=True))
    print()