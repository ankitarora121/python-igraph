#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple script that tests CytoscapeGraphDrawer.

This script is kept separate from the unit tests as it is very
hard to test for the correctness of CytoscapeGraphDrawer without
a working instance of Cytoscape.

Prerequisites for running this test:

    1. Start Cytoscape
    2. Activate the Cytoscape RPC plugin, listening at port 9000

"""

from igraph import Graph
from igraph.drawing.graph import CytoscapeGraphDrawer

def test():
    g = Graph.GRG(100, 0.2)

    # String attribute
    g.vs["name"] = ["Node %d" % (i+1) for i in xrange(g.vcount())]
    # Integer attribute
    g.vs["degree"] = g.degree()
    # Float attribute
    g.vs["pagerank"] = g.pagerank()
    # Boolean attribute
    g.vs["even"] = [i % 2 for i in xrange(g.vcount())]
    # Mixed attribute
    g.vs["mixed"] = ["abc", 123, None, 1.0] * ((g.vcount()+3) / 4)
    # Special attribute with Hungarian accents
    g.vs[0]["name"] = u"árvíztűrő tükörfúrógép ÁRVÍZTŰRŐ TÜKÖRFÚRÓGÉP"

    # String attribute
    g.es["name"] = ["Edge %d -- %d" % edge.tuple for edge in g.es]
    # Integer attribute
    g.es["multiplicity"] = g.count_multiple()
    # Float attribute
    g.es["betweenness"] = g.edge_betweenness()
    # Boolean attribute
    g.es["even"] = [i % 2 for i in xrange(g.ecount())]
    # Mixed attribute
    g.es["mixed"] = [u"yay", 123, None, 0.7] * ((g.ecount()+3) / 4)

    drawer = CytoscapeGraphDrawer()
    drawer.draw(g)

if __name__ == "__main__":
    test()

