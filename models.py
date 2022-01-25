from typing import Optional, List

from pydantic import BaseModel


class Term(BaseModel):
    type: Optional[int]
    terms: Optional[List[str]]
