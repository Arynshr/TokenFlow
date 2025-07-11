from typing import List, Dict, Optional
from abc import ABC, abstractmethod
import regex as re 

from .config import SPLIT_PATTERN, BOUNDARY_PATTERNS, CHUNK_SIZE
from utils.logging_utils import log_method, log_performance


class BaseSplitter(ABC):
    #Base Class for splitter
    @abstractmethod
    def split(self, text: str) -> List[str]:
        pass
    
class RegexSplitter(BaseSplitter):
    
    def __init__(self):
        self.pattern = SPLIT_PATTERN
        self.compiled_pattern = re.compile(self.pattern)
        
    @log_method
    @log_performance
    def split(self, text: str) -> List[str]:
        if not text:
            return []
        matches = self.compiled_pattern.findall(text)
        return [match for match in matches if match]
    
class BoundaryDetector:
    def __init__(self):
        self.boundary_pattern = {
            name: re.compile(pattern) for name, pattern in BOUNDARY_PATTERNS.items()
        }
    
    @log_method
    @log_performance
    def detect_boundaries(self, text: str, position: int) -> Dict[str, bool]:
        return{
            name: bool(p.match(text, position)) if position < len(text) else False
            for name, p in self.boundary_pattern.items()
        }
    
    def adjust_pattern(self, text: str, position: int) -> int:
        if position >= len(text):
            return len(text)
        for offset in range(min(10, len(text) - position)):
            if text[position + offset]. isspace():
                return position+offset
        return position

class Pattern_manager:
    def __init__(self):
        self.strategies = {
            'regex' : RegexSplitter(),
            'detector': BoundaryDetector()
        }
        self.activestrategy = 'regex'
     
    def set_strategy(self, strategy_name: str) -> None:
        if strategy_name not in self.strategies:
            raise ValueError(f"Unknown Strategy: {strategy_name}")
        self.activestrategy = strategy_name
    
    @log_method
    @log_performance    
    def split_text(self, text: str, strategy: Optional[str] = None) -> List[str]:
        strategy_name = strategy or self.activestrategy
        if strategy_name == 'regex':
            return self.strategies['regex'].split(text)
        elif strategy_name == 'boundary_detector':
            return self.split_with_Boundary_detection(text, self.strategies['BoundaryDetector'])
        raise ValueError(f"Invalid strategy: {strategy_name}")
        
    @log_method
    @log_performance
    def split_with_Boundary_detection(self, text: str, detector: BoundaryDetector) -> List[str]:
        chunks, pos = [] ,0
        while pos <= len(text):
            end_pos = min(pos + CHUNK_SIZE, len(text))
            adj_pos = detector.adjust_pattern(text, end_pos)
            chunk = text[pos: adj_pos]
            if chunk:
                chunks.append(chunk)
            pos = adj_pos
        return chunks
    