def words(string):

	split_string = string.split()
	my_dict = {}

	for word in split_string:
		if word.isdigit():
		word = int(word)

		if word in my_dict:
			my_dict[word] += 1

		else:
			my_dict[word] = 1

	return my_dict


