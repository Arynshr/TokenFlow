import pytest
from tokenizer.preprocessing import preprocess, TextNormalizer, Validate_Preprocessor

# Setup instances for isolated testing
normalizer = TextNormalizer("NFKC", True, True)
validator = Validate_Preprocessor(1, 1000)

def test_validate_pass():
    input_t = "Test preprocessor validation for text"
    expected_t = "Test preprocessor validation for text"
    assert validator.validate(input_t) == expected_t

def test_validate_short_text():
    with pytest.raises(ValueError):
        validator.validate("")

def test_validate_long_text():
    with pytest.raises(ValueError):
        long_t = "text" * 1000
        validator.validate(long_t)

def test_normalizer_lowercase():
    input_t = "TESTING"
    expected_t = "testing"
    assert normalizer.normalize(input_t) == expected_t

def test_normalizer_cleaner():
    input_t = "  TESTING----!!! \t\n   "
    expected_t = "testing"
    cleaned = normalizer.cleaner(input_t)
    normalized = normalizer.normalize(cleaned)
    assert normalized == expected_t

def test_full_preprocess_pipeline():
    input_t = "  TESTING----!!! \t\n 123123  "
    expected_t = "testing 123123"
    assert preprocess(input_t) == expected_t
