# OASA

### Introduction
[BKChem](http://bkchem.zirael.org) is a free chemical drawing program. It was conceived and written by [Beda Kosata](beda@zirael.org) and is currently maintained by [Reinis Danne](rei4dan@gmail.com). BKChem is written in Python, and it is based on [OASA](http://bkchem.zirael.org/oasa_en.html) library. Unfortunately, BKChem is dead in 2010.

![Image of BKChem](http://bkchem.zirael.org/img/bkchem_macos_10_2-small.png)

[OASA](http://bkchem.zirael.org/oasa_en.html) is a free python library for manipulating and analyzing chemical structures. Even though OASA is already some 4 years old project, its API may be unstable. This is mainly because it was never before released outside of BKChem and Reinis Danne followed all significant API changes there. Therefore please do not expect a highly polished, well documented library. OASA is probably rather the opposite. You have been warned.

### Features
* reading and writing of SMILES, InChI, Molfile
* atom coordinate generation
* molecule rendering into PNG, PDF and SVG using cairo

### Missing features
* documentation
* full streochemistry support (only cis/trans double bond stereochemistry is supported)
* many more I cannot remember now

### Sample export
This is an example of PNG export:

![Image of OASA](http://bkchem.zirael.org/img/22646404.png)

### Requirements
* OASA needs python 2.3 or higher to run properly.


### STATUS
bellow are summarized the limitations of the library. it does by no means mean that there are no other limitations, however, for these it has no sense to write bugreports :)


##### OVERALL:
- no documentation beyond the source code is available
- stereochemistry support is limited to cis/trans stereochemistry on double bonds
  and only in some formats
- not much effort was invested into optimalization of the code, it may be pretty slow sometimes
- the API might be unstable


##### SMILES:
- cis/trans stereochemistry is supported, some attempt were made to make tetrahedral stereochemistry
  work, but it is not very much tested


##### InChI:
- reading is done natively by OASA
- for writing the original InChI program is needed (cInChI, cInChI.exe)


##### MOLFILE
- not all data in the properties block (after the bond block) are supported
  (this means that molfiles containing a properties block might not be read properly)


##### COORDS GENERATOR:
- coords for molecules like calix[4]arene and similar do not give a very nice picture
- tetrahedral stereochemistry is not taken into account


##### CAIRO_OUT:
- pycairo is required to make use of cairo_out functionality
- PNG, PDF and SVG export is supported now
