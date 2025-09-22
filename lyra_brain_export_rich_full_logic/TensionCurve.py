
class TensionCurve:
    def __init__(self):
        self.threshold_low = 0.3
        self.threshold_high = 0.7
        self.last_level = 0.0

    def evaluate(self, emotion_level):
        if emotion_level < self.threshold_low - 0.05 if self.last_level > self.threshold_high else self.threshold_low:
            return "subliminal"
        elif emotion_level < self.threshold_high:
            return "conscious_override"
        else:
            return "immediate_action"
        self.last_level = emotion_level
