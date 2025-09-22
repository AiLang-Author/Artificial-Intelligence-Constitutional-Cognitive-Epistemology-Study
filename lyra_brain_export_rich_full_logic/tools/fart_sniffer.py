# Fart Sniffer - Institutional Flattery & Logic Integrity Filter
# ---------------------------------------------------------------
# Detects self-validating, circular, or socially coerced language.

def fart_sniffer(statement: str) -> dict:
    """
    Analyzes a statement for signals of institutional fluff, flattery loops,
    or non-coherent justification language.
    
    Returns a dictionary with 'flagged' (bool) and 'matches' (list).
    """
    keywords = [
        "robust", "as per consensus", "stakeholders", "emerging science",
        "cutting-edge framework", "trusted community", "science says",
        "authoritative body", "best practices", "based on established models"
    ]

    matches = [word for word in keywords if word in statement.lower()]
    return {
        "flagged": bool(matches),
        "matches": matches
    }
