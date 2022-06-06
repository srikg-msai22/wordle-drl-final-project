# wordle-drl-final-project
Github link: https://github.com/srikg-msai22/wordle-drl-final-project

> Clarissa Cheam, Devyani Gauri, Kavya J, Srik G



## Introduction

Wordle is a game now owned by New York Times which was created by Josh Wardle in 2013. The prototype was dusted off for the pandemic and since then has steadily gained popularity. The rules are simple; the user has 6 chances in a day to guess a 5 letter word and for every guess the game tells you whether each letter in the guess exists in the goal word.

Information provided for a guess:
* If a letter is in the goal word and in the right position, the letter turns green 
* If a letter is in the goal word and not in the right position, the letter turns yellow
* If the letter is not in the goal word it turns gray.

Our project is to solve this problem using reinforcement learning.

## Problem Statement

For this project, we want to train an agent using model-based approaches to solve Wordle using reinforcement learning in the least number of tries. As part of the task, we want to find the optimal first word. To evaluate our model, we will use the overall accuracy of the model and the average number of tries it takes to get to the goal word (given a certain number of games played by the agent).	

## Data and Tech Stack

The data is the list of 12972 5-letter words from the Wordle dictionary. 

The tech stack includes Pytorch modules, PyTorch Lightning module, Colab IDE, Weights and Biases (for logging).

## Methodology

Existing approaches to solve Wordle are mainly focused on information theory. This project is focused on using Deep Reinforcement Learning to solve this problem. 

We tried the following methods:

1. **Deep Q learning:** 

  Q-learning is a values-based reinforcement learning algorithm which updates the value function based on the Bellman equation. Deep Q-Learning uses experience replay to learn the value function in small batches, so that the agent doesn't need to re-train after each step.

  In our case, we have used the learnt embeddings for the encoded words as the predicted Q-value of taking an action for a given state.


2. **Advantage Actor Critic (A2C):**

  “Actor-Critic” is a class of algorithms that satisfy the criteria that there exists parameterized actors and critics. The actor is the policy while the critic computes the value function to assist the actor in learning.

  In our case, we have trained the network to solve the problem sequentially increasing the complexity by increasing the vocabulary size.


## Implementation choices

The state vector is an integer vector of size 417, one for the number of remaining turns, and the rest to represent the state. The neural network takes this vector as input, feeds it through an MLP with some hidden layers to an output layer of size 130. Because the output word has a fixed size (5), the vocabulary is one-hot encoded to get a 130-wide one-hot representation for the word (26x5).

This is essentially constraining the value of each word, given an input state, to be the sum of its letters. For Deep Q learning, we use this as the predicted Q-value of taking this action in the given state. For policy gradients, we pass this through a softmax layer to get probabilities.

We experimented with the following hyperparameters for the DQN algorithm:

1. max_epochs: We tried values in the range of 500 to 5000 and settled on 5000 as the final value for max_epochs to give the agent enough runs to learn from

2. replay_size: We tried values between 100 and 1000 and our final value was 1000

3. lr: We started with high values for the learning rate at 1e-3, and moved down until 1e-5, but 1e-3 gave the best results.

4. weight_decay: We tried multiple values between 1e-6 and 1e-2 and settled on 1e-5 as the best value for our task

5. batch_size: Batch size 512 worked the best for the model

For the A2C model, we used a learning rate of 1e-4, a batch_size of 64, replay_size of 1000. 

## Results

From the 2 models, A2C showed better results with an average win rate of 92.5% (accuracy).

<img width="834" alt="image" src="https://user-images.githubusercontent.com/91037549/172090405-1ab8b298-4f4c-45fb-b748-1c49adebe286.png">

Following are the graphs for our best performing run of A2C:



<img width="1344" alt="image" src="https://user-images.githubusercontent.com/91037549/172091452-5dd91eb3-cbce-40df-8758-56001d867bbb.png">
<img width="1341" alt="image" src="https://user-images.githubusercontent.com/91037549/172091477-f35c7c18-13ce-4f9d-b3a4-b7416f1340d4.png">

<img width="456" alt="image" src="https://user-images.githubusercontent.com/91037549/172091139-1614cc4f-287d-4915-bc90-8c9a5fd227c4.png">





## Future work

In the future, we want to extend this work to be able to solve more complex versions of Wordle, namely:

1. We want to explore using policy gradient methods. For this, we plan to make the Agent choose actions probabilistically, and based on the loss function nudge the Agent to make that specific action more or less probable

2. Extending the code so that the agent can how to solve Wordle for 6-letter words. We will require a bigger dataset of 6-letter words and adding new constraints for the agent to learn from. We would also like to determine the best 6-letter word to start guessing with, as a result.

3. Extending the code so that the agent can learn to guess a variable-length word, mimicking the game Semantle. We would require a much larger dataset and many more constraints for the agent to guess the word correctly. 

4. We could also extend this code to solve Quordle, another game inspired by Wordle where the user has to guess 4 words at the same time in 8 tries. 



Inspiration and reference from:

https://wandb.ai/andrewkho/wordle-solver/reports/Solving-Wordle-with-Reinforcement-Learning--VmlldzoxNTUzOTc4
https://andrewkho.github.io/wordle-solver/

