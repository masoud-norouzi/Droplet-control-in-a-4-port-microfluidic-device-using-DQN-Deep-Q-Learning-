# Droplet control in a 4 port microfluidics device using DQN (Deep Q-Learning Network)

## Project description:
The goal of this process is to show the possibility of the controlling a droplet in a given set-point in a 4 port microfluidic device. The device is a square device with 4 ports (two inlets and two outlets) on each corner with a diagonal arrangment. Based on the flow rates, there will be a stagnation point (were the flow rate is basically zero) in the middle of the device. The position of the stagnation point depends on the flow rates.
For simplicity, the droplet is assumed to behave similar to a point-particle, i. e., it simply follows the streamline of the fluid at each position.Knowing the flow rates, the velocity of the fluid at every point in the device can be calculated by solving (Analytically) the laplace equaion:

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial^2&space;\psi}{\partial&space;x^2}&space;&plus;&space;\frac{\partial^2&space;\psi}{\partial&space;y^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial^2&space;\psi}{\partial&space;x^2}&space;&plus;&space;\frac{\partial^2&space;\psi}{\partial&space;y^2}" title="\frac{\partial^2 \psi}{\partial x^2} + \frac{\partial^2 \psi}{\partial y^2}" /></a>

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
