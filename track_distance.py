

import sys

print()
print()

print('\U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f')

print()
print("This is an app for runners who want to know the total distance they ran in miles and/or kilometers.")
print() 
print("Enter the lane you ran in and the total number of laps you ran.")
print()
print("You will get the calculation for the distance in yards and miles, and meters with kilometers.")
print()
print("Each lane is a different distance, lane 1 is shorter than lane 2, and lane 8 is much longer than lane 1 and a little longer than lane 7.")
print()
print("So if you stayed in the same lane or changed lanes, you can get an accurate total of the distance you completed.")
print()

def runner_input():
  while True:
    try:
      lane_num = int(input("Which lane did you run in on the track?  Enter 1-8:  "))
      print()
    except ValueError:
      print("That's not a number.")
    else:
      if 1 <= lane_num < 9:
        break
      else:
        print("Number entered not between 1-8.")
  num_of_laps = float(input("How many laps did you complete?  Enter the number (2, 5, 20, whatever you ran)? If you ran 1/4 lap enter .25, 1/2 lap enter .50, 3/4 lap enter .75:  "))
  print()



  total_yards = 0
  total_miles = 0
  total_meters = 0
  total_kilometers = 0

  if lane_num == 1:
    total_yards += (440 * num_of_laps)
    total_meters += (402.36 * num_of_laps)
  elif lane_num == 2:
    total_yards += (446 * num_of_laps)
    total_meters += (407.67 * num_of_laps)
  elif lane_num == 3:
    total_yards += (454 * num_of_laps)
    total_meters += (415.33 * num_of_laps)
  elif lane_num == 4:
    total_yards += (463 * num_of_laps)
    total_meters += (423 * num_of_laps)
  elif lane_num == 5:
    total_yards += (471 * num_of_laps)
    total_meters += (430.66 * num_of_laps)
  elif lane_num == 6:
    total_yards += (474 * num_of_laps)
    total_meters += (433.38 * num_of_laps)
  elif lane_num == 7:
    total_yards += (488 * num_of_laps)
    total_meters += (446 * num_of_laps)
  elif lane_num == 8:
    total_yards += (496 * num_of_laps)
    total_meters += (453.66 * num_of_laps)
  else:
    print("You must be watching Youtube and did not go running.")

  total_miles  = total_yards / 1760
  total_kilometers = total_meters / 1000
  print()
  print("You ran a total of %s yards which is %.2f miles, and %.2f total meters which is %.2f total kilometers." % (total_yards, total_miles, total_meters, total_kilometers))
  if total_miles > 5:
    print("nice run.")
    print('\U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f')
  
  print()
  while True:
     lane_change = input("Did you change into another lane?, enter Y or N: ")
     lane_change = lane_change.upper()
     if lane_change == "N":
         print("Nice run.")
         sys.exit()
     elif lane_change == "Y":
         try:
             lane_num_more = int(input("Which other lane did you run in on the track?  Enter 1-8:  "))
         except ValueError:
             print("That's not a number.")
         else:
             if 1 <= lane_num < 9:
                 break
             else:
               print("Number entered not between 1-8.")
  num_of_laps_two = float(input("How many laps did you complete?  Enter the number (2, 5, 20, whatever you ran)? If you ran 1/4 lap enter .25, 1/2 lap enter .50, 3/4 lap enter .75: "))

  total_yards_two = 0
  total_miles_two = 0
  total_meters_two = 0
  total_kilometers_two = 0

  if lane_num == 1:
    total_yards_two += (440 * num_of_laps_two)
    total_meters_two += (402.36 * num_of_laps_two)
  elif lane_num == 2:
    total_yards_two += (446 * num_of_laps_two)
    total_meters_two += (407.67 * num_of_laps)
  elif lane_num == 3:
    total_yards_two += (454 * num_of_laps_two)
    total_meters_two += (415.33 * num_of_laps)
  elif lane_num == 4:
    total_yards_two += (463 * num_of_laps_two)
    total_meters_two += (423 * num_of_laps_two)
  elif lane_num == 5:
    total_yards_two += (471 * num_of_laps_two)
    total_meters_two += (430.66 * num_of_laps_two)
  elif lane_num == 6:
    total_yards_two += (474 * num_of_laps_two)
    total_meters_two += (433.38 * num_of_laps_two)
  elif lane_num == 7:
    total_yards_two += (488 * num_of_laps_two)
    total_meters_two += (446 * num_of_laps_two)
  elif lane_num == 8:
    total_yards_two += (496 * num_of_laps_two)
    total_meters_two += (453.66 * num_of_laps_two)
  else:
    print("You must be watching Youtube and did not go running.")

  print("Ok, now we'll add both lane distances together to get the combined total distance you ran today.")

  total_miles  = total_yards / 1760
  total_kilometers = total_meters / 1000
  print()
  total_miles_two = total_yards_two / 1760
  total_kilometers_two = total_meters_two / 1000
  print()
  overall_total_miles = total_miles + total_miles_two
  overall_total_kilometers = total_kilometers + total_kilometers_two

  print("For the lane change you ran a total of %s yards which is %.2f miles, and %.2f total meters which is %.2f total kilometers." % (total_yards_two, total_miles_two, total_meters_two, total_kilometers_two))
  print()
  print("And your overall combined total was {:.2f} miles and {:.2f} kilometers.".format(overall_total_miles, overall_total_kilometers))
  if overall_total_miles > 5 and overall_total_miles < 10:
      print("nice run.")
      print('\U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f')
  elif overall_total_miles >= 10:
      print("Wow, crushed it.")
      print()
  print('\U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f \U0001f3c3\u200d\u2640\ufe0f \U0001f3c3\U0001f3ff\u200d\u2640\ufe0f')


runner_input()