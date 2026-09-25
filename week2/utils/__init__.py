# Controls what 'from utils import *' exposes
# Also runs on 'import utils' — keep it minimal
from .math_utils import safe_divide, percentage, clamp
from .string_utils import slugify, truncate

__all__ = ["safe_divide", "percentage", "clamp", "slugify", "truncate"]

