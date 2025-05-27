bird(sparrow).
bird(penguin).
bird(eagle).

cannot_fly(penguin).

can_fly(Bird) :- 
    bird(Bird), 
    \+ cannot_fly(Bird).
