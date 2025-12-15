# with open("file1.txt") as file: numbers1 = [int(number.replace("\n","")) for number in file.readlines()]
# with open("file2.txt") as file: numbers2 = [int(number.replace("\n","")) for number in file.readlines()]
#
# result = [n for n in numbers1 if n in numbers2]
#
# print(result)



# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {item:len(item) for item in sentence.split()}
# print(result)



# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f = {day:(temp*9/5)+32 for (day, temp) in weather_c.items()}
#
# print(weather_f)

students_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# looping through dictionaries:
# for (key, value) in students_dict.items():
#     print(value)

import pandas

students_data_frame = pandas.DataFrame(students_dict)
# print(students_data_frame)

# # loop through a data frame
# for (key, value) in students_data_frame.items():
#      print(key)

# loop through rows of a data frame
for (index, row) in students_data_frame.iterrows():
    print(row[0], row[1])
    print(row.student)
    print(row.score)
    print(row.student, row.score)