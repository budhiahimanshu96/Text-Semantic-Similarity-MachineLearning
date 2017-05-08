from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet

myfile =  open('Text1.txt', 'r') 
data=myfile.read().replace('\n', '')

#myfile =  open('Text2.txt', 'r') 
#data1=myfile.read().replace('\n', '')

data = word_tokenize(data)
#data1 = word_tokenize(data1)

#x = 0
#for i in data:
    #for j in data1:
    #print(data(i))
        
 #       w1= wordnet.synsets(i)
  #      print(w1)
   #     w2= wordnet.synsets(data1[])
    #    print(w1)
        #print(w1[x].wup_similarity(w2[x]))
        #print('\n')
        #x++
    

synonyms= []
antonyms= []
for i in data:
    print(i)
    print('\n')
    for syn in wordnet.synsets(i):
        for l in syn.lemmas():
            print(l.name())
            #synonyms.append(l.name())
            #print(synonyms)
            #if l.antonyms():
              # antonyms.append(l.antonyms()[0].name()
               #print(antonyms)`
