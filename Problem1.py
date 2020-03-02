from pulp import *

Lp_prob = LpProblem("Exercise4", LpMinimize)

#Problem Variables
p1 = LpVariable("p1", lowBound = 15, upBound = 110)
p2 = LpVariable("p2", lowBound = 15, upBound = 110)
p3 = LpVariable("p3", lowBound = 15, upBound = 110)

s1 = LpVariable("s1", lowBound = 0, upBound = 60)
s2 = LpVariable("s2", lowBound = 0, upBound = 60)
s3 = LpVariable("s3", lowBound = 0, upBound = 60)

p12 = LpVariable("p12", lowBound = 0)
p13 = LpVariable("p13", lowBound = 0)
p23 = LpVariable("p23", lowBound = 0)

#Objective Function
Lp_prob += 600 * (p1 + p2 + p3) + 620 * (p12 + p23) + 640 * p13 + 660 * (s1 + s2 + s3)

#Constraints
Lp_prob += p1 + s1 >= 100
Lp_prob += p12 + p13 + p1 <= 110
Lp_prob += s1 <= 60

Lp_prob += p2 + s2 + p12 >= 130
Lp_prob += p23 + p2 <= 110
Lp_prob += s2 <= 60

Lp_prob += p3 + s3 + p23 + p13 >= 150

print(Lp_prob)

status = Lp_prob.solve()
print(LpStatus[status])

for v in Lp_prob.variables():
    print(v.name, "=", v.varValue)

print("Total Cost of Production = ", value(Lp_prob.objective))