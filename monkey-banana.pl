% Define valid positions
position(at_door).
position(at_window).
position(middle).

% Possible actions (move/3)
move(state(middle, on_box, middle, has_not), grasp, state(middle, on_box, middle, has)).

move(state(P, on_floor, P, has_not), climb, state(P, on_box, P, has_not)).

move(state(P1, on_floor, P1, has_not), push(P1, P2), state(P2, on_floor, P2, has_not)) :-
    position(P1), position(P2), P1 \= P2.

move(state(P1, on_floor, B, has_not), walk(P1, P2), state(P2, on_floor, B, has_not)) :-
    position(P1), position(P2), P1 \= P2.

% Goal state detection
can_get_banana(State) :-
    can_get_banana(State, []).

% Final success state
can_get_banana(state(_, _, _, has), _) :- 
    write('Banana reached!'), nl.

% Recursive rule with visited-state checking
can_get_banana(State, Visited) :-
    \+ member(State, Visited),
    move(State, Action, NewState),
    write('Action: '), write(Action), nl,
    can_get_banana(NewState, [State|Visited]).
