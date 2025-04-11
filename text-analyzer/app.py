from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    if request.method == 'POST':
        text = request.form['text']
        words = text.split()
        word_count = len(words)
        char_count = len(text)
        word_freq = {}
        for word in words:
            word = word.lower().strip(",.?!;:")
            word_freq[word] = word_freq.get(word, 0) + 1
        most_freq_word = max(word_freq, key=word_freq.get)
        lexical_density = len(set(words)) / word_count if word_count > 0 else 0

        result = {
            'word_count': word_count,
            'char_count': char_count,
            'most_freq_word': most_freq_word,
            'lexical_density': round(lexical_density, 2)
        }
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development purposes