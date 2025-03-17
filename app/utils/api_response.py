from typing import Any, Dict

class APIResponse:
    def __init__(self, success: bool, data: Any = None, message: str = "", code: int = 200):
        self.success = success
        self.data = data
        self.message = message
        self.code = code

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "data": self.data,
            "message": self.message,
            "code": self.code
        }

    @staticmethod
    def success(data: Any, message: str = "Operación exitosa", code: int = 200):
        return APIResponse(True, data, message, code).to_dict()

    @staticmethod
    def error(message: str = "Ocurrió un error", code: int = 400):
        return APIResponse(False, None, message, code).to_dict()
