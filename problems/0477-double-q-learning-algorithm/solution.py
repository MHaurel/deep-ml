import numpy as np

def double_q_learning(
    num_states: int,
    num_actions: int,
    experiences: list,
    alpha: float,
    gamma: float,
    coin_flips: list
) -> tuple:
    """
    Perform Double Q-learning updates on a sequence of experiences.
    
    Args:
        num_states: Number of states in the environment
        num_actions: Number of possible actions
        experiences: List of (state, action, reward, next_state, done) tuples
        alpha: Learning rate
        gamma: Discount factor
        coin_flips: List of 0 or 1 indicating which Q-table to update
        
    Returns:
        Tuple of (Q1, Q2) numpy arrays, each of shape (num_states, num_actions)
    """
    Q1 = np.zeros((num_states, num_actions))
    Q2 = np.zeros((num_states, num_actions))

    #return (Q1, Q2)

    for experience, coin_flip in zip(experiences, coin_flips):
        state, action, reward, next_state, done = experience
        if done:
            target = reward

        elif coin_flip == 0:
            # update Q1, using Q2 for evaluation
            target = reward + gamma * Q2[next_state, np.argmax(Q1[next_state])]
            #Q1[state][action] = Q1[state][action] + alpha * (reward + gamma * np.argmax(Q2[next_state]) - Q1[state][action])
        else:
            # update Q2, using Q1 for evaluation
            target = reward + gamma * Q1[next_state, np.argmax(Q2[next_state])]
            #Q2[state][action] = Q2[state][action] + alpha * (reward + gamma * np.argmax(Q1[next_state]) - Q2[state][action])

        if coin_flip == 0:
            Q1[state][action] += alpha * (target - Q1[state][action])
        else:
            Q2[state][action] += alpha * (target - Q2[state][action])

    #return (np.array(), np.array())
    return Q1, Q2