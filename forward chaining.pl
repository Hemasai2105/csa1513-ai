% Make the predicate dynamic
:- dynamic fact/1.

% Clear all previous facts (optional but useful for reset)
reset_facts :-
    retractall(fact(_)).

% Insert initial base facts
init_facts :-
    assertz(fact(rainy)),
    assertz(fact(cloudy)).

% Rule definitions
rule(wet_ground) :- fact(rainy).
rule(use_umbrella) :- fact(rainy).
rule(dark_sky) :- fact(cloudy).

% Forward chaining logic
forward :-
    rule(X),
    \+ fact(X),
    assertz(fact(X)),
    forward.
forward.

% Print all facts in the knowledge base
print_facts :-
    fact(X),
    write(X), nl,
    fail.
print_facts.
