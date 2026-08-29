% Base case
sum(1, 1).

% Recursive case
sum(N, S) :-
    N > 1,
    N1 is N - 1,
    sum(N1, S1),
    S is S1 + N.
