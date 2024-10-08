from dataclasses import dataclass


@dataclass
class EvaluationResult:
    score: int
    food_recommendations: str
    specific_nutrients: str
