from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# tokenizing - word tokenizers.... sentence tokenizers
# lexicon and corporas
# corpora - body of text. ex: medical journals, presidential speeches, English language
# lexicon - words and their means
str1 = "A cemetery is a place where dead people's bodies or their ashes are buried."
str2 = "A graveyard is an area of land ,sometimes near a church, where dead people are buried."
stop_words = set(stopwords.words("english"))
filtered_sentence1 = []
filtered_sentence2 = []


#myfile =  open('Text1.txt', 'r') 
#data=myfile.read().replace('\n', '')
##print(sent_tokenize(example_text))
##
##print(word_tokenize(example_text))


for i in word_tokenize(str1):
    if i not in stop_words:
        filtered_sentence1.append(i)

print(filtered_sentence1)

for i in word_tokenize(str2):
    if i not in stop_words:
        filtered_sentence2.append(i)

print(filtered_sentence2)



