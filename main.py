path = './books/frankenstein.txt'

def count_word(path):
	with open(path) as f:
		file_contents = f.read()
		word_list = file_contents.split()
	return len(word_list), file_contents

def count_character(content):
	char_count = {}
	lower_content = content.lower()

	for char in lower_content:
		if char == ' ':
			continue
		if char not in char_count:
			char_count[char] = 1
		else:
			char_count[char] += 1

	return char_count

#list of dictionary
def create_list_char(content):
	list_char = []
	# list char: value = directory
	for key in content:
		if not key.isalpha():
			continue
		list_char.append({"character": key, "count": content[key]})
	return list_char

def sort_on(value):
	return value["count"]

def main():
	number_of_word, file_contents = count_word(path)
	print(f"Number of words counted: {number_of_word}")
	char_count_dict = count_character(file_contents)
	result = create_list_char(char_count_dict)
	result.sort(reverse=True, key=sort_on)
	print(result)

main()