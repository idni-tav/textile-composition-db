#from transform.semantic.agents.composition_agent import build_composition_agent
from transform.semantic.agents.attribution_agent import build_attribution_agent

from transform.semantic.schemas import MaterialComposition, FinalMaterialProfile


def run_material_pipeline(materials_raw: str):
    """
    Full 2-stage semantic pipeline:
    1. Extract composition
    2. Attribute origins + certifications
    """

    #build agents
 
    #composition_agent=build_composition_agent()
    attribution_agent=build_attribution_agent()


    #agent 1: composition
    
    composition_output=composition_extractor.run(materials_raw)

    composition=MaterialComposition.model_validate(composition_output)


    #agent 2: Attribution

    attribution_output=attribution_agent.run({
        "materials": composition,
        "materials_raw": materials_raw
    })

    final_result=FinalMaterialProfile.model_validate(attribution_output)

    return final_result