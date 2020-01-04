import numpy as np

def retStream(curr_state, transition_prob, time_steps):
  """
  ***generate a stream of 1's and 0's based on the given transition probability matrix.
  """
  arr = []
  for step in range(time_steps):
    arr.append(curr_state)
    nxt_st = np.random.choice([0,1],p=list(transition_prob[curr_state,:]))
    curr_state = nxt_st
  return(arr)

def retNxtState(curr_state, transition_prob):
  """
  ***generate the next state based on the given transition matrix.
  """
  nxt_st = np.random.choice([0,1],p=list(transition_prob[curr_state,:]))
  return(nxt_st)

"""
Example 01(return a markov stream given the initial state)
"""
prob_mat = np.array([[0.1, 0.9], [0.18, 0.82]])
markov_stream = retStream(0, prob_mat, 100)
print(markov_stream)

"""
Example 02(return the next state given a current state)
"""
next_st = retNxtState(1, prob_mat)
print(next_st)
