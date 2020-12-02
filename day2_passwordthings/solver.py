import os

f = open(os.path.realpath('adventOfCode/day2_passwordthings/passwords_in'), 'r')

passwords = f.read()
checker = []
counter = 1


for password in passwords.split(':'):
	#print(password.split('\n'))
	if '-' in password:
		checker.append(password)
	else:
		checker.append(password)

	counter += 1

	if counter > 2:
		print(checker[0], checker[1])
		numbers = str(checker[0]).split('-')
		min_int = numbers[0]
		max_int = numbers[1]
		print(min_int, max_int)
	#w.write(password + '\n')
