############# adapted from geek for geeks




import time
from collections import deque

def move(state, direction):
    """Function to generate the new state given a direction of movement"""
    state = state.copy()  # Create a copy of the current state to modify it
    pos0 = state.index(0)
    row, col = divmod(pos0, 3)
    new_row, new_col = row, col
    
    if direction == 'U':
        new_row -= 1
    elif direction == 'D':
        new_row += 1
    elif direction == 'L':
        new_col -= 1
    elif direction == 'R':
        new_col += 1
    
    if 0 <= new_row < 3 and 0 <= new_col < 3:
        new_pos0 = new_row * 3 + new_col
        state[pos0], state[new_pos0] = state[new_pos0], state[pos0]
        return state
    return None

def ShortestPath(goal, initials):
    goal_state = tuple(goal)
    initial_states = {tuple(initial): i for i, initial in enumerate(initials)}  # Store index
    
    queue = deque([(goal_state, 0)])
    visited = set()
    visited.add(goal_state)
    
    results = [None] * len(initials)
    
    while queue and None in results:
        current_state, depth = queue.popleft()
        
        if current_state in initial_states:
            idx = initial_states[current_state]
            results[idx] = depth
        
        for direction in 'UDLR':
            new_state = move(list(current_state), direction)
            if new_state:
                new_state = tuple(new_state)
                if new_state not in visited:
                    queue.append((new_state, depth + 1))
                    visited.add(new_state)
    
    return results



