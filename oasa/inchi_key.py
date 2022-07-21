from rdkit import Chem


def key_from_inchi(input_inchi: str) -> str:
    """Use rdkit to drop legacy code"""
    mol = Chem.MolFromInchi(input_inchi)
    return Chem.MolToInchiKey(mol)


if __name__ == "__main__":
    inp = "InChI=1S/C6H10/c1-3-5-6-4-2/h3-6H,1-2H3/b5-3+,6-4+"
    out = "APPOKADJQUIAHP-GGWOSOGESA-N"
    ret = key_from_inchi(inp)
    print(ret)
    print(ret == out)
