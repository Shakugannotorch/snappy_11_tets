__version__ = '1.19'

def version():
    return __version__

import sys
from .database import get_tables, manifolds_path, original_manifolds_path

try:
    import snappy
    table_dict = snappy.database.add_tables_from_package('snappy_11_tets', False)
    for name, table in table_dict.items():
        setattr(snappy, name, table)
        if name not in snappy.database_objects:
            snappy.database_objects.append(name)
except:
    pass