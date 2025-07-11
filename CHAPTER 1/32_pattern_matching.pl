match(X, [X|_]).
match(X, [_|T]) :- match(X, T).