from typing import Optional 
from pydantic import BaseModel, Field 
import ollama


#pydantic class

class Material(BaseModel):
    material: str
    percentage: float=Field(ge=0, le=100)


class ProductSemantics(BaseModel):
    composition: Optional[list[Material]]=None
    certifications: list[str]=[]


SYSTEM_PROMPT="""
You are a semantic information extraction system for fashion products.

Extract ONLY information explicitly stated in the product text.

Rules:
- Extract material names and their percentages.
- Extract explicitly mentioned certifications.
- Do not infer information.
- If no composition is explicitly stated, return null.
- If no certifications are explicitly stated, return an empty list.
"""


def extract_semantics(product_text: str) -> ProductSemantics:

    response=ollama.chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": product_text,
            },
        ],
        format=ProductSemantics.model_json_schema(),
    )

    return ProductSemantics.model_validate_json(
        response.message.content
    )




def validate_composition(result: ProductSemantics) -> ProductSemantics:

    if result.composition is None:
        return result

    total=sum(
        material.percentage
        for material in result.composition
    )

    if total != 100:
        result.composition = None

    return result

