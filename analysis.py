import csv

APP = "Instagram"

# last7days = [95,120,80,140,60,170,110]
# counter = 0
# a = sum(last7days)
# print(a)
# print("Average daily activity for " + APP + ": " + str(a//7))

# with open("7days.csv", "w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(last7days)

minutes = []
with open("digital_behaviour.csv" , "r" ,encoding = "utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
                minutes.append(int(row['Instagram_Minutes']))

minutes = minutes[0:7]

# s = "A single piece of text"
# print(s[1::2] + s[0::2])

total = sum(minutes)

average = total // len(minutes)
highest = max(minutes)
lowest = min(minutes)

count = 0
for val in minutes:
        if val > average :
                count += 1

print(f"**REPORT OF LAST 7 DAYS SCREENTIME*** \nAPP : {APP}\nTotal Minutes : {total}\nAverage Minutes : {average}\nHighest Minutes :{highest}\nLowest Minutes : {lowest} \nAbove Average time Days : {count} ")