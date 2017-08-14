import urllib

def read_text():
	quotes = open ('/home/prakhar/Desktop/movie_quotes.txt')
	content_of_file = quotes.read()
	#print(content_of_file)
	quotes.close()
	check_profanity(content_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=' + text_to_check)
	output = connection.read()
	if (output == 'false'):
		print('koi gaali nahi thi')
	else:
		print ('gaali deta h')
	connection.close()

read_text()