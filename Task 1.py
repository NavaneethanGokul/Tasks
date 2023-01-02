# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 23:06:28 2023

@author: Navaneethan.S
"""

import re
import json
import os

print('Welcome to Slambook!')
#Print('The next biggest Social media that is going to rule the world!')
print('Please select one from the below options')
print('\n1. Register \n2. Login\n')

def registration():
#Criteria:
    #Email should have @ follwed by '.' but not in the immediate position
    #Email should not start with special characters and numbers
    #Password length should be between 5 and 16(both inclusive)
    #Must have minimum one special character, one digit, one uppercase, one lowercase
    
    
    r_mail_id = input('Enter your mail ID: ')
    r_password = input('Enter your password: ')
    
    
    regex_mail_id = '[A-Za-z]+\S+@\w+.com'
    regex_password = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$'
    
    v_mail_id = re.findall(regex_mail_id, r_mail_id)
    v_password = re.findall(regex_password, r_password)    

    credentials_keys = ['Name','Password']
    credential_values = []

    if len(v_mail_id) != 0 and len(v_password) != 0:
        credential_values.extend((r_mail_id,r_password))
        zip_data = zip(credentials_keys,credential_values)
        credentials = dict(zip_data)
        store(credentials)                             
        print('\nSuccessfully registered!')
        print('\nProceed to the Login page.')
        print('\n')
        login()
    
    else:
        print('\nCredentials doesn\'t match the below criteria.\n1. Email should have @ follwed by . but not in the immediate position\n2. Email should not start with special characters and numbers\n3. Password length should be between 5 and 16(both inclusive)\n4. Must have minimum one special character, one digit, one uppercase, one lowercase')
        print('\n')
        registration()
    
    return ''

def login():
    print('Provide your credentials below to login')
    l_mail_id = input('Enter your mail ID: ')
    l_password = input('Enter your password: ')

    fname = 'db_credentials.json'
    with open(fname, 'r') as cred_file:
        data = json.load(cred_file)
        count = False
        for i in data:
            if l_mail_id in i['Name'] and l_password in i['Password']:
                count = True
            else:
                pass
        if count:
            print('\nLogin Sucessful!')
        else:
            print('\nInvalid credentials. Or the account doesn\'t exists.\n\nPlease select one from the below option.\n1. Register\n2. Forgotten Password')
            user_selection = int(input('\n'))
            if user_selection == 1:
                print('\n')
                print(registration())
            else:
                print('\n')
                print(forgotten_password())                
    return ''

def forgotten_password():
    f_mail_id = input('Enter the mail ID to retrieve the password: ')
    fname = 'db_credentials.json'
    retrieved_pwd = []
    with open(fname, 'r') as cred_file:
        data = json.load(cred_file)
        for i in data:
            if i['Name'] == f_mail_id:
                retrieved_pwd.append(i['Password'])
            else:
                pass
    if len(retrieved_pwd) != 0:
        print('The password is: '+''.join(retrieved_pwd))
        print('\nProceed to the Login page.')
        print('\n')
        login()
    else:
        print('The account doesn\'t exist. Proceed to Registration')
        print('Create an account by providing your credentials below.')
        registration()

    return ''

def store(credentials):

    fname = 'db_credentials.json'
    if os.path.isfile(fname):
        with open(fname,'a+') as cred_file:
            cred_file.seek(0, 2) # Go to the end of file
            cred_file.seek(cred_file.tell()-1, os.SEEK_SET) # Go backwards 1 character
            cred_file.truncate()
            cred_file.write(',')
            json.dump(credentials, cred_file)
            cred_file.write(']')
    else:        
        with open(fname,'w') as cred_file:
            data= []
            data.append(credentials)
            json.dump(data, cred_file)
            
    return ''

user_selection = int(input())

if user_selection == 1:
    print('\n')
    print(registration())
else:
    print('\n')
    print(login())