import csv

file = open('output.csv', 'w')
writer = csv.writer(file)

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
    writer.writerow(['Starting Time', 'Ending Time', 'Amount'])
    writer.writerow([x, y, fr])