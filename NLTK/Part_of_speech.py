import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#train_text = state_union.raw("Text1.txt")
#sample_text = state_union.raw("Text2.txt")

myfile =  open('Text1.txt', 'r') 
data = myfile.read().replace('\n', '')

custom_sent_tokenizer = PunktSentenceTokenizer(data)
tokenized = custom_sent_tokenizer.tokenize(data)

def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


process_content()
