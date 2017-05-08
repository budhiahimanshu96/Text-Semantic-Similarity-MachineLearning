import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

##Sometimes a single sentence can contain two relevant opinions
##For example- Apple launched the iPhone and Ferarri launched 911
## Now if I give an opinion regarding something chunking helps
#me identify regarding what object I am making the opinion.

#train_text=state_union.raw("2005-GWBush.txt")
#sample_text=state_union.raw("2006-GWBush.txt")

myfile =  open('Text2.txt', 'r') 
data1 = myfile.read().replace('\n', '')

#myfile =  open('Text1.txt', 'r') 
#data=myfile.read().replace('\n', '')


custom_sent_tokenizer= PunktSentenceTokenizer(data1)

tokenized = custom_sent_tokenizer.tokenize(data1)


def process_content():
    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            #.?and * are regexps. 
            chunkGram="""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"""
            chunkParser=nltk.RegexpParser(chunkGram)
            chunked=chunkParser.parse(tagged)
            print(chunked)
            chunked.draw()
    except Exception as e:
        print(str(e))

process_content()
