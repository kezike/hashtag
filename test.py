#!/usr/bin/python

import model

#model.addPerson("uche", "uche", "uche", "ofuonye")
#model.addMatch(1,2)
# model.addPerson("uche", "uche", "uche", "ofuonye", "mentor")
# model.addPerson("kayode", "kayode", "kayode", "Ezike", "mentor")
# model.addPerson("ed", "ed", "ed", "ed", "mentor")
# model.addPerson("eric", "eric", "eric", "eric", "mentor")
# model.addPerson("john", "john", "john", "john", "mentee")

# model.addDescription(1, "Hi, my name is Kayode", "high", "ML", "christ", "african", "teen", "male", "bach")
# model.addDescription(2, "Hi, my name is Kayode", "high", "ML", "christ", "african", "teen", "male", "bach")
# model.addDescription(3, "Hi, my name is Kayode", "high", "ML", "christ", "african", "teen", "male", "bach")
# model.addDescription(4, "Hi, my name is Kayode", "high", "ML", "christ", "african", "teen", "male", "bach")
# model.addDescription(5, "Hi, my name is Kayode", "high", "AI", "christ", "african", "teen", "male", "bach")

mentors = model.getMentors("teen", "male", "christ", "african", "high","bach", "ML")
print mentors
