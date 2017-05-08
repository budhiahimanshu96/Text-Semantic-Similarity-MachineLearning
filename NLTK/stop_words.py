from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

str1 = "A cemetery is a place where dead people's bodies or their ashes are buried."
str2 = "A graveyard is an area of land ,sometimes near a church, where dead people are buried." 

#example_sentence = "This is an example showing off stop word filtration."
stop_words = set(stopwords.words("english"))

words1 = word_tokenize(str1)
words2 = word_tokenize(str2)

filtered_sentence1 = []
filtered_sentence2 = []

for w in words1:
    if w not in stop_words:
        filtered_sentence1.append(w)



#filtered_sentence = [w for w in data if not w in stop_words]

print(filtered_sentence1)
print('\n')

for w in words2:
    if w not in stop_words:
        filtered_sentence2.append(w)



#filtered_sentence = [w for w in data if not w in stop_words]

print(filtered_sentence2)
