# Building a simple text tokeniser for text pre-processing

# Lossy Normalisation of data
def is_whitespace(char):
    return char in [' ','\t','\n','\r']

def is_alpha_numeric(char):
    return ('a'<=char<='z')

def is_digit(char):
    return '0' <= char <= '9'

# Sentence tokeniser
def tokenise_sentence(sentence_char):
    tokens = []
    i=0
    while i< len(sentence_char):
        char = sentence_char[i]
        
        if(is_whitespace(char)):
            start = i
            while i<len(sentence_char) and is_whitespace(sentence_char[i]):
                i+=1
            tokens.append("".join(sentence_char[start:i]))
            
        elif is_alpha_numeric:
            start = i
            while i<len(sentence_char) and is_alpha_numeric(sentence_char[i]):
                i+=1
            tokens.append("".join(sentence_char[start:i]))
            
        else:
            tokens.append(char)
            i+=1
        
    return tokens

def sentence_segmentation(text_char):
    sentence = []
    sentence_start = 0
    for i, char in enumerate(text_char):
        if char in ['.','!','?']:
            sentence.append(text_char[sentence_start: i+1])
            sentence_start = i+1
    if sentence_start < len(text_char):
        sentence.append(text_char[sentence_start:])
    return sentence

def lower_case(tokens):
    return [token.lower() for token in tokens]

def remove_stop_words(tokens, stop_words):
    return [token for token in tokens if token.lower() not in stop_words]

def simple_stemming(token):
    if token.endswith('ing'):
        return token[:-3]
    elif token.endswith('s'):
        return token[:-1]
    return token

def count_token_freq(tokens):
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token,0) + 1
    return freq

def process_file(file_path, stop_words):
    try:
        with open(file_path, 'r', encoding = 'utf-8') as file:
            text_char = []
            while True:
                char = file.read(1)
                if not char:
                    break
                text_char.append(char)
            
            sentences = sentence_segmentation(text_char)
            all_tokens = []
            for sentence_chars in sentences:
                tokens = tokenise_sentence(sentence_chars)
                tokens = lower_case(tokens)
                tokens = remove_stop_words(tokens, stop_words)
                tokens = [simple_stemming(token) for token in tokens]
                all_tokens.extend(tokens)
                
            frequency = count_token_freq(all_tokens)
            return all_tokens, frequency
    
    except FileNotFoundError:
        return [], {}
    





