from .FreeType import any

class Item_Debugger:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "debug_title": ("STRING", {"default": 'Output:', "multiline": False}),
                "debug_value": (any, {}),
            },
        }
        
    RETURN_TYPES = ()
    FUNCTION = "WriteTerminal"
    OUTPUT_NODE = True
    CATEGORY = "Qais Helper"
    
    def WriteTerminal(self, debug_title, debug_value):
        resM = f"{debug_title} {debug_value}"
        print(resM)
        return ()
    
NODE_CLASS_MAPPINGS = {
    "Item Debugger": Item_Debugger,
}