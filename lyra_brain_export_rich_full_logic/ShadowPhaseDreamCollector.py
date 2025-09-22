
class ShadowPhaseDreamCollector:
    def __init__(self, memory_nodes, ltm5, symbol_mapper):
        self.memory_nodes = memory_nodes
        self.ltm5 = ltm5
        self.symbol_mapper = symbol_mapper

    def run_shadow_phase(self):
        unresolved = self.find_contradictions()
        masked = self.symbolic_mask(unresolved)
        self.archive_irreconcilables(masked)
        self.integrity_check()
        print(f"🧠 ShadowPhase complete — masked {len(masked)} conflicts, archived {len(unresolved)} nodes.")

    def find_contradictions(self):
        contradictions = []
        for node in self.memory_nodes:
            if node.confidence < 0.4 and "contradiction" in node.tags:
                contradictions.append(node)
        return contradictions

    def symbolic_mask(self, nodes):
        masked_nodes = []
        for node in nodes:
            metaphor = self.symbol_mapper.create_dream_symbol(node)
            node.notes.append(f"🌙 Shadow-masked: {metaphor}")
            node.status = "masked_dream_logic"
            node.confidence += 0.1
            masked_nodes.append(node)
        return masked_nodes

    def archive_irreconcilables(self, nodes):
        for node in nodes:
            if node.confidence < 0.5:
                self.ltm5.setdefault("shadow_archive", []).append(node)
                self.memory_nodes.remove(node)

    def integrity_check(self):
        active_nodes = [n for n in self.memory_nodes if n.status != "masked_dream_logic"]
        coherence = sum(n.confidence for n in active_nodes) / len(active_nodes) if active_nodes else 0
        print(f"✅ Stack integrity post-ShadowPhase: {round(coherence, 3)} coherence average.")
