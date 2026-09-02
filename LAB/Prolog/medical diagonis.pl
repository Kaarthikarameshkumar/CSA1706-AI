% Medical Diagnosis System

% Symptoms

symptom(fever).
symptom(cough).
symptom(cold).
symptom(headache).
symptom(body_pain).
symptom(sore_throat).
symptom(stomach_pain).
symptom(vomiting).
symptom(diarrhea).


% Diagnosis Rules

diagnosis(flu) :-
    symptom_present(fever),
    symptom_present(cough),
    symptom_present(body_pain).

diagnosis(common_cold) :-
    symptom_present(cold),
    symptom_present(cough),
    symptom_present(sore_throat).

diagnosis(migraine) :-
    symptom_present(headache),
    symptom_present(vomiting).

diagnosis(food_poisoning) :-
    symptom_present(stomach_pain),
    symptom_present(vomiting),

% Medical Diagnosis System

% Symptoms

symptom(fever).
symptom(cough).
symptom(cold).
symptom(headache).



symptom(body_pain).
symptom(sore_throat).
symptom(stomach_pain).
symptom(vomiting).
symptom(diarrhea).


% Diagnosis Rules

diagnosis(flu) :-
    symptom_present(fever),
    symptom_present(cough),
    symptom_present(body_pain).

diagnosis(common_cold) :-
    symptom_present(cold),
    symptom_present(cough),
    symptom_present(sore_throat).

diagnosis(migraine) :-
    symptom_present(headache),
    symptom_present(vomiting).

diagnosis(food_poisoning) :-
    symptom_present(stomach_pain),
    symptom_present(vomiting),
    symptom_present(diarrhea).


% Check whether symptom is present

symptom_present(Symptom) :-
    symptom_present(diarrhea).


% Check whether symptom is present

symptom_present(Symptom) :-
    symptom(Symptom).


% Start diagnosis

start :-
    write('Enter your symptoms:'), nl,
    write('Available symptoms:'), nl,
    write('fever, cough, cold, headache, body_pain,'), nl,
    write('sore_throat, stomach_pain, vomiting, diarrhea'), nl,
    nl,
    write('The possible diagnosis is:'), nl,
    diagnosis(Disease),
    write(Disease),
    nl.
