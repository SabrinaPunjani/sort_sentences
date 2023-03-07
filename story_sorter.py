
#Sabrina Punjani Story Sorter 2023



import nltk #natural language toolkit 

# download the punkt tokenizer if necessary
nltk.download('punkt')

filename = 'ShortStory.txt'

# open the input file
with open(filename, 'r') as file:
    # read the contents of the file
    contents = file.read()
    contents= contents.replace('------------------------------------------------','')

# split the contents into a list of sentences
sentences = nltk.sent_tokenize(contents)

# sort the sentences in alphabetical order, we will ignore the first character of the string if it starts with a quote or bracket when sorting
#lambda acts as a function passing through the string with the first index sliced off if the first index is " or ( or --
sentences = sorted(sentences, key=lambda s: s[1:] if s.startswith('"') or s.startswith('(') else s)
sentences = sorted(sentences, key=lambda s: s[2:] if s.startswith('--') else s)
#ignore case when sorting
sentences = sorted(sentences, key=lambda s: s.lower())



# join the sorted sentences back into a nicely formatted string

paragraph = 6 #new paragraph after this many sentences
newsection = 20 #new section after this many sentences
sorted_contents = ''

for i in range(len(sentences)):
    sorted_contents+=sentences[i]+' '
    if i%paragraph==0:
        sorted_contents+='\n'
    if i%newsection ==0:
        sorted_contents+='\n ------------------------------------------------ \n \n'
     
        

# write the sorted contents into the output file
with open('SortedShortStory.txt', 'w') as file:
    file.write(sorted_contents)

