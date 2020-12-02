import os

f = open(os.path.realpath('adventOfCode/day2_passwordthings/passwords_in'), 'r')

passwords = f.read()
valid_pass = []
x = 0

def format_passwords(password):
		counter = 0
		password = password.split(':')
		passwordnum = password[0].split('-')
		checkletter = passwordnum[1].split(' ')[1]

		print(passwordnum[0], passwordnum[1].split(' ')[0])
		print(password[1])

		for letter in password[1]:
			if letter == checkletter:
				counter += 1

		if counter > int(passwordnum[0]) and counter < int(passwordnum[1].split(' ')[0]):
			print(counter)
			print('valid password found:',password[1])
			valid_pass.append(password[1])
			print('valid passwords',len(valid_pass))

for password in passwords.split('\n'):
	format_passwords(password)
