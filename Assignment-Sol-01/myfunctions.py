# -------------------------------- Class To Register & Enroll Students -------------------------
from input_validations import Validation

class Student:
    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email

    def register_enroll_validation(check):
        if check == 'R' or check == 'r':
            Student.register()
        elif check == 'E' or check == 'e':
            Student.enroll()
        else:
            print('Invalid Input')
            check = input('Press `R` to Register. Press `E` to Enroll : \t')
            Student.register_enroll_validation(check)

    def register():
        print('\n \n --------------------------------- Registration Form ------------------------ \n \n')

        # Inputs for Registration Form
        name = Validation.name()
        phone = Validation.phone()
        email = Validation.email()

        student_detail = Student(name, phone, email)
        details = str(student_detail.__dict__.values())[12:-1].split(',')
        usr_mail = details[2][2:-2]

        # Saving Credentials in Text Files
        with open('credentials.txt', mode='a') as cred:
            cred.write(f'{vars(student_detail)}\n')

        with open('mail_list.txt', mode='a') as mail:
            mail.write(f'{usr_mail}\n')

        print('------------ Registration Successful -------------------')

        # Calling Enroll Function To Enroll Student
        consent = Validation.consent()
        Student.enroll() if consent == 'y' or consent == 'Y' else exit()

    def enroll():
        print('\n \n ------------------ Enrollment Form ----------------------------------- \n \n')

        # Inputs for Enrollment Form
        email = Validation.email()
        disabled = Validation.disabled()

        with open('mail_list.txt', mode='r') as mail:
            mail_list = mail.read().split('\n')

        if email not in mail_list:
            print('You Are Not Registered Yet. Please Register Yourself First.')
            Student.register()
        else:
            Student.result(email, disabled)

    def result(email, disabled):
        subject = Validation.subject()
        with open('capacity.txt', mode='r') as cap:
            lmt = cap.read().split('-')
            m, b, c = int(lmt[0]), int(lmt[1]), int(lmt[2])
            h_res = 3
            if disabled == 'N' or disabled == 'n':
                if subject == 'Math' and m-h_res > 0:
                    Student.success(email, disabled, subject, m - 1, b, c)
                elif subject == 'Bio' and b-h_res > 0:
                    Student.success(email, disabled, subject, m, b - 1, c)
                elif subject == 'Commerce' and c-h_res > 0:
                    Student.success(email, disabled, subject, m, b, c - 1)
                else:
                    Student.board(subject, m, b, c)
            else:
                if subject == 'Math' and m > 0:
                    Student.success(email, disabled, subject, m - 1, b, c)
                elif subject == 'Bio' and b > 0:
                    Student.success(email, disabled, subject, m, b - 1, c)
                elif subject == 'Commerce' and c > 0:
                    Student.success(email, disabled, subject, m, b, c - 1)
                else:
                    Student.board(subject, m, b, c)

    def success(email, disabled, subject, m, b, c):
        with open('enrolled_list.txt', mode='a') as enroll:
            enroll.write(f'{email}/{disabled}/{subject}\n')
        print(f'\n Enrollment Success. \n Email Id : \t {email} \n Subject : \t{subject}')

        with open('capacity.txt', mode='w') as cap:
            cap.write(f'{m}-{b}-{c}\n')
        exit()

    def board(subject, m, b, c):
        print(f'\n \n ---------- Capacity Board --------------- \n \n'
              f'* \t Math : {m}/30 \t ** \t Bio :  {b}/30  *** \t Commerce :  {c} '
              f'\n --> 10% Seats are Reserved for Handicaps.\n'
              f'-------------------------------------- \n'
              f'\n Seats for {subject} is already filled. Please Enroll in other Subject.')
        exit()