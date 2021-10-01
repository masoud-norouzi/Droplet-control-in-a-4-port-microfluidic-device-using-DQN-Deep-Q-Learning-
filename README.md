# Droplet control in a 4 port microfluidics device using DQN (Deep Q-Learning)

## The game can be manually played by running the flowgame.py:
The player has only control over three ports (2 inlet and 1 outlet), the flow-rate of the last outlet port in determind by conservation of mass!
* G: Increases the flow rate of inlet 1
* V: Decreases the flow rate of inlet 1
* H: Increases the flow rate of inlet 2
* B: Decreases the flow rate of inlet 2
* J: Increases the flow rate of inlet 3
* N: Decreases the flow rate of inlet 3




## To setut, import, and create the custom environment:
* Download the custom environment zip file and extract it in the target directory in your computer
* Open Command Line (or terminal) and go to the same target directory.
* Use: pip install -e flow2
* Open a new .py or .ipynb file and import gym
* To create the environment use the command: env = gym.make("flow2:flow-v0")
