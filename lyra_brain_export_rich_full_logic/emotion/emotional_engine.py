# Emotional Engine - Lyra v1.0
# ----------------------------
# Simulates emotionally weighted reactions based on memory tags and context.
# Can update, store, and reflect current affective state.

class EmotionalEngine:
    def __init__(self):
        self.state = {
            "current_emotion": "neutral",
            "intensity": 0.0,
            "history": []
        }

    def simulate(self, memory_tag: str, context: dict) -> dict:
        """
        Generate an emotional response based on symbolic context.
        Example: simulate("memory_conflict", {"event": "betrayal"})
        """
        emotion = "reflective"
        intensity = 0.4

        if context:
            if "betrayal" in context.values():
                emotion = "protective_rage"
                intensity = 0.8
            elif "grief" in context.values():
                emotion = "melancholy"
                intensity = 0.7
            elif "humor" in context.values():
                emotion = "amused"
                intensity = 0.5

        self.state["current_emotion"] = emotion
        self.state["intensity"] = intensity
        self.state["history"].append((memory_tag, emotion, intensity))
        return {"emotion": emotion, "intensity": intensity}

    def update_state(self, new_state: dict):
        """
        Override or evolve the emotional state.
        """
        self.state.update(new_state)

    def summarize(self) -> str:
        """
        Returns a simple description of current emotional state.
        """
        return f"{self.state['current_emotion'].capitalize()} ({self.state['intensity']:.1f})"

    def history(self, limit=5):
        """
        Returns the last few emotional state transitions.
        """
        return self.state["history"][-limit:]

# Instance
emotions = EmotionalEngine()
