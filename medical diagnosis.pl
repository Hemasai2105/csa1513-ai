disease(flu) :- fever, cough, body_pain.
disease(cold) :- sneezing, runny_nose.
disease(malaria) :- fever, chills, sweating.

symptom(fever).
symptom(cough).
symptom(body_pain).
symptom(sneezing).
symptom(runny_nose).
symptom(chills).
symptom(sweating).

ask_symptoms :- write('Enter symptoms using assert(symptom(X)).'), nl.

diagnose(Disease) :- disease(Disease), !.
