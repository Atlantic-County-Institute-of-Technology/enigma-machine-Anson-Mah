import os

def main():
	while True:
		# Initial Menu
		print("[0]. Quit Program")
		print("[1]. Encode Message")
		print("[2]. Decode Message")
	
		# Input Correction
		# If the user's input would break the program, it changes the input such that it will not break the program.
		while True:
			try:
				selection = int(input("Select an Option: "))
				print("")
				break
			except ValueError:
				# On ValueError, the input variable is instead set to an integer not corresponding to anything on the menu, which will bring you back to the initial menu
				selection = 9
				break

		clear_terminal()

		# Runs different functions based off of what you inputted
		match selection:
			case 0:
				print("Program Terminated")
				exit()
			case 1:
				encode_message()
			case 2:
				decode_message()

def encode_message():
	message = input("Message: ")
	key = input("Key: ")

	print(message)
	print(key)

def decode_message():
	pass

def clear_terminal(): os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
	main()