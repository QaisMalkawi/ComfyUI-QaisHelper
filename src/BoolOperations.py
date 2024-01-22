from typing import Any, Callable, Mapping

BOOL_BINARY_OPERATIONS: Mapping[str, Callable[[bool, bool], bool]] = {
    "Nor": lambda a, b: not (a or b),
    "Xor": lambda a, b: a ^ b,
    "Nand": lambda a, b: not (a and b),
    "And": lambda a, b: a and b,
    "Xnor": lambda a, b: not (a ^ b),
    "Or": lambda a, b: a or b,
    "Eq": lambda a, b: a == b,
    "Neq": lambda a, b: a != b,
}

class BoolUnaryOperation:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Input" : ("BOOLEAN", {}), 
                "Invert": ("BOOLEAN", {})
            },
        }
    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("Result",)
    FUNCTION = "op"
    CATEGORY = "Qais Helper/Boolean Operations"

    def op(self, Input, Invert):
        if Invert:
            return not Input
        else:
            return Input
        

class BoolBinaryOperation:
    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "op": (list(BOOL_BINARY_OPERATIONS.keys()),),
                "a": ("BOOLEAN", {}),
                "b": ("BOOLEAN", {})
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("Result",)
    FUNCTION = "op"
    CATEGORY = "Qais Helper/Boolean Operations"

    def op(self, op: str, a, b):
        return (BOOL_BINARY_OPERATIONS[op](a, b),)


NODE_CLASS_MAPPINGS = {
    "Bool Unary Operation": BoolUnaryOperation,
    "Bool Binary Operation": BoolBinaryOperation,
}
