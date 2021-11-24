import re

with open('assests/potential-contacts.txt', 'r') as file:
    all_data = file.read()

def find_phones():    
    wanted = re.findall(r'[(]?[0-9]+[)]?-?[0-9]{3}-?[0-9]{4}',all_data)
    phones = []
    for number in wanted:
        if number[3] == '-':
            phones.append(number)
        if number[0] == '(':
            phones.append(number[1:4] + '-' + number[5:])
        if len(number) == 10:
            phones.append(number[0:3] + '-' + number[3:6] + '-' + number[6:])
            
    phones = sorted(phones)
    phones = list(dict.fromkeys(phones))    
    with open('phone_numbers.txt', 'w+') as file:
        for phone in phones:
            file.write(f'{phone}\n')

def find_emails():
    wanted_emails = re.findall(r'[\w.+-_]+@[\w-]+.\w+', all_data)
    wanted_emails = sorted(wanted_emails)
    with open('emails.txt','w+') as file:
        for email in wanted_emails:
            file.write(f'{email}\n')

find_phones()
find_emails()