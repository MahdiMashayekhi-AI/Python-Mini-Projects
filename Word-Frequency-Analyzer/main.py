import string
import nltk
from collections import Counter

# Download the stopwords package
nltk.download('stopwords')

# Define the input file path and the number of top words to show
input_file = 'input.txt'
num_top_words = 10

# Load the stop words
stop_words = set(nltk.corpus.stopwords.words('english'))

# Read the input file and tokenize it into words
with open(input_file, 'r') as file:
    text = file.read().lower()
    words = text.split()

# Remove punctuation and stop words from the list of words
words = [word.strip(string.punctuation) for word in words if word not in stop_words]

# Count the frequency of each word and store the counts in a dictionary
word_counts = Counter(words)

# Sort the dictionary by count values in descending order
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Print out the top N words and their counts in a formatted report
print(f'Top {num_top_words} words in {input_file}:')
for word, count in sorted_word_counts[:num_top_words]:
    print(f'{word}: {count}')
