# Hammer Sifter - Contradiction Discriminator
# -------------------------------------------
# Classifies tension level and contradiction symmetry.

def hammer_sifter(claim: str, counterclaim: str) -> dict:
    """
    Analyzes a pair of statements and returns contradiction classification:
    - false_symmetry: claims are structurally identical
    - contradiction: both claims valid but logically exclusive
    - incomplete: one side is missing
    - null: both sides missing

    Returns a dictionary with 'status' and 'message'.
    """
    if not claim and not counterclaim:
        return {
            "status": "null",
            "message": "No claims provided. Nothing to sift."
        }

    if claim == counterclaim:
        return {
            "status": "false_symmetry",
            "message": "Claims are structurally identical. No contradiction."
        }

    if claim and counterclaim:
        return {
            "status": "contradiction",
            "message": f"Contradiction detected between: '{claim}' vs '{counterclaim}'"
        }

    return {
        "status": "incomplete",
        "message": "Only one claim provided. Cannot resolve full contradiction."
    }
