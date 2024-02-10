from bangla_stemmer.stemmer import stemmer
stmr = stemmer.BanglaStemmer()
valid_bangla_char = set(['া','ি','ী','ু','ূ','ৃ','ে','ৈ','ো','ৌ','ক','খ',
'গ','ঘ','ঙ','চ','ছ','জ','ঝ','ঞ','ট','ঠ','ড','ঢ','ণ','ত','থ','দ','ধ','ন',
'প','ফ','ব','ভ','ম','য','র','ল','শ','ষ','স','হ','ড়','ঢ়','য়','ৎ','ং','ঃ'
'‍ঁ','‍্','‍্য','‍‍্র','‍‍র্ক','‍্ব','৺','ক্ষ','জ্ঞ','অ','আ','ই','ঈ','উ','ঊ','ঋ','এ',
'ঐ','ও','ঔ','অ্যা','্','য়','ঁ','ড়','়','ঃ'])

stop_words = set([''])
stop_words_file_lines=open('/content/drive/MyDrive/Thesis_450/stop_words.txt','r',encoding='utf-8-sig').readlines()
for word in stop_words_file_lines:
    stop_words.add(word.strip())

def preprocess(sentence):
    words = sentence.split()
    unique_words_per_sentence = []
    for every_word in words:
        correct_word = ''
        for each_char in every_word:
            if each_char in valid_bangla_char:
                correct_word += each_char
            else:
                correct_word = ''
        if correct_word not in stop_words:
            unique_words_per_sentence.append(correct_word.strip())
        correct_word = ''

    new_refined_sentence = ' '.join(stmr.stem(unique_words_per_sentence))

    return new_refined_sentence
data["text_clean"] = data["verse"].apply(lambda x: puncuation_removal(x))
data.head()