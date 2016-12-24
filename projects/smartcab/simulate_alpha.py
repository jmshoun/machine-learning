import random
import numpy as np

# Given an action, simulate the reward associated with the action
def reward(action):
    baseline = 2 * random.random() - 1 # Random uniform noise
    penalty = 0.25 * random.random() # Rough approx. of deadline penalty
    if action == 0: # Correct action
        return 2 + baseline - penalty
    elif action < 3: # Wrong turn
        return 1 + baseline - penalty
    else: # Standing still
        return baseline - 5

# Given a number of observations and a value of alpha, stochastically
# simulate the truncated Q-Learner update rule. 
def learn(num_observations, alpha):
    weights = [0.0] * 4
    for o in range(num_observations):
        action = random.randint(0, 3)
        r = reward(action)
        weights[action] = weights[action] + alpha * (r - weights[action])

    return weights.index(max(weights))

# Given a number of trials, call learn num_trials time and count the 
# number of times the learner learns the true optimal action.
def learning_accuracy(num_trials, num_observations, alpha):
    results = [0] * 4
    for t in range(num_trials):
        results[learn(num_observations, alpha)] += 1
    return results

# Simulate a few different values of alpha.
for alpha in np.arange(0.1, 1.0, 0.1):
    results = learning_accuracy(10000, 20, alpha)
    print [round(alpha, 1), 20] + results

