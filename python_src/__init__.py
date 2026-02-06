__version__ = '1.18b'

def version():
    return __version__

import sys
from .database import get_tables, manifolds_path, original_manifolds_path
