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

