#!/usr/bin/python

def defineWorkout():
  try:
    n_sets = int(input("Number of sets [5]: "))
  except ValueError:
    n_sets = 5
  try:
    rest_between_sets = int(input("Rest between sets [30]: "))
  except ValueError:
    rest_between_sets = 30
  try:
    n_exercises = int(input("Number of exercises [6]: "))
  except ValueError:
    n_exercises= 6
  try:
    rest_between_exercises = int(input("Rest between exercises [120]: "))
  except ValueError:
    rest_between_exercises = 120
  return([n_sets, rest_between_sets, n_exercises, rest_between_exercises])

import time
def takeBreak(t):
  while t > 0:
    print(t)
    t -= 1
    time.sleep(1)

def runTimer(parms):
  n_sets = parms[0]
  rest_sets = parms[1]
  n_exercises = parms[2]
  rest_exercises = parms[3]
  for x in range(n_exercises):
    print("\nStarting exercise number " + str(x + 1) + " of " + str(n_exercises))
    for s in range(n_sets - 1):
      print("Start set number " + str(s + 1))
      input("Press enter to rest from set number " + str(s + 1) + " of " + str(n_sets))
      takeBreak(rest_sets)
    if x < n_exercises - 1:
      input("\nDONE! Press enter to rest from this exercise")
      takeBreak(rest_exercises)
    else:
      print("Workout finished. Well done!")

# Execution
parms = defineWorkout()
runTimer(parms)
