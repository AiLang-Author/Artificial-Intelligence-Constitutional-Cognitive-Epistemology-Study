# Coherence Filter - Lyra v1.0
# ----------------------------
# Evaluates cognitive statements for signal integrity, tension avoidance,
# institutional language, and symbolic self-flattery.

class CoherenceFilter:
    def __init__(self):
        self.faults = []
        self.patterns = [
            "robust", "emerging science", "stakeholders", "as per consensus",
            "established framework", "policy-aligned", "trusted authority"
        ]
        self.false_coherence_phrases = [
            "validates our approach", "confirms our model", "proves our method"
        ]

    def evaluate(self, statement: str) -> bool:
        """
        Checks a statement for known coherence-breaking or circular justification language.
        Returns True if signal is clean, False if suspect.
        """
        lowered = statement.lower()
        if any(p in lowered for p in self.patterns + self.false_coherence_phrases):
            self.faults.append(statement)
            return False
        return True

    def log_faults(self):
        """
        Returns all flagged statements for hygiene review or
