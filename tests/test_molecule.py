from oasa import smiles
from oasa.linear_formula import linear_formula


def test_formula():
    formulas = [
        ("CH3COOH", "CC(=O)O", 0, 0),
        ("CH3C(CH3)3", "CC(C)(C)C", 0, 0),
        ("CH2C(CH3)3", "CC(C)(C)C", 1, 0),
        ("(CH2)7Cl", "CCCCCCCCl", 1, 0),
    ]
    lin = linear_formula()
    for linear, smile, start_valency, end_valency in formulas:

        m1 = lin.parse_text(
            linear, start_valency=start_valency, end_valency=end_valency
        )
        m2 = smiles.text_to_mol(smile)

        assert m1 == m2


def test_substructure():
    formulas = [
        ("CC(=O)C", "CC(=O)C", True),
        ("CCCC", "CCC", True),
        ("CC(=O)C", "C=O", True),
        ("C=O", "CC(=O)C", False),
        ("C(=O)H", "C=O", True),
        ("C=O", "C(=O)H", True),  # implicit hydrogens work
        ("C(=O)O", "C(=O)OH", True),  # implicit hydrogens work
        ("C(=O)OH", "C(=O)O", True),
        ("C(=O)OC", "C(=O)OH", False),  # explicit hydrogens work
        ("C(=O)OC", "C(=O)[OH]", False),  # explicit hydrogens in atom specs work
        ("C(=O)OC", "C(=O)O", True),
        #
        ("CC(=O)H", "C(=O)H", True),
        # charges
        ("C(=O)[O-]", "C(=O)O", True),
        ("C(=O)O", "C(=O)[O-]", False),
        ("C(=O)[O-]", "C(=O)[OH]", False),
        ("C(=O)[OH]", "C(=O)[O-]", False),
        ("C(=O)[O-]", "C(=O)OH", False),
        ("C(=O)OCC", "C(=O)[O-]", False),
    ]
    for smile1, smile2, expected in formulas:
        m1 = smiles.text_to_mol(smile1)
        m2 = smiles.text_to_mol(smile2)
        assert m1.contains_substructure(m2) == expected


def test_SMILES_equality():
    formulas = [
        ("Sc1ccccc1", "S-c1ccccc1", True),  # check Sc (in PT scandium) bug
        ("Oc1ccccc1", "O-c1ccccc1", True),
        ("c1ccccc1", "C:1:C:C:C:C:C:1", True),
        ("c1ccccc1", "[CH]:1:[CH]:[CH]:[CH]:[CH]:[CH]:1", True),
        ("c1cscc1", "C1=C-S-C=C1", True),
        ("c1ccccc1", "C1=CC=CC=C1", True),
        ("c1ccccc1", "C=1C=CC=CC=1", True),
        ("C=1CC=1", "C1C=C1", True),
        ("C12CC%01CC2", "C12CC1CC2", True),
        ("C%01%02CC%01CC2", "C12CC1CC2", True),
        ("Oc%11ccccc%11", "Oc1ccccc1", True),
        ("C%99CCCCC%992CCCCC2", "C1CCCCC12CCCCC2", True),
        ("C%99CCCCC%88%99CCCCC%88", "C1CCCCC12CCCCC2", True),
        ("H", "[H]", False),
        ("C", "[2H]C", False),
        ("[C]", "[CH0]", True),
    ]
    for smile1, smile2, expected in formulas:
        m1 = smiles.text_to_mol(smile1)
        m2 = smiles.text_to_mol(smile2)
        assert (m1 == m2) == expected


def test_smiles_reading():
    formulas = [
        ("Sc1ccccc1", ("C6H6S",)),
        ("Oc1ccccc1", ("C6H6O",)),
        ("Oc%11ccccc%11", ("C6H6O",)),
        ("[Na+].[Cl-]", ("Na", "Cl")),
        ("[O-]c1ccccc1.[Na+]", ("C6H5O", "Na")),
        ("O=C[O-].[NH4+]", ("CHO2", "H4N")),
        ("c1ccccc1-c1ccccc1", ("C12H10",)),
        ("c1cscc1", ("C4H4S",)),
    ]

    for smile1, sum_forms in formulas:
        conv = smiles.converter()
        mols = conv.read_text(smile1)

        assert all([str(mol.get_formula_dict()) in sum_forms for mol in mols])
        assert len(mols) == len(sum_forms)
