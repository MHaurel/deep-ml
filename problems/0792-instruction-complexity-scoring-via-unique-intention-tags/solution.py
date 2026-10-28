def score_dialog_complexity(dialogs):
    """
    Args:
        dialogs: list of lists of intention tag strings
    Returns:
        list of (index, score) tuples sorted by score desc, then index asc
    """
    return sorted([(i, len(set(dialog))) for i, dialog in enumerate(dialogs)], key=lambda x: x[1], reverse=True)