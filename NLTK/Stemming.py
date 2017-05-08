#Stemming - stemming is a method of finding the roots of the words
#            from the sentence  For eg: written = write


from nltk.stem import PorterStemmer #importing the PortStemmer function
from nltk.tokenize import word_tokenize #importing the word_tokenize function

data = " A cemetery is a placing where dead people's bodies or their ashes are buried"

#myfile =  open('Text1.txt', 'r') #Reading file named Text1
#data = myfile.read().replace('\n', '')#File is converted to array of letters
#ex = ["write","writing","written"]
ps = PorterStemmer() #stemming

for i in word_tokenize(data): #Tokenizing the word
    print(ps.stem(i))
