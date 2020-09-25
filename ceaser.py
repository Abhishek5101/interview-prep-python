def caesarCipherEncryptor(string, key):
	new = ""
	for s in string:
		new += get_new_letter(s, key)
	return new


def get_new_letter(letter, key):
	offset = 96
	pos = (ord(letter) - offset) + key
	if pos > 26:
		wrap = pos % 26
		return chr(wrap + offset)
	else:
		return chr(pos + offset)


print(caesarCipherEncryptor("abc", 2))
print(caesarCipherEncryptor("abc", 67))