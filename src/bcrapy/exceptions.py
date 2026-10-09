

class BCRAError(Exception):
    pass

class APIError(BCRAError):
    pass

class BadRequestError(BCRAError):
    pass

class DataError(BCRAError):
    pass
