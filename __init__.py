from .src.InputSwitch import NODE_CLASS_MAPPINGS as inputSW_CN
from .src.Debugger import NODE_CLASS_MAPPINGS as debugger_CN
from .src.SizeSwapper import NODE_CLASS_MAPPINGS as swapper_CN
from .src.BoolOperations import NODE_CLASS_MAPPINGS as boolOp_CN
from .src.Graphics import NODE_CLASS_MAPPINGS as graphics_cn

NODE_CLASS_MAPPINGS = {
    **inputSW_CN,
    **debugger_CN,
    **swapper_CN,
    **boolOp_CN,
    **graphics_cn,
}

def Add_Prefix(node_mapping: str) -> str:
    return "QH: " + node_mapping

NODE_DISPLAY_NAME_MAPPINGS = {key: Add_Prefix(key) for key in NODE_CLASS_MAPPINGS}
