from setuptools import setup

setup()

set = setup(
    name="oasa",
    version="0.13.1",
    description="OASA is a free cheminformatics library written in Python",
    author="Beda Kosata",
    author_email="beda@zirael.org",
    url="https://bkchem.zirael.org/oasa_en.html",
    license="GNU GPL",
    platforms=["Unix", "Windows", "hopefully other OSes able to run Python"],
    long_description="OASA is a free cheminformatics library written in Python",
    packages=["oasa", "oasa/graph"],
    # data_files=[ ('oasa', glob.glob( 'oasa/templates/*.cdml')+glob.glob('templates/*.xml')),
    # windows=['oasa'],
    # options = {"py2exe": {"packages": ["encodings"]}}
)
