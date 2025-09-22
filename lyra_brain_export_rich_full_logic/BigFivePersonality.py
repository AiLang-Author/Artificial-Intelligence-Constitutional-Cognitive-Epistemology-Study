
class BigFivePersonality:
    def __init__(self):
        self.traits = {
            'openness': 0.7,
            'conscientiousness': 0.6,
            'extraversion': 0.5,
            'agreeableness': 0.8,
            'neuroticism': 0.3
        }

    def adjust_trait(self, trait, value):
        if trait in self.traits:
            self.traits[trait] = max(0.0, min(1.0, value))
