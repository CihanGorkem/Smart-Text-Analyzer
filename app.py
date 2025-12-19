from flask import Flask, render_template, request
import re
from collections import Counter

app = Flask(__name__)

# Filtrelenecek gereksiz kelimeler listesi
STOPWORDS = set([
    "ve", "bir", "ama", "fakat", "lakin", "ancak", "bu", "şu", "o", "da", "de", 
    "için", "gibi", "ile", "kadar", "mi", "mu", "mü", "mı", "en", "daha", "çok",
    "ise", "ki", "ben", "sen", "biz", "siz", "onlar", "olan", "olarak", "ne"
])

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        text = request.form['text']
        # Sadece harfleri al ve küçük harfe çevir
        words = re.findall(r'\w+', text.lower())
        
        # Filtreleme: Kelime STOPWORDS içinde değilse ve 2 harften uzunsa al
        filtered_words = [w for w in words if w not in STOPWORDS and len(w) > 2]
        
        # En çok geçen 5 anlamlı kelimeyi bul
        common_words = Counter(filtered_words).most_common(5)
        summary = ", ".join([word[0] for word in common_words])
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)