from depth_first_traversal import Graph

def test_unit():
    g1 = Graph([1, 2, 3], [(1, 2), (2, 3)])     
    assert g1.dfs() == [1, 2, 3]

def test_kritical():
    g2 = Graph([], [])
    assert g2.dfs() == []
