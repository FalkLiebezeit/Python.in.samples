# graph.py
# Aus "Algorithmen in Python" Kapitel 4
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import TypeVar, Generic, List, Optional
from edge import Edge


V = TypeVar('V') # Typ der Knoten im Graphen


class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices) # Anzahl der Knoten

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges)) # Anzahl der Kanten

    # Einen Knoten zum Graphen hinzufügen und seinen Index zurückgeben
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([]) # Leere Liste zum Speichern von Kanten hinzufügen
        return self.vertex_count - 1 # Index des hinzugefügten Knotens zurückgeben

    # Dies ist ein ungerichteter Graph,
    # also fügen wir stets Kanten in beide Richtungen hinzu
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    # Eine Kante mithilfe von Knotenindizes hinzufügen (Hilfsmethode)
    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.add_edge(edge)

    # Eine Kante durch Nachschlagen von Knotenindizes hinzufügen (Hilfsmethode)
    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    # Den Knoten an einem bestimmten Index finden
    def vertex_at(self, index: int) -> V:
        return self._vertices[index]

    # Den Index eines Knotens im Graphen finden
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)

    # Die Knoten finden, mit denen ein Knoten an einem bestimmten Index verbunden ist
    def neighbors_for_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    # Den Index eines Knotens nachschlagen und seine Nachbarn finden (Hilfsmethode)
    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))

    # Alle Kanten zurückgeben, die mit einem Knoten an einem bestimmten Index verknüpft sind
    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    # Den Index eines Knotens nachschlagen und seine Kanten zurückgeben (Hilfsmethode)
    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    # Die wohlformatierte Ausgabe eins Graphen ermöglichen
    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc


if __name__ == "__main__":
    # Grundlegende Konstruktion des Graphen testen
    city_graph: Graph[str] = Graph(["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston", "New York", "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"])
    city_graph.add_edge_by_vertices("Seattle", "Chicago")
    city_graph.add_edge_by_vertices("Seattle", "San Francisco")
    city_graph.add_edge_by_vertices("San Francisco", "Riverside")
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles")
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside")
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Chicago")
    city_graph.add_edge_by_vertices("Phoenix", "Dallas")
    city_graph.add_edge_by_vertices("Phoenix", "Houston")
    city_graph.add_edge_by_vertices("Dallas", "Chicago")
    city_graph.add_edge_by_vertices("Dallas", "Atlanta")
    city_graph.add_edge_by_vertices("Dallas", "Houston")
    city_graph.add_edge_by_vertices("Houston", "Atlanta")
    city_graph.add_edge_by_vertices("Houston", "Miami")
    city_graph.add_edge_by_vertices("Atlanta", "Chicago")
    city_graph.add_edge_by_vertices("Atlanta", "Washington")
    city_graph.add_edge_by_vertices("Atlanta", "Miami")
    city_graph.add_edge_by_vertices("Miami", "Washington")
    city_graph.add_edge_by_vertices("Chicago", "Detroit")
    city_graph.add_edge_by_vertices("Detroit", "Boston")
    city_graph.add_edge_by_vertices("Detroit", "Washington")
    city_graph.add_edge_by_vertices("Detroit", "New York")
    city_graph.add_edge_by_vertices("Boston", "New York")
    city_graph.add_edge_by_vertices("New York", "Philadelphia")
    city_graph.add_edge_by_vertices("Philadelphia", "Washington")
    print(city_graph)

    # BFS aus Kapitel 2 für city_graph wiederverwenden
    import sys
    sys.path.insert(0, '..') # Um auf das Package Chapter2 im übergeordneten Verzeichnis zuzugreifen
    from Chapter2.generic_search import bfs, Node, node_to_path

    bfs_result: Optional[Node[V]] = bfs("Boston", lambda x: x == "Miami", city_graph.neighbors_for_vertex)
    if bfs_result is None:
        print("Keine Lösung mit Breitensuche gefunden!")
    else:
        path: List[V] = node_to_path(bfs_result)
        print("Pfad von Boston nach Miami:")
        print(path)

