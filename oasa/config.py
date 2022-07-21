from pathlib import Path

from oasa import molecule


class Config:
    """this is a singleton class for library wide configuration"""

    molecule_class = molecule.molecule

    @classmethod
    def create_molecule(self):
        return self.molecule_class()

    inchi_binary_path = r"C:\Users\dario\.local\bin\inchi-1.exe"
    if not Path(inchi_binary_path).exists():
        assert RuntimeError(f"inchi-1.exe not found at {inchi_binary_path}!")
