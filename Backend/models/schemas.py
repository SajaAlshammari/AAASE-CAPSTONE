from pydantic import BaseModel
from typing import List


class Candidate(BaseModel):
    name: str
    email: str
    position: str
    experience: str
    skills: List[str]