from oasa import graph
from oasa import periodic_table as PT


class chem_vertex(graph.vertex):

    """this class is a parent class of atoms, groups etc., it defines common properties
    for vertices used in chemical context. It should not be instantiated directly, but
    rather inherited from."""

    attrs_to_copy = graph.vertex.attrs_to_copy + (
        "charge",
        "x",
        "y",
        "z",
        "multiplicity",
        "valency",
        "charge",
        "free_sites",
    )

    def __init__(self, coords=None):
        graph.vertex.__init__(self)
        self.charge = 0
        self.free_sites = 0
        # None means not set (used)
        if coords:
            self.x, self.y, self.z = coords
        else:
            self.x = None
            self.y = None
            self.z = None
        self._multiplicity = 1

    def matches(self, other):
        if other is self:
            return False
        return True

    ## PROPERTIES

    # coords
    def _set_coords(self, coords):
        if len(coords) == 2:
            self.x, self.y = coords
            self.z = 0
        elif len(coords) == 3:
            self.x, self.y, self.z = coords
        else:
            raise "wrong number of coordinates"

    def _get_coords(self):
        return self.x, self.y, self.z

    coords = property(_get_coords, _set_coords, None, "atom coords")

    # charge
    def _set_charge(self, charge):
        self._clean_cache()
        self._charge = charge

    def _get_charge(self):
        return self._charge

    charge = property(_get_charge, _set_charge, None, "atom charge")

    # multiplicity
    def _set_multiplicity(self, multiplicity):
        self._clean_cache()
        self._multiplicity = multiplicity

    def _get_multiplicity(self):
        return self._multiplicity

    multiplicity = property(
        _get_multiplicity, _set_multiplicity, None, "atom multiplicity"
    )

    # valency
    def _set_valency(self, valency):
        self._clean_cache()
        self._valency = valency

    def _get_valency(self):
        return self._valency

    valency = property(_get_valency, _set_valency, None, "atoms valency")

    # occupied_valency
    def _get_occupied_valency(self):
        i = 0
        for b in self._neighbors.keys():
            ord = b.order
            if ord == 4:
                ord = 1
            i += ord
        return i

    occupied_valency = property(
        _get_occupied_valency, None, None, "atoms occupied valency"
    )

    # free_valency
    def _get_free_valency(self):
        try:
            return self._cache["free_valency"]
        except KeyError:
            x = self.valency - self.occupied_valency
            self._cache["free_valency"] = x
            return x

    free_valency = property(_get_free_valency, None, None, "atoms free valency")

    # weight
    def _get_weight(self):
        try:
            return PT.periodic_table[self.symbol]["weight"]
        except:
            return 0

    weight = property(_get_weight, None, None, "atom weight")

    # free_sites
    def _set_free_sites(self, free_sites):
        self._free_sites = free_sites

    def _get_free_sites(self):
        really_free = self._free_sites - self.occupied_valency
        if really_free < 0:
            return 0
        else:
            return really_free

    free_sites = property(_get_free_sites, _set_free_sites, None, "atoms free_sites")

    def get_x(self):
        return self.x or 0

    def get_y(self):
        return self.y or 0

    def get_z(self):
        return self.z or 0

    def has_aromatic_bonds(self):
        for b in self._neighbors.keys():
            if b.aromatic:
                return 1
        return 0

    def bond_order_changed(self):
        """called by a bond when its order was changed"""
        self._clean_cache()

    def get_hydrogen_count(self):
        return 0
