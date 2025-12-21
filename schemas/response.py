from pydantic import BaseModel
from typing import Any, List, Optional, Union


class StandardResponse(BaseModel):
    status: str
    message: str
    data: Optional[Union[dict, List[dict], None]] = None
    error_details: Optional[dict] = None
    pagination: Optional[dict] = None 
