from __future__ import absolute_import

import copy


class edge:

    attrs_to_copy = ("disconnected",)

    def __init__(self, vs=[]):
        self.vertices = set()
        self.set_vertices(vs)
        self.properties_ = {}
        self.disconnected = False

    def __str__(self):
        return "edge between %s %s" % tuple(map(str, self.vertices))

    def copy(self):
        other = self.__class__()
        for attr in self.attrs_to_copy:
            setattr(other, attr, copy.copy(getattr(self, attr)))
        return other

    def set_vertices(self, vs=[]):
        if vs and len(vs) == 2:
            self.vertices = set(vs)

    def get_vertices(self):
        return self.vertices

    def get_neighbor_edges(self):
        v1, v2 = self.vertices
        out1 = [e for e in v1.get_neighbor_edges() if e != self]
        out2 = [e for e in v2.get_neighbor_edges() if e != self]
        return out1 + out2

    def get_neighbor_edges2(self):
        """returns 2 lists of neighbor edges (one for one side, one for the other)"""
        v1, v2 = self.vertices
        out1 = [e for e in v1.get_neighbor_edges() if e != self]
        out2 = [e for e in v2.get_neighbor_edges() if e != self]
        return out1, out2

    def _get_disconnected(self):
        return self._disconnected

    def _set_disconnected(self, d):
        self._disconnected = d

    # if d:
    #   warn(a "aaaaaa", UserWarning, 4)

    disconnected = property(_get_disconnected, _set_disconnected)
