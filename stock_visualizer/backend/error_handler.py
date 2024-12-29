class DataFetchError(Exception):
    """Exception raised for errors in data fetching"""
    pass

class ValidationError(Exception):
    """Exception raised for validation errors"""
    pass

def handle_error(error: Exception) -> str:
    """Central error handling function"""
    if isinstance(error, DataFetchError):
        return f"Data Fetch Error: {str(error)}"
    elif isinstance(error, ValidationError):
        return f"Validation Error: {str(error)}"
    return f"Unexpected Error: {str(error)}" 