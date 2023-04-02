# ------------------ Functions To Validate User Inputs ---------------------------
import re
# Regex Code to Validate Inputs
reg_name = '[A-Za-z]{2,25}\\s[A-Za-z]{2,25}'
reg_phone = '^\\+?[1-9][0-9]{7,14}$'
reg_mail = '^[a-z0-9]+[\\.]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$'

# Class To Take & Validate Inputs Taken
class Validation:

    def name():
        name = input('Please Enter Your Name (Format : F_Name L_Name, Type None if L_name is not Applicable) : \t')
        if re.match(reg_name, name):
            return name
        else:
            Validation.input_fail()

    def phone():
        phone = input('Please Enter Your Phone No. : \t')
        if re.match(reg_phone, phone):
            return phone
        else:
            Validation.input_fail()

    def email():
        email = input('Please Enter Your Email : \t')
        with open('mail_list.txt', mode='r') as mail:
            mail_list = mail.read().split('\n')

        if email in mail_list:
            print('User Already Registered . Please Follow Further Instructions.')

        if re.match(reg_mail, email):
            return email
        else:
            Validation.input_fail()

    def disabled():
        disabled = input('Are You Handicap? N : NO, Y : YES : \t')
        if disabled == 'Y' or disabled == 'y' or disabled == 'N' or disabled == 'n':
            return disabled
        else:
            Validation.input_fail()

    def consent():
        consent = input('Are You Handicap? N : NO, Y : YES : \t')
        if consent == 'Y' or consent == 'y' or consent == 'N' or consent == 'n':
            return consent
        else:
            Validation.input_fail()

    def subject():
        subject = input('\n Enter the Subject Code in which You want to Enroll. '
                        '\t Math -->M \t Bio --> B \t Commerce -->C :\t ')

        if subject == 'M' or subject == 'm':
            return 'Math'
        elif subject == 'B' or subject == 'b':
            return 'Bio'
        elif subject == 'C' or subject == 'c':
            return 'Commerce'
        else:
            Validation.input_fail()

    @staticmethod
    def input_fail():
        print('Invalid Input, Please Reload the Code to Restart Process.')
        exit()
