from litellm import completion

from transform.semantic.prompts import COMPOSITION_PROMPT
from transform.semantic.schemas import MaterialComposition


MODEL="ollama_chat/llama3.1:8b"


def extract_composition(materials_raw: str) -> MaterialComposition:
    """
    Extract the material composition from raw product text.
    """

    response = completion(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": COMPOSITION_PROMPT,
            },
            {
                "role": "user",
                "content": materials_raw,
            },
        ],
    )

    content = response.choices[0].message.content

    return MaterialComposition.model_validate_json(content)





























import json
from smolagents import LiteLLMModel

from transform.semantic.prompts import COMPOSITION_PROMPT
from transform.semantic.schemas import MaterialComposition


def extract_composition(materials_raw: str) -> MaterialComposition:
    """
    Extracts the material composition from raw product text.

    Parameters
    ----------
    materials_raw : str
        Raw product description.

    Returns
    -------
    MaterialComposition
        Validated material composition.
    """

    model=LiteLLMModel(model_id="ollama_chat/llama3.1:8b")

    response=model(
        messages=[
            {
                "role": "system",
                "content": COMPOSITION_PROMPT,
            },
            {
                "role": "user",
                "content": materials_raw,
            },
        ]
    )

    return MaterialComposition.model_validate_json(response.content)


















