
class student:

 def __init__(self, name, roll_number, cgpa):
   self.name = name
   self.roll_number = roll_number
   self.cgpa= cgpa


def sort_student(student_list):
  # sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                        key=lambda student:student.cgpa,
                         reverse=True)
  #syntax _ lambda arg:exp
  return sorted_students


#Example usage:
student = [
  student("stephen","A123",7.8),
  student("karthik","A124",8.9),
  student("santhosh","A125",9.1),
  student("komban","Ai26",9.9),
]

sorted_students = sort_student(student)

 # Print the sorted list of students
for students in sorted_students:
   print("Name;{},Roll number:{}.CGPA {}".format(students.name,
                            students.roll_number,
                  students.cgpa))                                 
