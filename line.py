
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None
	alice_word_count = 0
	Dajie_word_count = 0
	alice_sticker_count = 0
	Dajie_sticker_count = 0
	alice_image_count = 0
	Dajie_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == '千芳':
			if s[2] =='貼圖':
				alice_sticker_count += 1
			elif s[2] == '圖片':
				alice_image_count += 1
			else:
				for m in s[2:]:
					alice_word_count += len(m)
		elif name == 'Dajie':
			if s[2] =='貼圖':
				Dajie_sticker_count += 1
			elif s[2] == '圖片':
				Dajie_image_count += 1
			else:
				for m in s[2:]:
					Dajie_word_count += len(m)
	print('千芳說了',alice_word_count, '傳了',alice_sticker_count, '個貼圖',alice_image_count, '個圖片')
	print('Dajie說了',Dajie_word_count, '傳了',Dajie_sticker_count, '個貼圖',Dajie_image_count, '個圖片')




		#print(s)

	

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('line.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

main()