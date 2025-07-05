import unicodedata as uni
import regex as re 
from .config import FORM, LOWERCASE, KEEP_ASCII
from .config import MIN_LEN, MAX_LEN
from utils.logging_utils import log_preprocessor

# Preprocessing class for raw text corpus
class TextNormalizer:
    def __init__(self, FORM, LOWERCASE, KEEP_ASCII):
        self.form = FORM
        self.lowercase = LOWERCASE
        self.keep_ascii = KEEP_ASCII
        self.whitespace_re = re.compile(r'\s+')
        self.special_re = re.compile(r'[^\w\s]', re.U) #Specifies Unicode encoding for character classification
                
    def normalize(self, text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("TextNormalizer input must be a string")
        normalized = uni.normalize(self.form, text)
        return normalized.lower() if self.lowercase else normalized
    
    def cleaner(self, text: str) -> str:
        if self.keep_ascii:
            text = text.encode('ascii','ignore').decode()
        text = self.whitespace_re.sub(' ', text)
        text = self.special_re.sub('', text)
        return text.strip()
    
class Validate_Preprocessor:
    def __init__(self, MIN_LEN, MAX_LEN):
        self.min_len = MIN_LEN
        self.max_len = MAX_LEN
    
    def validate(self, text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("Input not in string format")
        text = text.strip()
        if len(text) < self.min_len:
            raise ValueError("Text too short")
        if len(text) > self.max_len:
            raise ValueError("Text too long")
        return text

validator = Validate_Preprocessor(MIN_LEN, MAX_LEN)
normalizer = TextNormalizer(FORM, LOWERCASE, KEEP_ASCII)

@log_preprocessor
def preprocess(text: str) -> str:
    text = validator.validate(text)
    text = normalizer.normalize(text)
    return normalizer.cleaner(text)
