father(john, alice).
father(john, bob).
mother(mary, alice).
mother(mary, bob).

sibling(X, Y) :- 
    father(F, X), father(F, Y), 
    mother(M, X), mother(M, Y), 
    X \= Y.
