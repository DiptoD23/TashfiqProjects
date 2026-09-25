import random

hot_limit = 30
cold_limit = 15


temperatures = [random.randint(5, 40) for _ in range(30)]

avg_temp = sum(temperatures) / len(temperatures)
max_temp = max(temperatures)
min_temp = min(temperatures)

hottest_day = temperatures.index(max_temp) + 1

above_avg = [temp for temp in temperatures if temp > avg_temp]

hot_days = 0
normal_days = 0
cold_days = 0

current_hot_streak = 0
max_hot_streak = 0

for temp in temperatures:
    if temp > hot_limit:
        hot_days += 1
        current_hot_streak += 1
        max_hot_streak = max(max_hot_streak, current_hot_streak)
    else:
        current_hot_streak = 0
        if temp < cold_limit:
            cold_days += 1
        else:
            normal_days += 1

print("\nProblem-5")
print("\n30-Day temperature analysis")
print(f"Daily temperatures: \n{temperatures}\n")
print(f"Average temperature: {avg_temp:.2f}°C")
print(f"Highest temperature: {max_temp}°C (Day {hottest_day})")
print(f"Lowest temperature:  {min_temp}°C")
print(f"\nTemperatures above average ({avg_temp:.2f}°C): {above_avg}")
print("\nCategory counts:")
print(f"  - Hot days (> {hot_limit}°C): {hot_days}")
print(f"  - Normal days ({cold_limit}°C - {hot_limit}°C): {normal_days}")
print(f"  - Cold days (< {cold_limit}°C): {cold_days}")
print(f"\nLongest consecutive cequence of hot days: {max_hot_streak} day(s)")