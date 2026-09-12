import re
from smolagents import tool

CERTIFICATION_REGISTRY={
    "oeko_tex_standard_100": {
        "name": "OEKO-TEX Standard 100",
        "acronym": "OEKO-TEX",
        "applies_to": ["yarn","fabric","finished_garment"],
        "description": "Label for fabrics tested for harmful substances",
    },
    "gots": {
        "name": "Global Organic Textile Standard",
        "acronym": "GOTS",
        "applies_to": ["fiber","yarn","fabric"],
        "description": "Label for textiles produced from organic fibres",
    },
    "ecolabel": {
        "name": "EU Ecolabel",
        "acronym": None,
        "applies_to": ["finished_garment"],
        "description": "Label that certifies products with low environmental impact ",
    },
    "recycled_claim_standard": {
        "name": "Recycled Claim Standard",
        "acronym": "RCS",
        "applies_to": ["fibre","yarn","fabric"],
        "description": "Label that allows the marketing of textiles made from recycled materials",
    },
    "global_recycled_standard": {
        "name": "Global Recycled Standard",
        "acronym": "GRS",
        "applies_to": ["fiber","yarn","fabric","finished_garment"],
        "description": "Label that ensures at least 20% of the garment was made with recycled materials",
    },
    "bluesign_product": {
        "name": "Bluepass Consumer Product",
        "acronym": None,
        "applies_to": ["finished_garment"],
        "description": "Label that guarantees 90% of components of the product were produced with social and environmental responsibility",
    },
}


@tool
def lookup_certification(certification_name: str) -> dict | None:
    """
    Look up a certification in the registry.

    Args:
        certification_name: Name or acronym of the certification.

    Returns:
        Metadata dictionary for the certification if found, otherwise None.
    """

    def normalize(text):
        """Lowercase and replace non-alphanumeric characters with underscores."""
        text=text.lower()
        text=re.sub(r"[^a-z0-9]+", "_", text)
        return text.strip("_")   #removes trailing and leading underscores only

    query=normalize(certification_name)

    #1) direct lookup by registry key
    if query in CERTIFICATION_REGISTRY:
        return CERTIFICATION_REGISTRY[query]

    #2) lookup by official name or acronym
    for cert in CERTIFICATION_REGISTRY.values():

        if normalize(cert["name"])==query:
            return cert

        if cert["acronym"] and normalize(cert["acronym"])==query:
            return cert

    return None