# Text-Semantic-Similarity-MachineLearning
Machine Learning Project of Semester VI students(Group 3) at School of Engineering and Applied Science, Ahmedabad University.

# Project Abstract
Machine Learning has found its place in the technological world rapidly since the past few years. One of the applications of Machine Learning includes Plagiarism Checking which is an application of Text Semantic Similarity. Text Semantic Similarity is a measure of the degree of semantic equivalence between two pieces of text.

How do we know whether a document that we are reading is authorized? Are students copying the content/ideas from other sources or are they produced by them?  
In this project, we build algorithms (one or more) and analyse the algorithms suitable for plagiarism checking software by applying the already understood concepts of Machine Learning. 

# Group Members
1)Aneri Sheth- 1401072 <br />
2)Himanshu Budhia- 1401039 <br />
3)Raj Shah- 1401050 <br />
4)Twinkle Vaghela- 1401106

# NATURAL LANGUAGE PROCESSING
Natural Language processing is a wide domain coveringconcepts of Computer Science, Artificial Intelligence and Machine Learning. 
It is used to analyze text or how humansspeak. One of the applications of NLP is Semantic Analysis(Understanding the meaning of text).

# ![Alt text](/Images/VennNLP.PNG?raw=true "NLP")

# CORPUS-BASED APPROACH
This approach uses semantically annotated corpora to train
Machine learning algorithms to decide which word to use in
which context. Corpus-based methods are supervised learning
approaches when the training data is trained by the algorithms.
The corpora and the lexical resource used is WordNet.

# ![Alt text](/Images/NLTK.jpg?raw=true "NLTK Overview")
<br />
Sentence 1 - A cemetery is a place where dead people’s bodies or their ashes are buried.
<br />
Sentence 2 - A graveyard is an area of land, sometimes near a church, where dead people are buried.
<br />

- #### Tokenizing:
Splitting sentences and words from the body of text. Words are separated by space after the word, i.e.after every word there is a space. It counts punctuation as a separate token.
<br />
<br />
![Alt text](/Images/tokenize.JPG?raw=true "Tokenizing Example")
<br />
[Tokenize.py](https://github.com/budhiahimanshu96/Text-Semantic-Similarity-MachineLearning/blob/master/NLTK/word_tokenize.py)
  
- #### Stop Words:
Sometimes, some extremely common words which would appear to be of little value in helping select documents matching a user need are excluded from the vocabulary entirely. These words are called stop words .
Stop words can be filtered from the text to be processed. 
<br />
<br />
![Alt text](/Images/stop_words.JPG?raw=true "Stopwords Example")
<br />
[StopWords.py](https://github.com/budhiahimanshu96/Text-Semantic-Similarity-MachineLearning/blob/master/NLTK/stop_words.py)

- #### Lemmatizing:
The goal of lemmatization is to reduce inflectional forms and sometimes derivationally related forms of a word to a common base form.
By default, an attempt will be made to find the closest noun of a word.
<br/>
<br />
![Alt text](/Images/lemmatizing.JPG?raw=true "Lemmatizing Example")
<br />
[Lemmatizing.py](https://github.com/budhiahimanshu96/Text-Semantic-Similarity-MachineLearning/blob/master/NLTK/Lemmatizing.py)

- #### Synsets:
WordNet is a lexical database for the English language, and is part of the NLTK corpus. We can use WordNet alongside the NLTK module to find the meaning of words, synonyms, antonyms and more.
<br/>
<br />
![Alt text](/Images/wordnet.JPG?raw=true "Wordnet Example 1")
<br />
<br />
![Alt text](/Images/wordnet2.JPG?raw=true "Wordnet Example 2")
<br />
[Wordnet.py](https://github.com/budhiahimanshu96/Text-Semantic-Similarity-MachineLearning/blob/master/NLTK/similarity.py)

# Results

- Let S1 be ”I was given a card by her in the garden” and S2 be ”In the garden, she gave me a card.”
- For semantic analysis, two phrases/sentences are taken. The two sentences are similar, dissimilar or somewhat similar.
- After that, set of stopwords are defined for English language.
- After eliminating the special characters and punctuations and then removing all the stop words and lemmatizing, we get S1={I, given, card, garden} and S2={In, garden, gave, card}.
- After lemmatizing, we find the synonyms of the lemmatized words which are called synsets. Then, we compare first word of S1 with all the words of S2 and continue this iteratively and find the similarity index of each word with words in the S2.
- We find the mean of the computed similarity indexes and thus we we anaylze the semantic similarity using machine learning.
- If the similarity index is less than 0.65, the sentences are labeled as ’Not Similar’, if it is between 0.65 and 0.8, the sentences are labeled as ’Somewhat Similar’ and more than 0.8, the sentences are ’Similar’.

# Output

- Similarity Example 1: <br /> ![Alt text](/Images/Similar.PNG?raw=true "Similar Example 1")
- Similarity Example 2: <br />![Alt text](/Images/Similar2.PNG?raw=true "Similar Example 2")
- Somewhat Similarity Example: <br />![Alt text](/Images/SomewhatSimilar.PNG?raw=true "Somewhat Similar Example")
- Dissimilarity Example: <br />![Alt text](/Images/NotSimilar.PNG?raw=true "Not-Similar Example")
<br />
[Final.py](https://github.com/budhiahimanshu96/Text-Semantic-Similarity-MachineLearning/blob/master/NLTK/Final.py)


# Discussion and Future Work

- Semantics Similarity has been done for sentences and phrases. However, for paragraphs and short texts will need complex algorithms for separating of sentences and finding their semantics similarity.
- We find similarity word by word and thus we may get false positives and negatives.
- We would try to decrease the false positive and negative rates by using sentence- sentence similarity instead of word-word similarity.
- Our implementation does not consider spellings. To implement that, Longest Common Subsequence (LCS) Algorithm can be used.


