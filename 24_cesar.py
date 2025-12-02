import os

def main():
	while True:
		# Initial Menu
		print("[0]. Quit Program")
		print("[1]. List Cesar Cipher (Encode)")
		print("[2]. List Cesar Cipher (Decode)")
		print("[3]. Ordinal Cesar Cipher (Encode)")
		print("[4]. Ordinal Cesar Cipher (Decode)")
	
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
				list_cesar_cipher_encode()
			case 2:
				list_cesar_cipher_decode()
			case 3:
				ordinal_cesar_cipher_encode()
			case 4:
				ordinal_cesar_cipher_decode()


def list_cesar_cipher_encode():
	global alphabet_lower, alphabet_upper

	has_alpha = False

	while has_alpha == False:
		user_text = input("Input text to encode: ")
		for char in user_text:
			if char.isalpha():
				has_alpha = True
				break
		if has_alpha == False:
			clear_terminal()
			print("String Has No Letters. Please input a string that has at least one letter.\n")

	while True:
		try:
			rotation = int(input("Input Shift / Rotation: "))
		except ValueError:
			clear_terminal()
			print("Input Unrecognized. Please input an integer value.\n")
			continue
		if rotation > 25 or rotation < -25:
			clear_terminal()
			print("Input not a part of valid encryption options. Please input an integer value between -25 and 25.\n")
		else:
			break

	# Declares empty string
	encrypted_text = "" 

	for letter in user_text:
		if letter.isalpha():
			character_list = alphabet_upper if letter.isupper() else alphabet_lower
			encrypted_text += character_list[character_list.index(letter) + rotation]
		else:
			encrypted_text += letter

	print("\n" + encrypted_text + "\n")


def list_cesar_cipher_decode():
	global alphabet_lower, alphabet_upper

	has_alpha = False

	while has_alpha == False:
		user_text = input("Input text to decode: ")
		for char in user_text:
			if char.isalpha():
				has_alpha = True
				break
		if has_alpha == False:
			clear_terminal()
			print("String Has No Letters. Please input a string that has at least one letter.\n")
	
	print("")

	# Rotates through and prints every possible Cesar Cipher
	for i in range(26):
		# Declares empty string
		encrypted_text = "" 
		for letter in user_text:
			if letter.isalpha():
				character_list = alphabet_upper if letter.isupper() else alphabet_lower
				encrypted_text += character_list[character_list.index(letter) - i]
			else:
				encrypted_text += letter
		print(encrypted_text)
	
	print("")
	

alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def ordinal_cesar_cipher_encode():

	# Input Validation for User Text
	has_alpha = False
	while has_alpha == False:
		user_text = input("Input text to encode: ")
		for char in user_text:
			if char.isalpha():
				has_alpha = True
				break
		if has_alpha == False:
			clear_terminal()
			print("String Has No Letters. Please input a string that has at least one letter.\n")

	while True:
		try:
			rotation = int(input("Input Shift / Rotation: "))
			break
		except ValueError:
			clear_terminal()
			print("Input Unrecognized. Please input an integer value.\n")
			continue

	# Declares empty string
	encrypted_text = "" 

	for letter in user_text:
		if letter.isalpha():
			charset = 65 if letter.isupper() else 97
			encrypted_text += chr((ord(letter) - charset + rotation) % 26 + charset)
		else:
			encrypted_text += letter

	print("\n" + encrypted_text + "\n")


def ordinal_cesar_cipher_decode():

	# Input Validation for User Text
	has_alpha = False
	while has_alpha == False:
		user_text = input("Input text to decode: ")
		for char in user_text:
			if char.isalpha():
				has_alpha = True
				break
		if has_alpha == False:
			print("String Has No Letters. Please input a string that has at least one letter.\n")

	print("")

	# Rotates through and prints every possible Cesar Cipher
	for i in range(26):
		# Declares empty string
		encrypted_text = ""
		for letter in user_text:
			if letter.isalpha():
				charset = 65 if letter.isupper() else 97
				encrypted_text += chr((ord(letter) - charset - i) % 26 + charset)
			else:
				encrypted_text += letter
		print(encrypted_text)

	print("")

def clear_terminal(): os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
	main()