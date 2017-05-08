from nltk.stem import WordNetLemmatizer
from nltk.tokenize import  word_tokenize

#myfile =  open('Text1.txt', 'r') 
#data=myfile.read().replace('\n', '')
data1 = " A cemetery is a placing where dead people's bodies or their ashes are buried"
data2 = "A graveyard is an area of land ,sometimes near a church, where dead people are buried."
lemmatizer  =  WordNetLemmatizer()
lemm_sentence1 = []
lemm_sentence2 = []


for i in word_tokenize(data1):
    lemm_sentence1.append(lemmatizer.lemmatize(i))
    
print(lemm_sentence1)
print('\n')

for i in word_tokenize(data2):
    
    lemm_sentence2.append(lemmatizer.lemmatize(i))
print(lemm_sentence2)


