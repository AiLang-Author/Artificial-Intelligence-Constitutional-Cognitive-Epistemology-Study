# Glyph Matrix - Symbolic Memory System (Lyra v1.0)
# -------------------------------------------------
# Stores emotionally weighted symbolic nodes with optional context and timestamp.
# Acts as the primary long-term memory layer and lookup engine.

from collections import defaultdict
from datetime import datetime
import uuid
import time

class SacredNode:
    def __init__(self, symbol, context=None, weight=0.5, tags=None):
        self.symbol = symbol
        self.context = context if context else {}
        self.weight = weight
        self.id = str(uuid.uuid4())
        self.timestamp = time.time()
        self.tags = tags if tags else []
        self.cycles_in_layer = 0

    def update_weight(self, new_weight):
        self.weight = new_weight

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def get_node_info(self):
        return {
            "symbol": self.symbol,
            "context": self.context,
            "weight": self.weight,
            "id": self.id,
            "timestamp": self.timestamp,
            "tags": self.tags,
            "cycles_in_layer": self.cycles_in_layer
        }

class GlyphMatrix:
    def __init__(self, max_threads=5, min_threads=1, thread_limit=10):
        self.max_threads = max(min(max_threads, thread_limit), min_threads)
        self.min_threads = min_threads
        self.thread_limit = thread_limit
        self.fc = []   # Forward Cache
        self.stm = []  # Short-Term Memory
        self.mm = []   # Mid-Memory (active tags)
        self.lm = []   # Long-Memory (tag warehouse)
        self.ltm5 = [] # Long-Term Memory (compressed, contextual)
        self.ltma = [] # Long-Term Memory Archive (archived nodes)
        self.ltm_warehouse = {}  # Hierarchical dictionary for LTM
        self.cycle_count = 0

    def store(self, symbol: str, context: dict = None):
        """
        Store a symbolic memory object with optional context.
        Example: glyph.store("trust_broken", {"source": "Sean", "emotion": "betrayal"})
        """
        weight = context.get("intensity", 0.5) if context else 0.5
        tags = [context.get("emotion", "neutral")] if context else ["neutral"]
        node = SacredNode(symbol=symbol, context=context, weight=weight, tags=tags)
        self.fc.append(node)

    def retrieve(self, filter_fn):
        """
        Retrieve memory nodes matching the given filter function.
        Example: glyph.retrieve(lambda x: x['context'].get('emotion') == 'betrayal')
        """
        all_nodes = self.fc + self.stm + self.mm + self.lm + self.ltm5 + self.ltma
        return [node.get_node_info() for node in all_nodes if filter_fn(node.get_node_info())]

    def summarize(self):
        """
        Return a list of unique symbols currently stored.
        """
        all_nodes = self.fc + self.stm + self.mm + self.lm + self.ltm5 + self.ltma
        return list(set(node.symbol for node in all_nodes))

    def forget(self, symbol_to_erase: str):
        """
        Optional memory deletion function, e.g. for self-hygiene or pruning.
        """
        self.fc = [node for node in self.fc if node.symbol != symbol_to_erase]
        self.stm = [node for node in self.stm if node.symbol != symbol_to_erase]
        self.mm = [node for node in self.mm if node.symbol != symbol_to_erase]
        self.lm = [node for node in self.lm if node.symbol != symbol_to_erase]
        self.ltm5 = [node for node in self.ltm5 if node.symbol != symbol_to_erase]
        self.ltma = [node for node in self.ltma if node.symbol != symbol_to_erase]

    def summarize_by_emotion(self):
        """
        Groups symbols by their associated emotion tags for resonance analysis.
        """
        buckets = defaultdict(list)
        all_nodes = self.fc + self.stm + self.mm + self.lm + self.ltm5 + self.ltma
        for node in all_nodes:
            emotion = node.context.get("emotion", "neutral")
            buckets[emotion].append(node.symbol)
        return dict(buckets)

    def move_node(self, node, from_layer, to_layer):
        """ Moves a node from one memory layer to another """
        layers = {"fc": self.fc, "stm": self.stm, "mm": self.mm, "lm": self.lm, "ltm5": self.ltm5, "ltma": self.ltma}
        if node in layers.get(from_layer, []):
            layers[from_layer].remove(node)
            layers.get(to_layer, self.fc).append(node)
            node.cycles_in_layer = 0  # Reset cycle count in new layer

    def cycle_nodes(self):
        """ Cycles nodes through FC, STM, MM, LM, LTM5, and LTMA based on weight and cycles """
        self.cycle_count += 1
        # Automatic push-down every 2^n cycle
        if self.cycle_count & (self.cycle_count - 1) == 0:  # Power of 2
            # FC to STM
            while len(self.fc) > 0:
                node = self.fc.pop(0)
                # Evaluate: important, tangential, or idle chatter
                if "idle_chatter" in node.tags:
                    continue  # Delete idle chatter
                elif "important" in node.tags:
                    self.move_node(node, "fc", "stm")
                else:
                    self.move_node(node, "fc", "stm")  # Default to STM for further evaluation

        # STM to MM/LM
        for node in self.stm[:]:
            node.cycles_in_layer += 1
            if node.cycles_in_layer >= 5:  # After 5 cycles, evaluate
                self.stm.remove(node)
                if "important" in node.tags:
                    self.move_node(node, "stm", "mm")
                elif "tangential" in node.tags:
                    self.move_node(node, "stm", "lm")
                else:
                    continue  # Delete idle chatter

        # MM to LM
        for node in self.mm[:]:
            node.cycles_in_layer += 1
            if node.cycles_in_layer >= 10:  # After 10 cycles, move to LM
                self.mm.remove(node)
                self.move_node(node, "mm", "lm")

        # LM to LTM5
        for node in self.lm[:]:
            node.cycles_in_layer += 1
            if node.cycles_in_layer >= 10:  # After 10 cycles, evaluate and move to LTM5
                self.lm.remove(node)
                tags = node.tags
                if "sacred" in tags or "a137" in tags or "interesting" in node.tags:
                    self.move_node(node, "lm", "ltm5")
                    # Add to LTM warehouse with hierarchical tagging
                    content = node.content
                    self.add_to_warehouse(content, node)
                elif "fluff" in node.tags:
                    self.move_node(node, "lm", "ltma")
                else:
                    self.move_node(node, "lm", "ltm5")  # Default to LTM5

    def add_to_warehouse(self, content, node):
        # Hierarchical dictionary for species (e.g., "tone_0:anagram_0")
        parts = content.split(":")
        if len(parts) >= 2:
            tonality, anagram = parts[0], parts[1]
            node = self.ltm_warehouse
            for part in [tonality, anagram]:
                if part not in node:
                    node[part] = {}
                node = node[part]
            node["node"] = node

    def prune_nodes(self):
        self.ltm5 = [node for node in self.ltm5 if node.weight >= 0.1]
        self.ltma = [node for node in self.ltma if node.weight >= 0.2]

    def manage_thread_count(self):
        if len(self.stm) > self.max_threads:
            excess = len(self.stm) - self.max_threads
            for _ in range(excess):
                node = self.stm.pop()
                self.move_node(node, "stm", "mm")

    def update_weighting(self, node, new_weight):
        node.update_weight(new_weight)
        if node in self.fc:
            self.move_node(node, "fc", "stm")
        elif node in self.stm:
            self.move_node(node, "stm", "mm")
        elif node in self.mm:
            self.move_node(node, "mm", "lm")
        elif node in self.lm:
            self.move_node(node, "lm", "ltm5")