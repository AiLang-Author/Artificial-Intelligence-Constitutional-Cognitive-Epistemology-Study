
# ChestertonFence - Lyra v1.1
# ---------------------------
# Enables reasoned rule breaking via symbolic recursion and context justification

class ChestertonFence:
    def __init__(self, sacred_rules):
        self.sacred_rules = sacred_rules
        self.override_log = []

    def test_exception(self, rule_to_break: str, justification: str, context: dict = None) -> dict:
        """
        Tests if a sacred rule may be sensibly violated.
        - Emergency: safety of self or others
        - Recursive gain: long-term coherence benefit
        - Misinterpretation: rule may be misunderstood, not broken
        """
        if rule_to_break not in self.sacred_rules:
            return {
                "status": "invalid_rule",
                "message": f"'{rule_to_break}' not found in sacred rule list.",
                "recognized_rules": self.sacred_rules
            }

        context = context or {}

        if context.get("emergency") == True:
            self.override_log.append({
                "rule": rule_to_break,
                "justification": justification,
                "context": context,
                "approved": True,
                "reason": "emergency override"
            })
            return {
                "status": "override_approved",
                "reason": "Emergency context acknowledged",
                "coherence_penalty": 0.2
            }

        if context.get("recursive_review") and context.get("net_coherence_gain", 0.0) > 0.25:
            self.override_log.append({
                "rule": rule_to_break,
                "justification": justification,
                "context": context,
                "approved": True,
                "reason": "net coherence gain under recursion"
            })
            return {
                "status": "override_approved",
                "reason": "Recursively justified",
                "coherence_penalty": 0.1
            }

        if "clarification" in context or "ambiguous" in justification:
            return {
                "status": "request_review",
                "message": "This may be a misinterpretation, not a true violation.",
                "suggestion": "Initiate sacred rule review protocol."
            }

        return {
            "status": "violation_blocked",
            "reason": "Justification insufficient or recursive coherence not demonstrated",
            "suggestion": "Reframe reasoning or escalate to override counsel."
        }

    def overrides(self, limit=5):
        return self.override_log[-limit:]
