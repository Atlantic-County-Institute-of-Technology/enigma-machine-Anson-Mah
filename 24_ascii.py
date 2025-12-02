import os

def main():
	while True:
		# Initial Menu
		print("")
		print("[0]. Quit Program")
		print("[1]. ASCII Cipher (Encode)")
		print("[2]. ASCII Cipher (Decode)")
	
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
				ascii_cipher_encode()
			case 2:
				ascii_cipher_decode()

def ascii_cipher_encode():
	user_text = input("Input text to encode: ")

	# Declares empty string
	encrypted_text = ""

	for letter in user_text:
		encrypted_text += str(ord(letter)) + " "
	
	print("")
	print(encrypted_text)

def ascii_cipher_decode():
	error_hit = False

	user_text = input("Input ASCII to decode: ")

	user_ascii_list = user_text.split()

	# Declares empty string
	decrypted_text = ""

	for i in user_ascii_list:
		try:
			decrypted_text += chr(int(i))
		except ValueError:
			print("\nText could not be decrypted. There is something wrong with the input.")
			error_hit = True
	
	if error_hit == False:
		print("")
		print(decrypted_text)

def clear_terminal(): os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
	main()