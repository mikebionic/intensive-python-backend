from random import randrange


class Employee:
	def __init__(self):
		self.name = ""
		self.id_number = ""
		self.mob_phone = ""
		self.balance = 0
		self.salary = 0.0
		self.check = False # account was created or not

	def create_employee(self):
		if self.check == False:
			self.name = input("Write your name: ")
			self.id_number = input("Write your ID number: ")
			self.mob_phone = input("Write your mobile phone: ")
			self.check = True
		else:
			print("You've already has created account!")

	def give_salary(self):
		# if you give the salary, it means that 1 month passed.

		while self.check == True:
			self.salary = float(input("Give salary ( > 540$): "))
			if self.salary >= 540:
				break
		self.balance = self.salary - randrange(100, 540)

	def check_yourself(self):
		if self.check == False:
			print("You didn't create an account")
		else:
			print(f"Name: {self.name}\n" \
				  f"ID number: {self.id_number}\n" \
				  f"Moblie phone: {self.mob_phone}\n" \
				  f"Balance: {self.balance}\n")


employee = Employee()


if __name__ == "__main__":
	while True:
		answer = input("\n1. Create account; 2. Give salary; 3. Check yourself ---> ")
		if answer == "1":
			employee.create_employee()
		elif answer == "2":
			employee.give_salary()
		elif answer == "3":
			employee.check_yourself()
		elif answer == "q":
			break
		else:
			print("Please choose in range 1-3")
			continue
