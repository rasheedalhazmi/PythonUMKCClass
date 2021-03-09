import io
import urllib.request
import nltk
from bs4 import BeautifulSoup
from bs4.element import Comment
from nltk import ne_chunk
#nltk.download('words')

# TODO
# Grab text, Source: https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


html = urllib.request.urlopen('https://en.wikipedia.org/wiki/Google').read()
finalText = text_from_html(html)
text_file = "1 input.txt"

with io.open(text_file, "w", encoding="utf-8") as f:
    f.write(finalText)

# Tokenization
from nltk.tokenize import word_tokenize

tokenizedText = word_tokenize(finalText)
with io.open("2 Tokenized.txt", "w", encoding="utf-8") as f:
    f.write(str(tokenizedText))
f.close()

# PoS Tags
TaggedText = nltk.pos_tag(tokenizedText)
with io.open("3 TaggedText.txt", "w", encoding="utf-8") as f:
    f.write(str(TaggedText))
f.close()

# stemming
from nltk.stem import PorterStemmer

ps = PorterStemmer()
StemmedText = ()
for word in tokenizedText:
    StemmedText += (word, ps.stem(word))
with io.open("4 StemmedText.txt", "w", encoding="utf-8") as f:
    f.write(str(StemmedText))

# lemmatization
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
LemmatizedText = ()
for word in tokenizedText:
    LemmatizedText += word, lemmatizer.lemmatize(word)
with io.open("5 LemmatizedText.txt", "w", encoding="utf-8") as f:
    f.write(str(LemmatizedText))

# trigram
from nltk.util import ngrams
#alfari
trigrams = ngrams(tokenizedText, 3)
final = ""
for element in trigrams:
    final += str(element)
    final += "\n"
with io.open("6 Trigrams.txt", "w", encoding="utf-8") as f:
    f.write(str(final))

# Named Entity Recognition
NER = ne_chunk(TaggedText)
with io.open("7 NER.txt", "w", encoding="utf-8") as f:
    f.write(str(NER))