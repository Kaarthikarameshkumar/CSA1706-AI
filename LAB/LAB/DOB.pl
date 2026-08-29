person(john, dob(15, 5, 1995)).
person(alice, dob(22, 10, 1998)).
person(bob, dob(3, 1, 1990)).
person(emma, dob(12, 12, 2002)).
person(asha, dob(15, 15, 2004)).

get_dob(Name, DOB) :-
    person(Name, DOB).

born_in_year(Name, Year) :-
    person(Name, dob(_, _, Year)).

is_adult(Name) :-
    person(Name, dob(_, _, Year)),
    Year =< 2008.

display_all :-
    person(Name, dob(Day, Month, Year)),
    format('Name: ~w | DOB: ~w/~w/~w~n',
           [Name, Day, Month, Year]),
    fail.

display_all.
