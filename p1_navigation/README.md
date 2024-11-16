

# Project Description


In this project, the Deep Reinforcement Learning agent learns to navigate and collect yellow bananas and avoid blue ones using Deep Q-Networks (dqn)

A reward of +1 is given after collecting a yellow banana, and a reward of -1 for blue banana.

The state vector is of 37 length and has the agent's velocity, along with ray-based perception of objects around agent's front direction. It also has four discrete actions available:
1. 0 - move forward.
2. 1 - move backward.
3. 2 - turn left.
4. 3 - turn right.

The agent must get in a 100 consecutive episodes an average score of +13 over.

### Getting Started

1. Please follow the instructions here for installing dependences [click here](https://github.com/udacity/Value-based-methods?tab=readme-ov-file#dependencies)

2. Download the environment from one of the links below:
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
    
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    

3. Place the file in the `p1_navigation/` folder, and unzip it. 


### Instructions on how to run the code for training or for watching trained agent
Inside the Navigation file in `p1_navigation/` folder:

For training the agent:
Please run the cells from the start till the end of part 3 Training agent section

For watching trained agent:
Please restart the kernel and rerun the cells from the start till till the end except for part 3 Training agent section (I mean don't rerun that section or you would would train the agent again)

