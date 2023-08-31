from logic import *

rain = Symbol("rain") # Its is raining.
hagrid = Symbol("Hagrid") # Harry visited Hagrid.
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore.

knowledge = And(
    Impliction(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(model_check(knowledge, rain))
