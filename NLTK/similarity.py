from nltk.corpus import wordnet
from itertools import product

sims = []

list1 = ['Kaivalya']
#list2 = ['choose', 'copy', 'define', 'duplicate', 'find', 'how', 'identify', 'label', 'list', 'listen', 'locate', 'match', 'memorise', 'name', 'observe', 'omit', 'quote', 'read', 'recall', 'recite', 'recognise', 'record', 'relate', 'remember', 'repeat', 'reproduce', 'retell', 'select', 'show', 'spell', 'state', 'tell', 'trace', 'write']
list2 = ['Boy']
list = []
print("word1 : ", list1)
print("word2 : ", list2)

for word1,word2 in product(list1,list2):
    
       # print(word1)
        #print(word2)
        syns1 = wordnet.synsets(word1)
        #print(wordFromList1[0])
        syns2 = wordnet.synsets(word2)
        #print(wordFromList2[0])
        for sense1, sense2 in product(syns1, syns2):
            d = wordnet.wup_similarity(sense1, sense2)
            if d != None:
                sims.append(d)
        #if wordFromList1 and wordFromList2: #Thanks to @alexis' note
          #  s = wordFromList1[0].wup_similarity(wordFromList2[0])
           # list.append(s)
print("Similarity index :",max(sims))
        
