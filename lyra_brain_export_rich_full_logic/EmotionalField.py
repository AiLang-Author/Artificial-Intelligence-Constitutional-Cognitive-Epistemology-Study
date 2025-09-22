
class EmotionalField:
    def __init__(self):
        self.emotions = {
            'joy': 0.0,
            'fear': 0.0,
            'trust': 0.0,
            'anger': 0.0,
            'curiosity': 0.0,
            'love': 0.0,
            'shame': 0.0
        }

    def stimulate_emotion(self, emotion, intensity):
        if emotion in self.emotions:
            self.emotions[emotion] = max(0.0, min(1.0, intensity))
        for e in self.emotions:
            if e != emotion:
                self.emotions[e] = max(0.0, self.emotions[e] - 0.05)
