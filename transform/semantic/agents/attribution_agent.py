from smolagents import ToolCallingAgent, LiteLLMModel
#from smolagents.models import OllamaModel
#from smolagents import InferenceClientModel

from transform.semantic.prompts import ATTRIBUTION_PROMPT
from transform.semantic.schemas import FinalMaterialProfile
from transform.semantic.tools import lookup_certification

import importlib.resources
import yaml


def build_attribution_agent():


    #getting the default prompt from the source code
    folder=importlib.resources.files("smolagents.prompts")
    file=folder.joinpath("toolcalling_agent.yaml")
    text=file.read_text()
    default_prompt_templates=yaml.safe_load(text)

    #adding our propmt to the system prompt
    attribution_prompt_templates=default_prompt_templates.copy()
    attribution_prompt_templates["system_prompt"]+="\n\n"+ATTRIBUTION_PROMPT

    
    model=LiteLLMModel(model_id="ollama_chat/llama3.1:8b")

    
    agent=ToolCallingAgent(
        model=model,
        tools=[lookup_certification],
        prompt_templates=attribution_prompt_templates,
    )


    return agent

