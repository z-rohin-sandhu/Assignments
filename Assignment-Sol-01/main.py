# ------------------------------------ Student Enrollment System -----------------------------
from myfunctions import Student

print('\n ********************** STUDENT ENROLLMENT SYSTEM ****************************** \n')
print('\n ---------------------- Please Register Yourself First Before Getting Enrolled. ----------------------\n')

# Input to Register/Enrollment
check = input('Press `R` to Register. Press `E` to Enroll : \t')
Student.register_enroll_validation(check)
