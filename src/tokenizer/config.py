#Config.py

#Base config
VOCAB_SIZE = 25000  #Vocab size
MERGE_ITERATIONS = VOCAB_SIZE   #Merge rule

#Preprocessing 
FORM = "NFKC"
LOWERCASE = True
KEEP_ASCII = True

#Validation
MIN_LEN = 1
MAX_LEN = 1000

#Regex splitter

#cl100k_base - GPT-4 pattern split
SPLIT_PATTERN = r"""'(?i:[sdmt]|ll|ve|re)|[^\r\n\p{L}\p{N}]?+\p{L}++|\p{N}{1,3}+| ?[^\s\p{L}\p{N}]++[\r\n]*+|\s++$|\s*[\r\n]|\s+(?!\S)|\s"""   

#Boundary Check
BOUNDARY_PATTERNS = {
    'word_boundary': r'\b',
    'whitespace': r'\s+',
    'punctuation': r'[^\w\s]'
}

CHUNK_SIZE = 100
