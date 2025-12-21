from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from typing import Union, Dict
from typing import Any, List, Optional, Dict

def custom_response(
    status_code: int,
    status: str,
    message: str,
    data: Optional[Union[dict, List[dict], None]] = None,
    error_details: Optional[dict] = None,
    pagination: Optional[dict] = None
) -> JSONResponse:
    """
    Creates a custom JSON response for FastAPI with a structured format.
    
    :param status_code: HTTP Status Code (e.g., 200, 404, 500)
    :param status: Response status ('success' or 'error')
    :param message: A message describing the response or error
    :param data: Optional response data (e.g., the results from a query)
    :param error_details: Optional details for error responses
    :param pagination: Optional pagination info for paginated results
    :return: A structured JSONResponse
    """
    response = {
        "status": status,
        "message": message,
        "data": data,
        "error_details": error_details,
        "pagination": pagination,
    }
    
    # Remove None fields from the response
    response = {key: value for key, value in response.items() if value is not None}
    
    return JSONResponse(status_code=status_code, content=response)
