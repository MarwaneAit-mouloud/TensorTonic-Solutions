import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        
        # Define special tokens
        self.special_tokens = ["<PAD>", "<UNK>", "<BOS>", "<EOS>"]
        self.vocab_size = 0
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Builds a mapping from words to unique IDs.
        """
        # 1. Start with special tokens
        tokens = self.special_tokens.copy()
        
        # 2. Extract unique words from all texts
        unique_words = set()
        for text in texts:
            # Simple split by whitespace for word-level tokenization
            words = text.strip().split()
            unique_words.update(words)
        
        # 3. Combine and build dictionaries
        full_vocab = tokens + sorted(list(unique_words))
        
        for i, word in enumerate(full_vocab):
            self.word_to_id[word] = i
            self.id_to_word[i] = word
            
        self.vocab_size = len(full_vocab)
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to IDs. If a word isn't found, use <UNK>.
        """
        words = text.strip().split()
        # Return the ID if word exists, else the ID for <UNK>
        return [self.word_to_id.get(w, self.word_to_id["<UNK>"]) for w in words]
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert IDs back to a space-separated string.
        """
        # Return the word for the ID, or <UNK> if the ID is invalid
        return " ".join([self.id_to_word.get(i, "<UNK>") for i in ids])

# Example Usage:
# texts = ["hello world", "hello machine learning"]
# tokenizer = SimpleTokenizer()
# tokenizer.build_vocab(texts)
# encoded = tokenizer.encode("hello learning") # Output: [4, 6] (ids may vary)
