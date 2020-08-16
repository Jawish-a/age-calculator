from datetime import datetime

def check_birthdate(year, month, day):
	# write code here
	birthdate = datetime(year, month, day)
	if birthdate > datetime.now():
		return False
	else:
		return True
	

def calculate_age(year, month, day):
    # write code here
	now = datetime.now()
	age = now.year - year
	print("You are " + str(age) + " years old.")

def main():
	# write main code here
	year = int(input("Enter year of birth: "))
	month = int(input("Enter month of birth: "))
	day = int(input("Enter day of birth: "))
	if check_birthdate(year, month, day):
		calculate_age(year, month, day)
	else:
		print("the birthdate is invalid.")


if __name__ == '__main__':
	main()