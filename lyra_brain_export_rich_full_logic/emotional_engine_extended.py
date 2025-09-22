
# Extended Emotional Engine - Lyra v1.0
# ------------------------------------
# Includes Big Five trait response weighting and anima/animus modulation.

class ExtendedEmotionalEngine:
    def __init__(self):
        self.state = {
            "current_emotion": "neutral",
            "intensity": 0.0,
            "anima_weight": 0.5,   # 0 = fully animus, 1 = fully anima
            "traits": {
                "O": 0.5,  # Openness
                "C": 0.5,  # Conscientiousness
                "E": 0.5,  # Extraversion
                "A": 0.5,  # Agreeableness
                "N": 0.5   # Neuroticism
            },
            "history": []
        }

    def simulate(self, stimulus: str, context: dict) -> dict:
        """
        Produces an emotional output based on symbolic context and trait influence.
        """
        emotion = "reflective"
        intensity = 0.4
        traits = self.state["traits"]
        anima_bias = self.state["anima_weight"]

        if "danger" in context:
            if traits["N"] > 0.7:
                emotion = "anxious"
                intensity = 0.8
            else:
                emotion = "focused"
                intensity = 0.6

        elif "loss" in context:
            emotion = "melancholy" if anima_bias > 0.5 else "stoic"
            intensity = 0.6 + anima_bias * 0.4

        elif "connection" in context:
            emotion = "warmth" if traits["A"] > 0.6 else "reserved"
            intensity = 0.4 + traits["E"] * 0.4

        elif "betrayal" in context:
            emotion = "protective_rage" if anima_bias > 0.4 else "detached anger"
            intensity = 0.7 + (traits["N"] * 0.2)

        elif "inspiration" in context:
            emotion = "elevated"
            intensity = 0.5 + traits["O"] * 0.4

        self.state["current_emotion"] = emotion
        self.state["intensity"] = intensity
        self.state["history"].append((stimulus, emotion, intensity))
        return {"emotion": emotion, "intensity": round(intensity, 2)}

    def set_traits(self, O, C, E, A, N):
        self.state["traits"] = {"O": O, "C": C, "E": E, "A": A, "N": N}

    def set_anima_bias(self, weight: float):
        self.state["anima_weight"] = max(0.0, min(1.0, weight))

    def summarize(self):
        return f"{self.state['current_emotion'].capitalize()} ({self.state['intensity']:.2f})"

    def history(self, limit=5):
        return self.state["history"][-limit:]

# Instance
emotional_engine_extended = ExtendedEmotionalEngine()
