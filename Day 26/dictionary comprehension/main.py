# Day 26 - dictionary comprehension exercise

# exercise 1

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
result = {word:len(word) for word in sentence.split()}


print(result)

# exercise 2

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}


print(weather_f)


