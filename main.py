import csv
from datetime import date
import math

print('Enter start time (Format hh:mm in 24hrs):')
x = input()

print ("Enter end time (Format hh:mm in 24hrs): ")
y = input()

if x and y:
    fx = int(x.split(":")[0])
    fy = int(y.split(":")[0])
    sx = int(x.split(":")[1])
    sy = int(y.split(":")[1])
    f = fy-fx
    s = max(sx, sy) - min(sx, sy) * 0.834
    fr = f * 5 + s
    print("You earned $"+str(math.trunc(round(fr, 0)))+" for tutoring for "+str(math.trunc(round(f, 0)))+" hours and "+str(math.trunc(round(s, 0)))+" minutes")
    List = [x, y, date.today(), fr]
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('output.csv', 'a') as f_object:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = csv.writer(f_object)

        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(List)

        # Close the file object
        f_object.close()