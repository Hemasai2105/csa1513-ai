diet(diabetes, 'Low sugar, high fiber diet').
diet(blood_pressure, 'Low salt, high potassium diet').
diet(obesity, 'Low calorie, high protein diet').

suggest_diet(Disease, Diet) :- 
    diet(Disease, Diet).
