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
				encrypt_decrypt_message("encrypt")
			case 2:
				encrypt_decrypt_message("decrypt")

def encrypt_decrypt_message(cipher_direction):
	global uppercase_letters, lowercase_letters

	# File Validation
	# If user's filename does not exist in the assets folder, return back to Initial Menu [main() function].
	try:
		file_name = input("Enter File Name: ")
		with open(f"assets/{file_name}.txt", "r") as file:
			message = file.read()
	except FileNotFoundError:
		print('File unable to be located. Make sure that you have done the following things:\n')
		print('Put your message inside a .txt file.')
		print('Put your file inside the "assets" folder.')
		print('Input the file name without the ".txt" extension.\n')
		return

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

	key_length = len(key)

	# Filters out special characters from the key and makes it all lowercase
	key = remove_nonalpha(key).lower()

	# Declares empty string. This string will store the encrypted/decrypted text.
	modified_text = "" 

	# Encryption/Decryption of Text
	# j is used so that the cipher can skip over special characters
	j = -1
	rotation_direction = 1 if cipher_direction == "encrypt" else -1
	for i in range(len(message)):
		letter = message[i]
		if letter.isalpha():
			character_list = uppercase_letters if letter.isupper() else lowercase_letters
			j += 1
			rotation = lowercase_letters.index(key[j % key_length])

			# Rotates text one way if encoding, rotates text opposite way if decoding
			modified_text += character_list[character_list.index(letter) + rotation * rotation_direction]
		else:
			modified_text += letter

	# Prints Modified and Unmodified Text
	print(f"Original Text: {message}")
	print(f"Your {cipher_direction}ed message: {modified_text}")

	# END TEXT MODIFICATION
	# START FILE HANDLING

	while True:
		# Save Menu
		print(f"\nWhat would you like to do with your {cipher_direction}ed message?")
		print("[1]. Overwrite Existing File")
		print("[2]. Write to a New File")
		print("[3]. Nothing")

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

		# Runs the code associated with user selection
		match selection:
			case 1:
				with open(f"assets/{file_name}.txt", "w") as file:
					file.write(modified_text)
				print("File Overwritten.\n")
			case 2:
				file_name = input("Enter name of New File: ")
				with open(f"assets/{file_name}.txt", "w") as new_file:
					new_file.write(modified_text)
				print("New File Created.\n")
			case 3:
				print("Nothing ever happens...\n")

		break

def remove_nonalpha(text):
	# Declares empty string. This string will store the filtered text.
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