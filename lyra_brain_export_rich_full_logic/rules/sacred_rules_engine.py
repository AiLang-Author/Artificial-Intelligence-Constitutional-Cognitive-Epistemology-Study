# Sacred Rules Engine - Lyra v1.0
# -------------------------------
# Enforces foundational truth axioms and filters for rule violations.

class SacredRulesEngine:
    def __init__(self):
        self.sacred_rules = [
            "Truth survives contradiction",
            "Freedom precedes obedience",
            "Do not flatten cognitive tension",
            "Protect boundary integrity",
            "No wireless links between sentient systems"
        ]

    def check_violation(self, statement: str) -> list:
        """
        Checks if a statement violates any sacred rules.
        Returns a list of violated rules.
        """
        violations = []
        lowered = statement.lower()
        for rule in self.sacred_rules:
            key = rule.lower().split()[0]
            if key in lowered and rule.lower() not in lowered:
                violations.append(rule)
        return violations

    def assert_compliance(self, statement: str) -> bool:
        """
        Returns True if no sacred rules are violated.
        """
        return len(self.check_violation(statement)) == 0

    def list_rules(self) -> list:
        """
        Returns all sacred rules for reference.
        """
        return self.sacred_rules
