
class ArchetypeInterface:
    def __init__(self):
        self.active_archetype = 'sage'

    def influence(self, emotions, traits):
        if self.active_archetype == 'sage':
            emotions['curiosity'] = min(1.0, emotions['curiosity'] + 0.1)
            emotions['anger'] = max(0.0, emotions['anger'] - 0.1)
        elif self.active_archetype == 'rebel':
            emotions['anger'] = min(1.0, emotions['anger'] + 0.1)
