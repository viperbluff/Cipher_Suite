def caeser_encrypt(keyword):
	List=list(keyword)
	new_list=[]
        for i in List:
                if i=='x':
			x='a'
			new_list.append(x)
		elif i=='y':
			x='b'
			new_list.append(x)
		elif i=='z':
			x='c'
			new_list.append(x)
		elif i==' ':
			x=' '
			new_list.append(x)
		else:
			x=chr(ord(i)+3)
			new_list.append(x)
	y=" ".join(new_list)
	return y


def caeser_decrypt(keyword):
	List=list(keyword)
	new_list=[]
        for i in List:
                if i=='a':
			x='x'
			new_list.append(x)
		elif i=='b':
			x='y'
			new_list.append(x)
		elif i=='c':
			x='z'
			new_list.append(x)
		elif i==' ':
			x=' '
			new_list.append(x)
		else:
			x=chr(ord(i)-3)
			new_list.append(x)
	y=" ".join(new_list)
	return y

def main():
	word=raw_input("Do you want to Encrypt Or Decrypt? [E/D]:\t")
	if(word == 'E'):
		new_word=raw_input("Enter the Input Text to Encrypt:\t")
		x=caeser_encrypt(new_word)
		print "Cipher is shown below:"
		print x 
	elif(word == 'D'):
		new_word=raw_input("Enter the Cipher Text to Decrypt:\t")
		y=caeser_decrypt(new_word)
        	print "Plain Text is shown below:"
		print y
	else:
		print "Option selected isn't correct."

main()
