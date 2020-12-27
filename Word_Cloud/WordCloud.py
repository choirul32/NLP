import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# dataset mengambil satu baris dalam text
def readDataset(file):
    with open(file) as f:
        lines = f.readline().lower()
        f.close()
    lines = lines.translate(str.maketrans('', '', string.punctuation))
    res = ' '.join([i for i in lines.split(' ') if not i.isdigit()])
    return res #bentuk paragraph satu baris

def readStopword(file):
    words = open('stopwords.txt', 'r') 
    lines = words.readlines() 
    stop_words = []
    for line in lines: 
        stop_words.append(line.strip())
    return stop_words # bentuk list

dataset_ = readDataset('datatext.txt')
stopword_ = readStopword('stopwords.txt')

wordcloud = WordCloud(width = 800, height = 800, background_color = 'black', stopwords = stopword_, max_words = 1000, min_font_size = 20).generate(dataset_)
#plot the word cloud
fig = plt.figure(figsize = (8,8), facecolor = None)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()