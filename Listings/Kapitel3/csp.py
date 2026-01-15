# csp.py
# Aus "Algorithmen in Python", Kapitel 3
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
from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V') # Variablen-Typ
D = TypeVar('D') # Domänen-Typ


# Basisklasse für alle Bedingungen
class Constraint(Generic[V, D], ABC):
    # Die Variablen, zwischen denen die Bedingung besteht
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    # Muss von Unterklassen überschrieben werden
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...


# Ein Bedingungserfüllungsproblem besteht aus Variablen vom Typ V,
# die Wertebereiche namens Domänen vom Typ D und Bedingungen haben,
# die bestimmen, ob die Domänenauswahl einer bestimmten Variablen gültig ist
class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables # Variablen, für die Bedingungen gelten
        self.domains: Dict[V, List[D]] = domains # Die Domänen der Variablen
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Jeder Variablen sollte eine Domäne zugewiesen werden.")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in Bedingung nicht im CSP")
            else:
                self.constraints[variable].append(constraint)

    # Prüfen, ob die Wertzuweisung konsistent ist, indem alle Bedingungen für
    # die gegebene Variable damit verglichen werden
    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # Zuordnung beendet, wenn jede Variable zugeordnet ist (unsere Abbruchbedingung)
        if len(assignment) == len(self.variables):
            return assignment

        # Alle Variablen holen, die im CSP, aber in keiner Zuordnung sind
        unassigned: List[V] = [v for v in self.variables if v not in assignment]

        # Jeden möglichen Domänenwert der ersten nicht zugeordneten Variablen holen
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            # Wenn wir noch konsistent sind, Rekursion (fortfahren)
            if self.consistent(first, local_assignment):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                # Wenn wir das Ergebnis nicht gefunden haben, Backtracking
                if result is not None:
                    return result
        return None
