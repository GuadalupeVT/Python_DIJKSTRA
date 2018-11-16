#https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
from collections import deque, namedtuple

# infinito como la distancia default entre nodos
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

def hacer_edge(start, end, cost=1):
    return Edge(start, end, cost)

class Grafo:
    def __init__(self, edges):
        # verificar que la informacion sea correcta
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Datos de edges erroneos: {}'.format(wrong_edges))

        self.edges = [hacer_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_nodo_par(self, n1, n2, both_ends=True):
        if both_ends:
            nodoPar = [[n1, n2], [n2, n1]]
        else:
            nodoPar = [[n1, n2]]
        return nodoPar

    def remover_edge(self, n1, n2, both_ends=True):
        nodoPar = self.get_nodoPar(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in nodoPar:
                self.edges.remove(edge)

    def agregar_edge(self, n1, n2, cost=1, both_ends=True):
        nodoPar = self.get_nodoPar(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in nodoPar:
                return ValueError('Edge {} {} ya existe'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

'''
Created on 16/11/2018

@author: GVT
'''
