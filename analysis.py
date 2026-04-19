import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sleep_data.csv")

df["Sleep Disorder"] = df["Sleep Disorder"].fillna("None")

df.columns = df.columns.str.replace(" ", "_")

print("----- MISSING DATA CHECK -----")
print(df.isnull().sum())

avg_sleep = df.groupby("Stress_Level")["Sleep_Duration"].mean()

print("\n----- AVERAGE SLEEP DURATION BY STRESS LEVEL -----")
print(avg_sleep)

correlation_sleep = df["Stress_Level"].corr(df["Sleep_Duration"])

print("\n----- CORRELATION (SLEEP DURATION) -----")
print("Stress vs Sleep Duration:", round(correlation_sleep, 3))

min_stress_sleep = avg_sleep.loc[avg_sleep.index.min()]
max_stress_sleep = avg_sleep.loc[avg_sleep.index.max()]

percent_decrease_sleep = ((min_stress_sleep - max_stress_sleep) / min_stress_sleep) * 100

print("\n----- PERCENT CHANGE (SLEEP DURATION) -----")
print("From lowest to highest stress level, sleep duration decreased by:",
      round(percent_decrease_sleep, 2), "%")

plt.figure(figsize=(8, 5))
avg_sleep.plot(kind="line", marker="o")

plt.title("Stress Level vs Average Sleep Duration")
plt.xlabel("Stress Level")
plt.ylabel("Average Sleep Duration (Hours)")
plt.grid(True)

plt.savefig("outputs/sleep_duration.png")  # ✅ DÜZELTİLDİ
plt.show()

avg_quality = df.groupby("Stress_Level")["Quality_of_Sleep"].mean()

print("\n----- AVERAGE SLEEP QUALITY BY STRESS LEVEL -----")
print(avg_quality)

correlation_quality = df["Stress_Level"].corr(df["Quality_of_Sleep"])

print("\n----- CORRELATION (SLEEP QUALITY) -----")
print("Stress vs Sleep Quality:", round(correlation_quality, 3))

min_stress_quality = avg_quality.loc[avg_quality.index.min()]
max_stress_quality = avg_quality.loc[avg_quality.index.max()]

percent_decrease_quality = ((min_stress_quality - max_stress_quality) / min_stress_quality) * 100

print("\n----- PERCENT CHANGE (SLEEP QUALITY) -----")
print("From lowest to highest stress level, sleep quality decreased by:",
      round(percent_decrease_quality, 2), "%")


plt.figure(figsize=(8, 5))
avg_quality.plot(kind="line", marker="o")

plt.title("Stress Level vs Average Sleep Quality")
plt.xlabel("Stress Level")
plt.ylabel("Average Sleep Quality")
plt.grid(True)

plt.savefig("outputs/sleep_quality.png")  
plt.show()