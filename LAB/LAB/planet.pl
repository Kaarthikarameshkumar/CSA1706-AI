% ==========================================
%           PLANETS DATABASE
% ==========================================

% planet(Name, Type, DistanceFromSun, NumberOfMoons).

planet(mercury, terrestrial, 57.9, 0).
planet(venus, terrestrial, 108.2, 0).
planet(earth, terrestrial, 149.6, 1).
planet(mars, terrestrial, 227.9, 2).
planet(jupiter, gas_giant, 778.5, 95).
planet(saturn, gas_giant, 1434.0, 146).
planet(uranus, ice_giant, 2871.0, 28).
planet(neptune, ice_giant, 4495.0, 16).

% ==========================================
%              RULES
% ==========================================

% Find all terrestrial planets
terrestrial_planet(Name) :-
    planet(Name, terrestrial, _, _).

% Find all gas giant planets
gas_giant_planet(Name) :-
    planet(Name, gas_giant, _, _).

% Find all ice giant planets
ice_giant_planet(Name) :-
    planet(Name, ice_giant, _, _).

% Find planets having moons
has_moons(Name) :-
    planet(Name, _, _, Moons),
    Moons > 0.

% Find planets with no moons
no_moons(Name) :-
    planet(Name, _, _, 0).

% Find planets farther than Earth from the Sun
farther_than_earth(Name) :-
    planet(Name, _, Distance, _),
    Distance > 149.6.

% Display complete details of a planet
show_planet(Name) :-
    planet(Name, Type, Distance, Moons),
    write('Planet Name       : '), write(Name), nl,
    write('Planet Type       : '), write(Type), nl,
    write('Distance from Sun : '), write(Distance),
    write(' million km'), nl,
    write('Number of Moons   : '), write(Moons), nl.
