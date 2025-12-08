import os

def main():
	while True:
		# Initial Menu
		print("[0]. Quit Program")
		print("[1]. Encrypt Message")
		print("[2]. Decrypt Message")
	
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
				encrypt_decrypt_message(1)
			case 2:
				encrypt_decrypt_message(-1)

def encrypt_decrypt_message(encrypt_or_decrypt):
	global uppercase_letters, lowercase_letters

	message = input("Message: ")

	# Input validation for the Key
	valid_key = False

	while valid_key == False:
		key = input("Key: ")
		if len(key) == 0:
			print("Please input a key.")
			continue
		elif len(remove_nonalpha(key)) == 0:
			print("Your key must contain valid letters used in the English alphabet.")
		else:
			break

	key = remove_nonalpha(key)
	key_length = len(key)

	# Declares empty string
	modified_text = "" 

	# Encryption/Decryption of text
	for i in range(len(message)):
		letter = message[i]
		if letter.isalpha():
			character_list = uppercase_letters if letter.isupper() else lowercase_letters

			try:
				rotation = uppercase_letters.index(key[i % key_length])
			except ValueError:
				rotation = lowercase_letters.index(key[i % key_length])

			# Rotates text one way if encoding, rotates text opposite way if decoding
			modified_text += character_list[character_list.index(letter) + rotation * encrypt_or_decrypt]
		else:
			modified_text += letter

	# Prints encrypted/decrypted message
	if encrypt_or_decrypt == 1:
		print(f"Your encrypted message: {modified_text}")
	else:
		print(f"Your decrypted message: {modified_text}")

def remove_nonalpha(text):
	# Declares empty string
	new_text = ""

	# Removes all non-alpha characters
	for character in text:
		if character.isalpha():
			new_text += character
		else:
			continue

	return new_text

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

def clear_terminal(): os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
	main()