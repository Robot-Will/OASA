class diedge:
    def __init__(self, vs=[]):
        self.vertices = []
        self.set_vertices(vs)
        self.properties_ = {}

    def __str__(self):
        return "directed edge between %s %s" % tuple(map(str, self.vertices))

    def set_vertices(self, vs=[]):
        if vs and len(vs) == 2:
            self.vertices = vs

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
