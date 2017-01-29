import smtplib

def sendmail():
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('xxxx@gmail.com', 'xxxxxxxxxxxxxxxxxxx')
    smtpObj.sendmail('xxxx@gmail.com', '5595551234@vtext.com', msg_list)
    smtpObj.quit()

msg = "-=Shopping list items=-\n"
list = []

def menu():
    print('A)dd item')
    print('V)iew list')
    print('S)end list')
    print('Q)uit')
    global action
    action = input('> ').lower()

menu()
while True:
    if action == 'a':
        print('Please enter items')
        print('Preass Q when done')
        adding = True
        while adding == True:
            item = input('> ').lower()
            if item == "q":
                adding = False
            else:
                list.append(item)

    if action == 'v':
        print(list)

    if action == 's':
        my_list = ' '.join(list)
        msg_list = str (msg + my_list)
        sendmail()
        print('Shopping list sent...')

    if action == 'q':
        raise SystemExit

    else:
        menu()
