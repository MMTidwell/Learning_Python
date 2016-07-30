# Checks for profanity

# Step 1
#     - Read text from document
# Step 2
#     - Check for curse words


def read_text():
    quotes = open("C:\Users\mittsy\Google Drive\PROGRAMMING\Udacity\Intro to Programing\Python\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()


read_text()
