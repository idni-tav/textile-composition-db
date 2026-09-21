
from transform.semantic.models import ProductSemantics
import ollama
from transform.semantic.prompts import SYSTEM_PROMPT
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