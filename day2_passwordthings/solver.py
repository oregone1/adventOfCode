f = open('day2_passwordthings/passwords_in', 'r')
#w = open('day2_passwordthings/passwords_out', 'w') # this is bad i know

counter = 1

passwords = f.read()

for password in passwords.split(':'):
    #print(password)
    #w.write(password + '\n')
