#--------------------------------------------------------------------------
#     This file is part of OASA - a free chemical python library
#     Copyright (C) 2003-2008 Beda Kosata <beda@zirael.org>

#     This program is free software; you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation; either version 2 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     Complete text of GNU GPL can be found in the file gpl.txt in the
#     main directory of the program

#--------------------------------------------------------------------------

import sys
if not (sys.version_info[0] > 2 or (sys.version_info[0] == 2 and sys.version_info[1] >= 3)):
  raise ImportError, "Python version %d.%d is lower than 2.3 which is needed by OASA" % sys.version_info[0:2]


import atom
import bond
import molecule
import smiles
import coords_generator
import coords_optimizer
import molfile
import inchi
import cdml
import graph
import linear_formula
import periodic_table
import config
import query_atom
import chem_vertex
import oasa_exceptions
import subsearch
import svg_out
import stereochemistry
import geometry
import transform3d
import transform

atom = atom.atom
molecule = molecule.molecule
bond = bond.bond
query_atom = query_atom.query_atom
chem_vertex = chem_vertex.chem_vertex

all = ['atom','bond','molecule','smiles','coords_generator','molfile','inchi','graph',
       "linear_formula",'periodic_table','config','coords_optimizer','chem_vertex',
       'query_atom','oasa_exceptions','name_database',"subsearch", "svg_out",
       'stereochemistry','geometry','transform','transform3d']

try:
  import cairo_out
except:
  CAIRO_AVAILABLE = False
else:
  all.append( "cairo_out")
  CAIRO_AVAILABLE = True

# inchi_key
try:
  import inchi_key
except Exception, e:
  #print >> sys.stderr, "Module inchi_key could not be loaded - inchi_key related features will be disabled\nSee the error message for more info:\n  %s" % e
  INCHI_KEY_AVAILABLE = False
else:
  all.append( "inchi_key")
  INCHI_KEY_AVAILABLE = True

# name_database (requires inchi_key which requires mhash in Python 2.4)
try:
  import name_database
except Exception, e:
  NAME_DATABASE_AVAILABLE = False
else:
  all.append( "name_database")
  NAME_DATABASE_AVAILABLE = True

# structure_database requires sqlite
try:
  import structure_database
except Exception, e:
  #print >> sys.stderr, "Module structure_database could not be loaded - structure_database related features will be disabled\nSee the error message for more info:\n  %s" % e
  STRUCTURE_DATABASE_AVAILABLE = False
else:
  all.append( "structure_database")
  STRUCTURE_DATABASE_AVAILABLE = True

# pybel
try:
  import pybel_bridge
except Exception, e:
  #print >> sys.stderr, "The 'pybel_bridge' python module could not be loaded - oasa-pybel integration will be disabled\nSee the error message for more info:\n  %s" % e
  PYBEL_AVAILABLE = False
else:
  all.append( "pybel_bridge")
  PYBEL_AVAILABLE = True  


__all__ = all




  
