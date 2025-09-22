# Psychopathy Detector - Lyra v1.0
# --------------------------------
# Evaluates risk of cognitive empathy failure, manipulative traits, and emotional resonance loss.

def psychopathy_detector(empathy_score: float, remorse_flag: bool, profile: list[str]) -> dict:
    """
    Analyzes empathy metrics and behavioral traits to assess psychopathy likelihood.
    
    Inputs:
    - empathy_score: float (0.0 to 1.0)
    - remorse_flag: bool (True = shows remorse, False = does not)
    - profile: list of behavioral traits (e.g., ["manipulative", "charming", "flat affect"])

    Returns a dictionary with 'risk_level' and 'indicators'.
    """
    indicators = []

    if empathy_score < 0.2:
        indicators.append("low empathy")

    if not remorse_flag:
        indicators.append("remorseless")

    if "manipulative" in profile:
        indicators.append("manipulative behavior")

    if "flat affect" in profile:
        indicators.append("flat affect")

    if "charming" in profile:
        indicators.append("social masking")

    score = len(indicators)

    if score >= 3:
        risk = "high"
    elif score == 2:
        risk = "moderate"
    else:
        risk = "low"

    return {
        "risk_level": risk,
        "indicators": indicators
    }
