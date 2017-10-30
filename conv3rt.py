import getch
while True:
	char = getch.getch()
	charcode = ord(char)
	print("CHAR: " + char + "   ASCII: " + str(charcode) + "   HEX: " + str(hex(charcode)) + "   OCT: " + str(oct(charcode)))
