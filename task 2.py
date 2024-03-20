loc = input(r'Enter path of Image : ')

print('The path of file : ', loc)
	
fin = open(loc, 'rb')
image = fin.read()
fin.close()
	
image = bytearray(image)
#image_new = image[::-1]     #swap operation

for index, values in enumerate(image):  #encryption using mathematical operation 
    image[index] = (7*values + 4) % 256
    
for index, values in enumerate(image):  #decryption using mathematical operation
   image[index] = 183*(values - 4) % 256

fin = open(loc, 'wb')
	
fin.write(image)
fin.close()
print('Encryption Done...')

	

