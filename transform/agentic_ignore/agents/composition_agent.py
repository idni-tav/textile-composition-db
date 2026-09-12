from smolagents import ToolCallingAgent, LiteLLMModel
from transform.semantic.prompts import COMPOSITION_PROMPT
from transform.semantic.schemas import MaterialComposition

import importlib.resources
import yaml


def build_composition_agent():

    #getting the default prompt from the source code
    folder=importlib.resources.files("smolagents.prompts")
    file=folder.joinpath("toolcalling_agent.yaml")
    text=file.read_text()
    default_prompt_templates=yaml.safe_load(text)

    #adding our propmt to the system prompt
    composition_prompt_templates=default_prompt_templates.copy()
    composition_prompt_templates["system_prompt"]+="\n\n"+COMPOSITION_PROMPT

    
    model=LiteLLMModel(model_id="ollama_chat/llama3.1:8b")

    
    agent=ToolCallingAgent(
        model=model,
        tools=[],
        prompt_templates=composition_prompt_templates,
    )

    return agent




