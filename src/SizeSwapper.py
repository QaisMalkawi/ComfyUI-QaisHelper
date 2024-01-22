from .FreeType import any

class Size_Swapper:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "size1": ("INT", {}),
                "size2": ("INT", {}),
                "mode": (["width x height", "height x width", "width x width", "height x height"],),
            },
        }
        
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("Width", "Height")
    FUNCTION = "CheckSwap"
    #OUTPUT_NODE = True
    CATEGORY = "Qais Helper"
    
    def CheckSwap(self, size1, size2, mode):
        if mode == "width x height":
            return (size1, size2)
        elif mode == "height x width":
            return (size2, size1)
        elif mode == "width x width":
            return (size1, size1)
        elif mode == "height x height":
            return (size2, size2)

NODE_CLASS_MAPPINGS = {
    "Size Swapper": Size_Swapper,
}
