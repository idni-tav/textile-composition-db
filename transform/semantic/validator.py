
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

