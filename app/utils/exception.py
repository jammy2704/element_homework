from fastapi import status, HTTPException

class APIException(HTTPException):

    status_code = status.HTTP_400_BAD_REQUEST
    detail = None

    def __init__(self, *args, **kwargs):
        if "status_code" not in kwargs:
            kwargs["status_code"] = self.status_code
        if "detail" not in kwargs:
            kwargs["detail"] = self.detail
        super().__init__(*args, **kwargs)


class InvalidParameter(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "N must be a positive integer"


class InvalidLengthOfArray(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "length of array should be more than n"
