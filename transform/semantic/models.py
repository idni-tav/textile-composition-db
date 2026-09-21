#this file defines the Pydantic enforced structure for the semantic output.


from pydantic import BaseModel, Field 
from typing import Optional

class Material(BaseModel):
    material: str
    percentage: float=Field(ge=0, le=100)


class ProductSemantics(BaseModel):
    composition: Optional[list[Material]]=None
    certifications: list[str]=[]