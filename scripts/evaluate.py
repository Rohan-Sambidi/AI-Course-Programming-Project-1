import problem 
from node import Node
from priority_queue import PriorityQueue
import time

class SearchTimeOutError(Exception):
    pass

def compute_g(algorithm, node, goal_state):
    """
        Evaluates the g() value.

        Parameters
        ===========
            algorithm: str
                The algorithm type based on which the g-value will be computed.
            node: Node
                The node whose g-value is to be computed.
            goal_state: State
                The goal state for the problem.

        Returns
        ========
            int
                The g-value for the node.
    """

    if algorithm == "bfs":
    	return 0

    if algorithm == "astar":

        return node.get_total_action_cost()

    elif algorithm == "gbfs":

        return 0

    elif algorithm == "ucs":

        return node.get_total_action_cost()

    elif algorithm == "custom-astar":

        return node.get_total_action_cost()

    # Should never reach here.
    assert False
    return float("inf")


def compute_h(algorithm, node, goal_state):
    """
        Evaluates the h() value.

        Parameters
        ===========
            algorithm: str
                The algorithm type based on which the h-value will be computed.
            node: Node
                The node whose h-value is to be computed.
            goal_state: State
                The goal state for the problem.

        Returns
        ========
            int
                The h-value for the node.
    """

    if algorithm == "bfs":
        
        return 0

    if algorithm == "astar":

        return get_manhattan_distance(node.get_state(), goal_state)

    elif algorithm == "gbfs":

        return get_manhattan_distance(node.get_state(), goal_state)

    elif algorithm == "ucs":
        
        return 0

    elif algorithm == "custom-astar":

        return get_custom_heuristic(node.get_state(), goal_state)

    # Should never reach here.
    assert False
    return float("inf")


def get_manhattan_distance(from_state, to_state):
    return abs(from_state.x - to_state.x) + abs(from_state.y - to_state.y)


def get_custom_heuristic(from_state, to_state):
    return ((from_state.x - to_state.x)**2 + (from_state.y - to_state.y)**2)**0.5

def graph_search(algorithm, time_limit):
    """
        Performs a search using the specified algorithm.
        
        Parameters
        ===========
            algorithm: str
                The algorithm to be used for searching.
            time_limit: int
                The time limit in seconds to run this method for.
                
        Returns
        ========
            tuple(list, int)
                A tuple of the action_list and the total number of nodes
                expanded.
    """
    
    # The helper allows us to access the problem functions.
    helper = problem.Helper()
    
    # Get the initial and the goal states.
    init_state = helper.get_initial_state()
    goal_state = helper.get_goal_state()[0]

    #Initialize the init node of the search tree and compute its f_score
    init_node = Node(init_state, None, 0, None, 0)
    f_score = compute_g(algorithm, init_node, goal_state) \
        + compute_h(algorithm, init_node, goal_state)

       
    # Initialize the fringe as a priority queue.
    priority_queue = PriorityQueue()
    priority_queue.push(f_score, init_node)
    

    # action_list should contain the sequence of actions to execute to reach from init_state to goal_state
    action_list = []

    # total_nodes_expanded maintains the total number of nodes expanded during the search
    total_nodes_expanded = 0
    time_limit = time.time() + time_limit
    
    '''
    YOUR CODE HERE

    Remove "raise NotImplementedError() and add your code.

    Your code for graph search should populate action_list and set total_nodes_expanded
    The automated script will verify their values

    In addition to this you must also write code for:
    1. compute_g
    2. compute_h
    '''
    
    explored = []
    flag = 0
    a_list = {}
    a_list[init_node] = []
    
    if algorithm == "bfs":
    	
    	if init_node.get_state() == goal_state:
    		return action_list, total_nodes_expanded
    		
    	while True:
    		if flag == 1:
    			break
    		
    		if priority_queue.is_empty():
    			#return action_list, total_nodes_expanded
    			break
    	
    		node = priority_queue.pop()
    		
    		curr_action = a_list.pop(node)
    		
    		explored.append(node.get_state())
    		total_nodes_expanded += 1
    		    		
    		children_nodes = list(helper.get_successor(node.get_state()).items())
    	
    		for a in children_nodes:
    			curr_state = a[1][0]
    			curr_node = Node(curr_state, node, 0, a[0], a[1][1])
    			
    			curr_action.append(a[0])
    			
    			f_score = compute_g(algorithm, curr_node, goal_state) \
        			+ compute_h(algorithm, curr_node, goal_state)
        			
    			if (curr_state not in explored):  #and (not priority_queue.contains(curr_state))):
    				if curr_state == goal_state:
    					flag ==1
    					action_list = curr_action
    					dummy = curr_action.pop()
    					#return action_list, total_nodes_expanded
    					break
    				
    				priority_queue.push(f_score, curr_node)
    				
    				a_list[curr_node] = curr_action
    				dummy = curr_action.pop() 


    else:

	    while True:	    		
	    	if priority_queue.is_empty():
	    		return action_list, total_nodes_expanded
	    	
	    	node = priority_queue.pop()
	    	
	    	curr_action = a_list.pop(node)
	    	
	    	if node.get_state() == goal_state:
	    		return curr_action, total_nodes_expanded
	    		
	    	explored.append(node.get_state())
	    	total_nodes_expanded += 1
	
	    	children_nodes = list(helper.get_successor(node.get_state()).items())
	    	
	    	for a in children_nodes:
	    		curr_state = a[1][0]
	    		curr_node = Node(curr_state, node, total_nodes_expanded, a[0], a[1][1])
	    		
	    		
	    		f_score = compute_g(algorithm, curr_node, goal_state) \
	        		+ compute_h(algorithm, curr_node, goal_state)
	        			
	    		if (curr_state not in explored):# and (not priority_queue.contains(curr_state))):
	    			priority_queue.push(f_score, curr_node)
	    			
	    			curr_action.append(a[0])
	    			a_list[curr_node] = curr_action 
	    			dummy = curr_action.pop()  
    

    if time.time() >= time_limit:
    
        raise SearchTimeOutError("Search timed out after %u secs." % (time_limit))

    return action_list, total_nodes_expanded
