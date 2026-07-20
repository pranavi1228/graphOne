from pydantic import BaseModel
from typing import Optional


class Startup(BaseModel):

    schemaVersion: str

    recordType: str

    source: dict

    content: dict

    collectedAt: str