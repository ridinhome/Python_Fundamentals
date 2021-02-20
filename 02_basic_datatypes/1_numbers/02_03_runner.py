'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

run_distance = 10
run_time_mins = 30
run_time_sec = 30

total_mins = run_time_mins + (run_time_sec / 60)
speed = run_distance / total_mins
speed_mph = speed * 60
speed_kmh = speed_mph * 1.6
print ("The runners speed is: ",round(speed_kmh,1))


