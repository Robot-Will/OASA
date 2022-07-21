from . import atom
from . import bond
from . import cdml
from . import chem_vertex
from . import config
from . import coords_generator
from . import coords_optimizer
from . import geometry
from . import graph
from . import inchi
from . import linear_formula
from . import molecule
from . import molfile
from . import oasa_exceptions
from . import periodic_table
from . import query_atom
from . import smiles
from . import stereochemistry
from . import subsearch
from . import svg_out
from . import transform
from . import transform3d

atom = atom.atom
molecule = molecule.molecule
bond = bond.bond
query_atom = query_atom.query_atom
chem_vertex = chem_vertex.chem_vertex

all = [
    "atom",
    "bond",
    "molecule",
    "smiles",
    "coords_generator",
    "molfile",
    "inchi",
    "graph",
    "linear_formula",
    "periodic_table",
    "config",
    "coords_optimizer",
    "chem_vertex",
    "query_atom",
    "oasa_exceptions",
    "name_database",
    "subsearch",
    "svg_out",
    "stereochemistry",
    "geometry",
    "transform",
    "transform3d",
]

try:
    from . import cairo_out
except ImportError:
    CAIRO_AVAILABLE = False
else:
    all.append("cairo_out")
    CAIRO_AVAILABLE = True

# inchi_key
try:
    from . import inchi_key
except Exception as e:
    # print >> sys.stderr, "Module inchi_key could not be loaded - inchi_key related features will be disabled\nSee the error message for more info:\n  %s" % e
    INCHI_KEY_AVAILABLE = False
else:
    all.append("inchi_key")
    INCHI_KEY_AVAILABLE = True

# name_database (requires inchi_key which requires mhash in Python 2.4)
try:
    from . import name_database
except Exception as e:
    NAME_DATABASE_AVAILABLE = False
else:
    all.append("name_database")
    NAME_DATABASE_AVAILABLE = True

# structure_database requires sqlite
try:
    from . import structure_database
except Exception as e:
    # print >> sys.stderr, "Module structure_database could not be loaded - structure_database related features will be disabled\nSee the error message for more info:\n  %s" % e
    STRUCTURE_DATABASE_AVAILABLE = False
else:
    all.append("structure_database")
    STRUCTURE_DATABASE_AVAILABLE = True

# pybel deprecated
PYBEL_AVAILABLE = False


__all__ = all
