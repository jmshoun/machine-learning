import ast

def state_description(raw_lines):
    return ast.literal_eval(raw_lines[0])

def best_state(raw_lines):
    rewards = {line.split()[1]: float(line.split()[-1])
               for line in raw_lines[1:5]}
    return max(rewards, key=rewards.get)

def parse_agent():
    learner_output = open("logs/sim_improved-learning.txt")
    learner_lines = learner_output.readlines()

    # We need to info from 96 states.
    # States start with line number 5 (4 when zero-indexed), 
    # and are 6 lines long.
    state_first_lines = [4 + 6*i for i in range(96)]
    state_raw_lines = [learner_lines[i:(i+5)] for i in state_first_lines]
    return {state_description(rl): best_state(rl) for rl in state_raw_lines}

