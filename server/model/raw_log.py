from pydantic import BaseModel
from typing import Optional

class RawLog(BaseModel):
    provider: str
    data: str
    timestamp: str  # ISO format string 