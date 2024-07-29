from typing import List, Optional, Union
from pydantic import BaseModel, field_validator

class GetTicketsRequest(BaseModel):
    acoes: Optional[List[str]] = None
    fiis: Optional[List[str]] = None

    @field_validator('fiis')
    def fiis_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('A lista de FIIs não pode ser vazia.')
        return v

    @field_validator('acoes')
    def acoes_must_not_be_empty(cls, v):
        if not v:
            raise ValueError('A lista de ações não pode ser vazia.')
        return v