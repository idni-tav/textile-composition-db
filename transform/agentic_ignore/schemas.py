from pydantic import BaseModel
from typing import List, Optional


class Material(BaseModel):
    name: str
    percentage: Optional[float]=None


class MaterialComposition(BaseModel):
    materials: List[Material]



class Certification(BaseModel):
    name: str
    confidence: float=1.0
    scope: str="unknown"  
    #possible values later:
    #"material", "garment", "process", "unknown"


class Origin(BaseModel):
    type: str  
    #"fabric_origin", "manufacturing_origin", "sourcing_region"
    value: str



class AttributedMaterial(BaseModel):
    name: str
    percentage: Optional[float]=None

    origins: List[Origin]=[]
    certifications: List[Certification]=[]


class FinalMaterialProfile(BaseModel):
    materials: List[AttributedMaterial]



class ProductInput(BaseModel):
    materials_raw: str