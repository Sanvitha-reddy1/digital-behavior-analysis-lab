import numpy as np
import csv

insta_minutes = []
study_minutes = []

with open("digital_behaviour.csv","r" ,encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        insta_minutes.append(int(row["Instagram_Minutes"]))
        study_minutes.append(int(row["Study_Minutes"]))

insta_minutes = insta_minutes[:7]
study_minutes = study_minutes[:7]

instagram  = np.array(insta_minutes)
study = np.array(study_minutes)

total_insta = instagram.sum()
avg_insta = instagram.mean()
max_insta = instagram.max()
min_insta = instagram.min()
days_insta = len(instagram)

total_study = study.sum()
avg_study = study.mean()
max_study = study.max()
min_study = study.min()
days_study = len(study)

print(instagram[0],instagram[-1],instagram[2],)

print(instagram[:3], instagram[-2:],instagram[1:4])

print(instagram[::2])

hours_insta  = instagram/60
hours_study = study/60

hours_insta = hours_insta.round(2)
hours_study = hours_study.round(2)
#hours_study = np.round(study/60,2)

diff = study-instagram     #set diff in python sub in numpy

boolean = instagram > 100

greater = instagram[boolean]

count = boolean.sum()

print(count)

above_avg = instagram[instagram > avg_insta]
  
print(above_avg)
