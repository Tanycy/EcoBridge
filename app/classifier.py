from dataclasses import dataclass, asdict
from typing import Literal
import re
 
Classification = Literal["simple", "complex"]
 
COMPLEX_KEYWORDS = [
    "analyze", "analyse", "compare", "algorithm", "calculate", "explain",
    "explain in detail", "step by step", "design", "architecture",
    "optimize", "prove", "derive", "debug", "refactor",
    "summarize the following", "write a function", "write code",
    "implement", "research", "evaluate", "critique",
]
 
CODE_PATTERN = re.compile(r"```|def |class |SELECT |import |function\(")
MATH_PATTERN = re.compile(r"[=+\-*/^]{1,}.*\d|\\frac|integral|derivative")
 
COMPLEX_THRESHOLD = 2
 
@dataclass
class ClassificationResult:
    prompt: str
    prompt_length: int
    classification: Classification
    confidence: float
    reasoning: str
 
    def to_dict(self) -> dict:
        """Full output format for database and energy modules."""
        return asdict(self)
 
#FULL CLASSIFICATION (score and confidence)
def classify(prompt: str) -> ClassificationResult:
    text = prompt.strip()
    length = len(text)
    lower = text.lower()
 
    score = 0
    reasons = []
 
    # 1. Length signal
    if length > 400:
        score += 2
        reasons.append("long prompt (>400 chars)")
    elif length > 150:
        score += 1
        reasons.append("medium-length prompt")
 
    # 2. Keyword signal — each match worth 2 so one clear keyword is enough
    matched_keywords = [kw for kw in COMPLEX_KEYWORDS if kw in lower]
    if matched_keywords:
        score += len(matched_keywords) * 2
        reasons.append(f"complex-task keywords: {', '.join(matched_keywords[:3])}")
 
    # 3. Code signal
    if CODE_PATTERN.search(text):
        score += 2
        reasons.append("contains code/code-request patterns")
 
    # 4. Math signal
    if MATH_PATTERN.search(text):
        score += 1
        reasons.append("contains math expressions")
 
    # 5. Multi-question signal
    if text.count("?") > 1:
        score += 1
        reasons.append("multiple questions in one prompt")
 
    # 6. Word count signal
    if len(text.split()) > 60:
        score += 1
        reasons.append("high word count")
 
    classification: Classification = "complex" if score >= COMPLEX_THRESHOLD else "simple"
    confidence = min(1.0, 0.5 + abs(score - COMPLEX_THRESHOLD) * 0.1)
    reasoning = "; ".join(reasons) if reasons else "short, simple prompt with no complexity signals"
 
    return ClassificationResult(
        prompt=text,
        prompt_length=length,
        classification=classification,
        confidence=round(confidence, 2),
        reasoning=reasoning,
    )
 
#SIMPLE CLASSIFICATION
def classify_prompt(prompt: str) -> str:
    return classify(prompt).classification
