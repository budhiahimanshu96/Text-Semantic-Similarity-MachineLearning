import nltk
from nltk.corpus import state_union
from nltk.tokenize import sent_tokenize

##Chinking is removal of something. Basically, it is used to remove
##certain portions of chunks

#train_text=state_union.raw("2005-GWBush.txt")
#sample_text=state_union.raw("2006-GWBush.txt")

myfile =  open('Text1.txt', 'r') 
data = myfile.read().replace('\n', '')

#custom_sent_tokenizer= PunktSentenceTokenizer(train_text)

tokenized = sent_tokenize(data)


def process_content():
    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            #Chunking everything. Chinking is written in }{
            chunkGram="""Chunk: {<.*>+}
                        }<VB.?|IN|DT>+{"""
            chunkParser=nltk.RegexpParser(chunkGram)
            chunked=chunkParser.parse(tagged)
            print(chunked)
            chunked.draw()
        
    except Exception as e:
        print(str(e))


process_content()
