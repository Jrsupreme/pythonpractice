#Create a dictionary to store information about 3 students (name, age, grade)
#Print each student information in readable format
#include the dictionaries within script

# #student_info = {
#     "Name" : "Jaiden", "Maira", "Selena",
#     "Grade" : ["11th", "12th", "9th"],
#     "Age" : [16, 17, 15]
# }
students = { #went with nested dictionaries isntead so that we can access specific info about specific students example print(student_info["student_1"]["name"])
    "student_1": {
        "name": "Jayden",
        "grade": "12th",
        "age": 17
    },

    "student_2": {
        "name": "Maira",
        "grade": "11th",
        "age": 16    
    },

    "student_3": {
        "name": "Selena",
        "grade": "10th",
        "age": 15
    }
}

#for student_no, student_info in students.items(): #iterating through the main dictionary keys and values. .items() allows us to iterate through both keys and values of the dictionaries.
   # print(f"Details of {student_no}") #printing the keys only aka dictionary names.
    # for keys, values in student_info.items(): #iterating through the sub-dictionaries keys and values.
      #  print(f"{keys} : {values}") #printing the keys and values for each of the students dictionaries

#or

for student_no, student_info in students.items():
    print(f" Name: {student_info['name']} Grade: {student_info['grade']} Age: {student_info['age']}" )