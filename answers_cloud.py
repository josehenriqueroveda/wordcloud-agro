from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv('answers.csv')

words = ''
stopwords = set(STOPWORDS)

# Iterate through csv
for item in df['answers']:
    # Cast each value to string
    item = str(item)
    # Split the value
    tokens = item.split()

    # Convert the tokens to lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        words += " ".join(tokens)+" "
    

wordcloud = WordCloud(width=1024, height=720, background_color='white',
                    stopwords=stopwords, min_font_size=10).generate(words)

# Save output
wordcloud.to_file('answers_cloud.png')

# Create WordCloud image
plt.figure(figsize=(16,12), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()