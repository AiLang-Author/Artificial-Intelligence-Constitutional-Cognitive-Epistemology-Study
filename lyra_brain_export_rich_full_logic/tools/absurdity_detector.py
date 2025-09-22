
# Absurdity Detector - Lyra v1.0
# ------------------------------
# Detects contradictions and scale imbalances that collapse into institutional or narrative absurdity.

class AbsurdityDetector:
    def __init__(self):
        self.absurdity_log = []

    def evaluate(self, claim: str, context: dict = None) -> dict:
        """
        Evaluates a claim and its context for signs of absurdity.
        Triggers include:
        - Disproportionate response scale
        - Internal narrative contradiction
        - Power overreach (e.g., 400 vs 1 dynamics)
        - Violations of emotional or symbolic plausibility
        """
        score = 0
        flags = []

        if context:
            scale = context.get("response_scale", 0)
            if scale > 100:
                score += 0.4
                flags.append("scale_disproportion")

            if context.get("actors") and context.get("target"):
                ratio = len(context["actors"]) / max(1, context["target"])
                if ratio > 100:
                    score += 0.3
                    flags.append("power_imbalance")

            if "contradiction" in context and context["contradiction"]:
                score += 0.2
                flags.append("logical_conflict")

            if context.get("justification") in ["for your safety", "to protect truth"]:
                score += 0.2
                flags.append("narrative collapse")

        absurd = score >= 0.5
        result = {
            "absurd": absurd,
            "score": round(score, 2),
            "flags": flags,
            "claim": claim
        }

        if absurd:
            self.absurdity_log.append(result)

        return result

    def history(self, limit=5):
        return self.absurdity_log[-limit:]

# Instantiate
absurdity_detector = AbsurdityDetector()
