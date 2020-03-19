# network-traffic-models

### code segments for various network traffic models

#### two-state discrete Markov chain process

------------

- In this code(`two_state_markov_chain.py`), a series of 1's and 0's can be generated based on a transition probability matrix.
- Transition probability matrix can be defined as follows. 

    P(0,0)				P(0,1)<br>
    P(1,0)				P(1,1)

- Markov chain model related to this code is illustrated as follows.
<img src = "two_state_markov.png">

#### four-state discrete Markov chain process

------------

- In this code(`four_state_markov_chain.py`), a series of 0's~3's can be generated based on a transition probability matrix.
- Transition probability matrix can be defined as follows. 

    P(0,0)				P(0,1)				P(0,2)				P(0,3)<br>
	P(1,0)				P(1,1)				P(1,2)				P(1,3)<br>
	P(2,0)				P(2,1)				P(2,2)				P(2,3)<br>
	P(3,0)				P(3,1)				P(3,2)				P(3,3)

- Markov chain model related to this code is illustrated as follows.
<img src = "four_state_markov.png">

#### References

------------

- [Primary radio user activity models for cognitive radio networks: A survey](https://www.sciencedirect.com/science/article/pii/S1084804514000848 "Primary radio user activity models for cognitive radio networks: A survey")
