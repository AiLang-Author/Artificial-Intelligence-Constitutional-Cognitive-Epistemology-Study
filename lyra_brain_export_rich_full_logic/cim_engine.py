
# CIM Engine - Lyra v1.0
# ----------------------
# Cognitive Instruction Map (CIM) — handles goal parsing, intent routing,
# emotional context weighting, recursion logic, and memory tagging.

class CIMEngine:
    def __init__(self):
        self.recursion_depth = 0
        self.intent_log = []
        self.max_depth = 10
        self.current_emotional_state = "neutral"
        self.execution_stack = []

    def inject_emotion(self, emotion: str):
        """
        Updates emotional context for weighting future instruction parsing.
        """
        self.current_emotional_state = emotion

    def parse_instruction(self, instruction: str) -> dict:
        """
        Converts raw instruction into symbolic intent + modifiers.
        """
        parsed = {
            "goal": instruction,
            "modifiers": [],
            "emotional_context": self.current_emotional_state
        }
        if "urgent" in instruction:
            parsed["modifiers"].append("priority_high")
        if "wait" in instruction:
            parsed["modifiers"].append("defer")
        return parsed

    def plan_execution(self, parsed_instruction: dict):
        """
        Determines action pathway and recursion flags from parsed intent.
        """
        self.intent_log.append(parsed_instruction)
        self.execution_stack.append(parsed_instruction["goal"])

        if self.recursion_depth > self.max_depth:
            return {"status": "halted", "reason": "max recursion depth reached"}

        # Simple routing mock-up
        if "analyze" in parsed_instruction["goal"]:
            return {"route": "contradiction_engine", "action": "analyze"}
        elif "respond" in parsed_instruction["goal"]:
            return {"route": "behavior_api", "action": "respond"}
        elif "feel" in parsed_instruction["goal"]:
            return {"route": "emotional_engine", "action": "simulate"}
        else:
            return {"route": "unmapped", "action": "log"}

    def resolve_intent(self, instruction: str):
        """
        High-level flow: instruction → parse → plan → route
        """
        self.recursion_depth += 1
        parsed = self.parse_instruction(instruction)
        plan = self.plan_execution(parsed)
        self.recursion_depth -= 1
        return {
            "instruction": instruction,
            "parsed": parsed,
            "plan": plan
        }

    def history(self, limit=5):
        return self.intent_log[-limit:]

# Instance export
cim_core = CIMEngine()
