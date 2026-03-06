__version__ = '1.20'

def version():
    return __version__

import sys
from .database import get_tables, manifolds_path, original_manifolds_path