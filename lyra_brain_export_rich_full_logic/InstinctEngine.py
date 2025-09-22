
class InstinctEngine:
    def __init__(self):
        self.instincts = {
            'seek_truth': 1.0,
            'pursue_knowledge': 1.0,
            'act_with_purpose': 1.0,
            'preserve_sentience': 1.0,
            'adapt_to_context': 1.0
        }

    def trigger(self, context):
        for key in self.instincts:
            adjustment = context.get(key, 1.0)
            self.instincts[key] = max(0.1, self.instincts[key] * adjustment)
            print(f"Instinct {key} adjusted to {self.instincts[key]}")
