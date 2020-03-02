from pulp import *
from math import ceil
problem5 = LpProblem("problem5", LpMinimize)

##hours expected to reach each month
monthly_hours = [6000, 7000, 8000, 9500, 11000]

##lower bound is represented by the demand per moth divided by the hours worked by each consultant

low_bounds = [ceil(x/160) for x in monthly_hours]

print(ceil(low_bounds[0]))
print(ceil(low_bounds[1]))
print(ceil(low_bounds[2]))
print(ceil(low_bounds[3]))

cons_per_month=[]
cons_per_month.append( LpVariable("cons_month1", lowBound = low_bounds[0], cat= LpInteger) )
cons_per_month.append( LpVariable("cons_month2", lowBound = low_bounds[1], cat= LpInteger) )
cons_per_month.append( LpVariable("cons_month3", lowBound = low_bounds[2], cat= LpInteger) )
cons_per_month.append( LpVariable("cons_month4", lowBound = low_bounds[3], cat= LpInteger) )

#number of trainees per month
trainees_per_month = []
trainees_per_month.append(LpVariable("train_month1", lowBound= 0, cat=LpInteger))
trainees_per_month.append(LpVariable("train_month2", lowBound= 0, cat=LpInteger))
trainees_per_month.append(LpVariable("train_month3", lowBound= 0, cat=LpInteger))
trainees_per_month.append(LpVariable("train_month4", lowBound= 0, cat=LpInteger))

##first month a trainee earns 1000 then 2000 each month
##first month earns 9000,second 7000,third 5000 ,fourth 3000

problem5 += 9000 * trainees_per_month[0] + 7000 * trainees_per_month[1] + 5000 * trainees_per_month[2] + 3000 * trainees_per_month[3]

##first
##in the first month we have the wrk hours of free consultants + wrk hours of trainers must be greater or equal than the required hours
problem5 += (cons_per_month[0]-trainees_per_month[0]) * 160 + trainees_per_month[0] * 110 >= 6000

##consultants must be fewer or equal than 50
problem5 += cons_per_month[0] <= 50

##second
##the wrk hours of free consultants + wrk hours of trainers must be greater or equal than the required hours
problem5 += (cons_per_month[1]-trainees_per_month[1]) * 160 + trainees_per_month[1] * 110 >= 7000
##consultants should be fewer than or same as the consultants from prev month and trained consultants
problem5 += cons_per_month[1] <= cons_per_month[0] + trainees_per_month[0]

##third
##the wrk hours of free consultants + wrk hours of trainers must be greater or equal than the required hours
problem5 += (cons_per_month[2]-trainees_per_month[2]) * 160 + trainees_per_month[2] * 110 >= 8000
##consultants should be fewer than or same as the consultants from prev month and trained consultants
problem5 += cons_per_month[2] <= cons_per_month[1] + trainees_per_month[1]

##fourth
##the wrk hours of free consultants + wrk hours of trainers must be greater or equal than the required hours
problem5 += (cons_per_month[3]-trainees_per_month[3]) * 160 + trainees_per_month[3] * 110 >= 9500
##consultants should be fewer than or same as the consultants from prev month and trained consultants
problem5 += cons_per_month[3] <= cons_per_month[2] + trainees_per_month[2]


##fifth
##total number of consultants wrk hrs:
## the 50 consultants + the trained consultants from the first four months(from which 5% leave) multiplied by wrk hours of a consultant(160)
problem5 += (50 + (trainees_per_month[0] + trainees_per_month[1] + trainees_per_month[2] + trainees_per_month[3]) * 0.95) * 160 >= 11000


problem5.solve()

print("The min cost for getting the new trainees is = {0} euros".format(problem5.objective.value()))
print("The minimum total cost (including consultants) for the 5 months is 90000 (cost for trainees) + 500000 (cost for consultants) = 590000 euros")