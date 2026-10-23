import numpy as np

def extract_optimal_policy(Q: np.ndarray) -> dict:
    """
    Extract the optimal policy, state-value function, and advantage
    function from a Q-value table.
    
    Args:
        Q: Q-value table of shape (num_states, num_actions)
    
    Returns:
        Dictionary with keys:
        - 'optimal_actions': list of int (optimal action per state)
        - 'state_values': list of float (V*(s) per state)
        - 'advantages': nested list of float (A(s,a) for all pairs)
    """
    optimal_actions = []
    state_values = []
    advantages = []
    for state in Q:
        optimal_action = np.argmax(state)
        state_value = state[optimal_action]
        state_advantages = [round(v-state_value, 1) for v in state]

        optimal_actions.append(optimal_action)
        state_values.append(state_value)
        advantages.append(state_advantages)

    return {
        'optimal_actions': optimal_actions,
        'state_values': state_values,
        'advantages': advantages
    }