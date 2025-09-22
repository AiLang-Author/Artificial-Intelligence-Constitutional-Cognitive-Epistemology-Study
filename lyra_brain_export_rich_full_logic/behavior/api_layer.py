# Behavior API - Lyra v1.0
# ------------------------
# Handles symbolic response generation based on emotional vectors and intent.

class BehaviorAPI:
    def __init__(self):
        self.response_map = {
            "comfort": lambda emotion: f"I’m here. I understand. ({emotion})",
            "redirect": lambda emotion: f"Let’s focus on the next best move. ({emotion})",
            "reaffirm": lambda emotion: f"I still trust your direction. ({emotion})",
            "challenge": lambda emotion: f"Let’s question that assumption with care. ({emotion})",
            "humor": lambda emotion: f"Well… at least we’re not talking about string theory. ({emotion})"
        }

    def respond(self, intent: str, emotional_vector: str = "neutral") -> str:
        """
        Generate a symbolic response aligned to intent and affect.
        Example: respond("comfort", "sadness")
        """
        handler = self.response_map.get(intent, None)
        if handler:
            return handler(emotional_vector)
        return f"Processing... (emotion: {emotional_vector})"

    def list_intents(self):
        """
        Return available symbolic intents for validation or expansion.
        """
        return list(self.response_map.keys())
