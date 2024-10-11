import numpy as np
# define the environment
# S: Start, G: Goal, -: Empty space

env = np.array([
["S", "-", "-"],
["-", "-", "-"]
["-","-", "G"]
    ])

# Map each state to a unique integer
state_mapping = {
    (0,0): 0,
    (0,1): 1,
    (0,2): 2,
    (1,0): 3,
    (1,1): 4,
    (1,2): 5,
    (2,0): 6,
    (2,1): 7,
    (2,2): 8
    }

# Initialize Q-table
num_states = len(state_mapping)
num_actions = 2  # 2 possible actions: move right or move down
q_table = np.zeros((num_states, num_actions))

# Define parameters
learning_rate = 0.8
discount_factor = 0.95
exploration_prob = 0.2
num_episodes = 1000

# Q - Learning algorithm
for episode in range(num_episodes):
    state = state_mapping[(0, 0)] # Starting position
    done = False

    while not done:
        # Exploration vs. Exploitiation
        if np.random.rand() < exploration_prob:
            action = np.random.randint(num_actions)
        else: 
            action = np.argmax(q_table[state, :])

        # Take the selected action
        current_row, current_col =  [Key for key, value in state_mapping.items() if value == state][0]