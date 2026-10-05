import pandas as pd
 
import matplotlib 

matplotlib.use("Agg")

import matplotlib.pyplot as plt

plt.figure(figsize = (16,8))

df = pd.read_csv("Digital_behaviour.csv")

df["Total_screen_time"] = df["Instagram_Minutes"] + df["YouTube_Minutes"] + df["WhatsApp_Minutes"] + df["LinkedIn_Minutes"]

df["Day_label"] = [f"day {i+1}" for i in range(len(df))]

plt.bar(df["Day_label"] , df["Total_screen_time"] , color = "blue")

plt.title("Total Screen Time Per Day")

plt.xlabel("Days")
plt.ylabel("Total screen time(minutes)")

plt.xticks(rotation = 45)
plt.tight_layout()

plt.savefig("charts/total_screen_time.png")

plt.close()
# plt.show()

plt.Figure(figsize = (20,8))

plt.plot(df['Day_label'] , df['Total_screen_time'] , marker = 'o' , label = 'Total Screen Time' , color = 'b')
plt.title("Total Screen Time Per Day")

plt.xlabel("Days")
plt.ylabel("Total screen time(minutes)")

plt.xticks(rotation = 45)

plt.tight_layout()
plt.savefig("charts/plot.png")

plt.close()

plt.Figure(figsize = (20,8))

app_totals = {
   "Instagram" : df["Instagram_Minutes"].sum() , "Whatsapp" : df["WhatsApp_Minutes"].sum() , "YouTube" : df["YouTube_Minutes"].sum() , "LinkedIn" : df["LinkedIn_Minutes"].sum()
}

plt.pie(app_totals.values() , labels = app_totals.keys() , autopct = '%1.1f%%' , startangle=90)

plt.title("Total Screen Time Per Day")

plt.savefig("charts/piechart.png")
