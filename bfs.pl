% Define the graph using edge/2
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, d).
edge(d, e).

% Breadth First Search Algorithm
bfs([[Goal|Path] | _], Goal, [Goal|Path]).
bfs([[Node|Path] | Rest], Goal, Result) :-
    findall([Next, Node|Path],
        (edge(Node, Next), \+ member(Next, [Node|Path])),
        NextPaths),
    append(Rest, NextPaths, NewQueue),
    bfs(NewQueue, Goal, Result).

% Wrapper to reverse the result path
best_first_search(Start, Goal, Path) :-
    bfs([[Start]], Goal, RevPath),
    reverse(RevPath, Path).
