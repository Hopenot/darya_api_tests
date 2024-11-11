from pydantic import BaseModel
from typing import List, Any


class MemeJson(BaseModel):
    id: int
    info: dict
    tags: List[str]
    text: str
    updated_by: str
    url: str

class MemesListJson(MemeJson):
    data: List[MemeJson]

class DeleteMemeModel(BaseModel):
    data: Any
