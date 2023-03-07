

filename = "ShortStory.txt"

# open the input file
with open(filename, 'r') as file:
    # read the contents of the file
    contents = file.read()

# split the contents into a list of sentences
sentences = contents.split('.')

# sort the sentences in alphabetical order
sentences.sort()

# join the sorted sentences back into a string
sorted_contents = '.'.join(sentences)

# write the sorted contents to the output file
with open('SortedShortStory.txt', 'w') as file:
    file.write(sorted_contents)
