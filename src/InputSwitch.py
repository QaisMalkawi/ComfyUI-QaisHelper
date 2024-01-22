from .FreeType import any

class Input_Switch:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Input1" : (any, {}), 
                "Input2" : (any, {}), 
                "Use_First": ("BOOLEAN",)
            },
        }

    @classmethod
    def VALIDATE_INPUTS(s, **kwargs):
        return True
    
    RETURN_TYPES = (any, )
    RETURN_NAMES = ("output", )

    FUNCTION = "SelectInput"

    #OUTPUT_NODE = False

    CATEGORY = "Qais Helper"

    def SelectInput(self, Input1, Input2, Use_First):
        if Use_First:
            return (Input1,)
        else:
            return (Input2,)

NODE_CLASS_MAPPINGS = {
    "Item Switch": Input_Switch,
}