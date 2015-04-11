# this polyomino class code is obtained from https://parallelstripes.wordpress.com/2009/12/20/generating-polyominoes/
class Polyomino:
   def __init__(self, seq=[]):
        """Initialize polyomino set with sequence of cells."""

        self.cells = set(self.translate(seq)) 

   def translate(self,seq):
        """
        Translate sequence of cells to origin
        substracting minimum x and y values.

        """
        if seq == []: return [] 
        mx, my = reduce(lambda (rx,ry), (sx,sy): (min(rx,sx), min(ry,sy)), seq)
        return ((x - mx, y - my) for x, y in seq)
 
   def add_cell(self, c):
        """Return a new polyomino with the cell added."""
        return Polyomino(self.cells.union(set([c])))

   def contiguous_cells(self,x, y):
        return (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
   def new_cells(self):
        """
        Return list of cells that are contiguous to any cell
        in the polyomino, and fall outside of it.
     
        """
     
        nc = set()
        for x, y in self.cells:
            for c in self.contiguous_cells(x, y):
                nc.add(c)
        nc -= self.cells
        return nc

   def __eq__(self, other):
        return self.cells == other.cells

   def __repr__(self):
        return repr(self.cells)

def gen_fixed(n):
    """Generate list of fixed polyominoes up to n."""
    if n == 1:
        yield Polyomino([(0, 0)])
    elif n > 1:
        polys = []
        for P in gen_fixed(n - 1):
            for c in P.new_cells():
                new_poly = P.add_cell(c)
                if new_poly not in polys:
                    polys.append(new_poly)
                    yield new_poly

ig =  list( gen_fixed(4) )
for i in xrange(len(ig)):
    # for j in xrange(i+1, len(ig)):
    # for j in 
        # print i, j
        # print ig[i]==1 ig[j]
    print ig[i]
