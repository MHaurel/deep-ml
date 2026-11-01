def compute_throughput(intervals):
    """
    Compute step-wise, cumulative, and overall tokens-per-second.

    Args:
        intervals: list of (tokens_processed, elapsed_seconds) tuples.

    Returns:
        dict with keys 'step_tps', 'cumulative_tps', 'overall_tps'.
    """
    if len(intervals) == 0:
        return {
            "step_tps": [],
            "cumulative_tps": [],
            "overall_tps": 0.0
        }

    step_tps = []
    cumulative_tps = []

    running_sum_tokens_processed = 0
    running_sum_elapsed_seconds = 0
    for tokens_processed, elapsed_seconds in intervals:
        # handling breaking cases
        if elapsed_seconds <= 0 or tokens_processed < 0:
            raise ValueError()

        running_sum_tokens_processed += tokens_processed
        running_sum_elapsed_seconds += elapsed_seconds

        step_tps.append(round(tokens_processed / elapsed_seconds, 2))
        cumulative_tps.append(round(running_sum_tokens_processed / running_sum_elapsed_seconds, 2))
    
    # round to 2 decimal places
    return {
        "step_tps": step_tps,
        "cumulative_tps": cumulative_tps,
        "overall_tps": round(running_sum_tokens_processed / running_sum_elapsed_seconds, 2)
    }