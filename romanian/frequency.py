import re
import matplotlib.pyplot as plt
from nltk.stem.snowball import RomanianStemmer
#import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud

# for stopwords
#nltk.download('stopwords')

# =============================================================================
# Function: compute frequency of romanian
# Input : filename
# Output : dictory with word and number
# =============================================================================
def frequency(filename):
    
    # load file
    with open(filename,'r',encoding='utf-8') as f:
        content = f.read()
    
    # spllit
    words = re.split(r'[^a-zA-Z0-9-]+', content)
    dictory = {}
    
    # stop words
    try: 
        stop_words = stopwords.words('romanian')
    except:
        import nltk
        nltk.download('stopwords')
        stop_words = stopwords.words('romanian')
    # stem 
    stemmer = RomanianStemmer(ignore_stopwords=True)
    for w in words:
        w = w.lower()
        w = stemmer.stem(w)
        if w in stop_words or w == '-':
            continue
        if w in dictory:
            dictory[w] += 1
        else:
            dictory[w] = 1
        
    return dictory
    
# =============================================================================
# Function : draw horizantol bar of words
# Input : dictory of word and numble ,  display numble
# =============================================================================
def plotword(words, num=10):
    
    # sort
    words = sorted(words.items(), key=lambda x: x[1], reverse=True)
    cuv = [w[0] for w in words[:num]][::-1]
    apar = [w[1] for w in words[:num]][::-1]
    pos = range(num)
    
    plt.figure(1)
    plt.barh(pos, apar, align='center')
    plt.yticks(pos, cuv)
    plt.xlabel("Aparitii")
    plt.title("Cele mai frecvente cuvinte")
    
    plt.show()
    
# =============================================================================
# Function : draw wordcloud of words
# Input : dictory of word and numble
# =============================================================================
def wordcloud(words):
    wc = WordCloud(max_words=2000,
               width=400,
               height=400,
               background_color="white",
               margin=5)
    wc.generate_from_frequencies(words)
    plt.figure(2)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    
# main 
if __name__ == "__main__":
    
    words = frequency('test.txt')
    plotword(words,20)
    wordcloud(words)
    
