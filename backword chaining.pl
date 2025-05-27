fact(rainy).
fact(cloudy).

rule(wet_ground) :- fact(rainy).
rule(dark_sky) :- fact(cloudy).
rule(stay_home) :- rule(wet_ground).

% Backward chaining predicate
backward(X) :- fact(X).
backward(X) :- rule(X).
