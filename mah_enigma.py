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
	global uppercase_letters, lowercase_letters

	message = input("Message: ")
	key = input("Key: ")
	key_length = len(key)

	# Declares empty string
	encrypted_text = "" 

	for i in range(len(message)):
		letter = message[i]
		if letter.isalpha():
			character_list = uppercase_letters if letter.isupper() else lowercase_letters
			rotation = character_list.index(key[i % key_length])
			encrypted_text += character_list[character_list.index(letter) + rotation]
		else:
			encrypted_text += letter

	print(encrypted_text)

def decode_message():
	global uppercase_letters, lowercase_letters

	message = input("Message: ")
	key = input("Key: ")
	key_length = len(key)

	# Declares empty string
	decrypted_text = "" 

	for i in range(len(message)):
		letter = message[i]
		if letter.isalpha():
			character_list = uppercase_letters if letter.isupper() else lowercase_letters
			rotation = character_list.index(key[i % key_length])
			decrypted_text += character_list[character_list.index(letter) - rotation]
		else:
			decrypted_text += letter

	print(decrypted_text)

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

def clear_terminal(): os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
	main()