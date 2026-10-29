import json
import copy
from collections import deque
import heapq

class YardSearcher:
    def __init__(self, json_file_path=None):
        """
        Initialize YardSearcher by reading data from a JSON file.
        
        Args:
            json_file_path (str): Path to the JSON file containing yard, init, and goal data. Can be None.
        """

        if json_file_path:
            with open(json_file_path, 'r') as file:
                data = json.load(file)
            
            self.yard = data['yard']
            self.init = data['init']
            self.goal = data['goal']
    
    def __str__(self):
        """String representation of the YardSearcherAI object."""
        return f"YardSearcherAI:\nYard: {self.yard}\nInit: {self.init}\nGoal: {self.goal}"

    # PROBLEM 1
    def possible_actions(self, state):
        """
        Provides a list of all possible actions given a state (see project documentation).

        A State is a List[List[str]]
        An Action is a tuple[str, int, int]
        
        Args:
            state (State):  A given state.

        Returns:
            List[State] : A list of all possible actions that can be done on that state.

        """

        actions = []

        # BEGIN SOLUTION
        for left_track, right_track in self.yard:
            # Assign the left and right cars based on the current state
            left_car = state[left_track-1]
            right_car = state[right_track-1]

            # Check if the left track has an engine ('*') then add the RIGHT action to the list of possible actions
            if '*' in left_car:
                actions.append(("RIGHT", left_track, right_track))
                # If the right track has a car, then add the LEFT action to the list of possible actions
                if right_car:
                    actions.append(("LEFT", right_track, left_track))
            
            # If the right track has an engine ('*') then add the LEFT action to the list of possible actions
            elif '*' in right_car:
                actions.append(("LEFT", right_track, left_track))
                # If the left track has a car, then add the RIGHT action to the list of possible actions
                if left_car:
                    actions.append(("RIGHT", left_track, right_track))

        # END SOLUTION

        return actions

    # PROBLEM 2
    def result(self, action, state):
        """
        Consumes an action and a state and produces the state 
            that results from applying that action on the given state.

        Args:
            action (Action): The given action.
            state (State): The given state.

        Returns:
            State : The resulting state after applying "action" to "state".

        """
        resulting_state = copy.deepcopy(state)

        # BEGIN SOLUTION
        # YOUR CODE HERE
        # Unpack action tuple
        action_LR, from_state, to_state = action
        # Move from left to right
        if action_LR == "RIGHT":
            # Insert to the front of the list and remove from the end of the list
            resulting_state[to_state - 1].insert(0, resulting_state[from_state - 1][-1])
            resulting_state[from_state - 1].remove(resulting_state[from_state - 1][-1])
        # Move from right to left
        elif action_LR == "LEFT":
            # Append to the end of the list and remove from the front of the list
            resulting_state[to_state - 1].append(resulting_state[from_state - 1][0])
            resulting_state[from_state - 1].remove(resulting_state[from_state - 1][0])

        # END SOLUTION

        return resulting_state

    # PROBLEM 3
    def apply_action_sequence(self, action_sequence, state):
        """
        Consumes an action sequence and a state, and produces the state
            that results from applying the actions on a state.

        Args:
            action_sequence (List[Action]) : A list of actions.
            state (State) : The given state

        Returns:
            State : The resulting state after applying the actions in `action_sequence` 
                        on `state` in order.
        """
        resulting_state = copy.deepcopy(state)

        # BEGIN SOLUTION
        # YOUR CODE HERE
        # Loop through each action in the action sequence
        for action in action_sequence:
            # Apply the action to the current state and update the state
            resulting_state = self.result(action, resulting_state)
        # END SOLUTION

        return resulting_state

    @staticmethod
    def state_key(state):
        """
        Create a hashable, immutable representation of a nested-list state.
        """
        return tuple(tuple(track) for track in state)
    
    # PROBLEM 4
    def uninformed_search(self, init_state, goal_state):
        """
        Using an UNINFORMED search algorithm, returns an OPTIMAL sequence of 
            actions that transforms an intial state into a goal state.
            There may be multiple shortest paths, but you only need to find one.

        Args:
            init_state (State) : The initial state.
            goal_state (State) : The goal state.

        Returns:
            List[Action] : A sequence of actions that transforms the initial state into the
                goal state. The action sequence is an optimal path (e.g. a shortest path). 
                There may be multiple shortest paths, but you only need to find one.

            int : The total number of nodes explored during run of the search algorithm.

        """
        
        path = []
        nodes_explored = 0

        # BEGIN SOLUTION
        
        # YOUR CODE HERE
        # If the initial state is the same as the goal state, return an empty path and 0 nodes explored
        if init_state == goal_state:
            return [], 0

        # Initialize the frontier with the initial state and an empty path
        # Frontier is implemented as a queue (FIFO) for breadth-first search
        frontier = deque([(init_state, [])])
        visited = {self.state_key(init_state)}

        # Loop until the frontier is empty
        while frontier:
            # Pop the first state and path from the frontier
            current_state, current_path = frontier.popleft()
            nodes_explored += 1

            # Get all possible actions for the current state
            for action in self.possible_actions(current_state):
                # Get the resulting state after applying the action
                next_state = self.result(action, current_state)
                next_path = current_path + [action]

                # If the resulting state is the goal state, return the path and number of nodes explored
                if next_state == goal_state:
                    return next_path, nodes_explored

                # If the resulting state has not been visited, add it to the frontier and mark it as visited
                state_key = self.state_key(next_state)
                if state_key not in visited:
                    visited.add(state_key)
                    frontier.append((next_state, next_path))
        # END SOLUTION

        return path, nodes_explored
    
    # PROBLEM 5
    def heuristic_function(self, init_state, goal_state):
        """
        An ADMISSIBLE heuristic that returns an estimated cost between
            an intial state and a goal state.

        Args:
            init_state (State) : The initial state.
            goal_state (State) : The goal state.

        Returns:
            float : The estimated path cost between `init_state` and `goal_state`.
                This cost will never overestimate the distance from the intitial
                and goal state.

        """

        heuristic_score = 0

        # BEGIN SOLUTION
        # The heuristic function returns estimated path cost between the initial state and the goal state. 
        # The admissible heuristic function never overestimates the distance from the initial and goal state.   
        # This heuristic function calculates number of cars that are not in their goal position. 
        # For each car that is not in its goal position, we add 1 to the heuristic score. 
        # This is because each car will need at least one move to get to its goal position.
        # YOUR CODE HERE
        car_dict = {}
        
        for idx, track in enumerate(init_state):
            for car in track:
                car_dict[car] = idx

        for idx, track in enumerate(goal_state):
            for car in track:
                if car in car_dict and car_dict[car] != idx:
                    heuristic_score += 1

        # END SOLUTION


        return heuristic_score

    # PROBLEM 6
    def astar_search(self, init_state, goal_state):
        """
        Using the A* search algorithm, returns an OPTIMAL sequence of 
            actions that transforms an intial state into a goal state.
            There may be multiple shortest paths, but you only need to find one.

        Args:
            init_state (State) : The initial state.
            goal_state (State) : The goal state.

        Returns:
            List[Action] : A sequence of actions that transforms the initial state into the
                goal state. The action sequence is an optimal path (e.g. a shortest path). 
                There may be multiple shortest paths, but you only need to find one.

            int : The total number of nodes explored during run of the search algorithm.

        """

        path = []
        nodes_explored = 0

        # BEGIN SOLUTION
        
        # YOUR CODE HERE
        # If the initial state is the same as the goal state, return an empty path and 0 nodes explored
        if init_state == goal_state:
            return [], 0
        # Initialize the frontier with the initial state and an empty path
        # Frontier is implemented as a priority queue (min-heap) for A* search
        frontier = []
        heapq.heappush(frontier, (self.heuristic_function(init_state, goal_state), init_state, []))
        visited = {self.state_key(init_state)}

        # Loop until the frontier is empty
        while frontier:
            # Pop the state with the lowest cost from the frontier
            _, current_state, current_path = heapq.heappop(frontier)
            nodes_explored += 1

            # Get all possible actions for the current state
            for action in self.possible_actions(current_state):
                # Get the resulting state after applying the action
                next_state = self.result(action, current_state)
                next_path = current_path + [action]

                # If the resulting state is the goal state, return the path and number of nodes explored
                if next_state == goal_state:
                    return next_path, nodes_explored

                # If the resulting state has not been visited, add it to the frontier and mark it as visited
                state_key = self.state_key(next_state)
                if state_key not in visited:
                    visited.add(state_key)
                    cost = len(next_path) + self.heuristic_function(next_state, goal_state)
                    heapq.heappush(frontier, (cost, next_state, next_path))

        # END SOLUTION

        return path, nodes_explored

def main():
    # Feel free to edit code in the main function for your own testing purposes...
    searcher = YardSearcher("./yards/yard_1_EASY.json")
    
    path, nodes_explored = searcher.uninformed_search(searcher.init, searcher.goal)
    print("Path to goal: ", path)
    print("Length of path: ", len(path))
    print("Total number of nodes explored: ", nodes_explored)

if __name__ == "__main__":
    main()
