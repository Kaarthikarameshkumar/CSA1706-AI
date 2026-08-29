% FACTS

male(john).
male(robert).
male(david).
male(michael).

female(mary).
female(susan).
female(linda).
female(emma).

parent(john, robert).
parent(mary, robert).

parent(john, susan).
parent(mary, susan).

parent(robert, david).
parent(linda, david).

parent(robert, emma).
parent(linda, emma).

% RULES

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

grandfather(X, Y) :-
    male(X),
    grandparent(X, Y).

grandmother(X, Y) :-
    female(X),
    grandparent(X, Y).
