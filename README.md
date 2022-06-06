# wordle-drl-final-project

Github link: https://github.com/srikg-msai22/wordle-drl-final-project

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

The tech stack includes Pytorch modules, Colab IDE, Weights and Biases (for logging).

## Methodology

Existing approaches to solve Wordle are mainly focused on information theory. Tgus project is focused on using Deep Reinforcement Learning to solve this problem. 

We tried the following methods:

1. **Deep Q learning:** 

  Q-learning is a values-based reinforcement learning algorithm which updates the value function based on the Bellman equation. Deep Q-Learning uses experience replay to learn the value function in small batches, so that the agent doesn't need to re-train after each step.

  In our case, we have used the learnt embeddings for the encoded words as the predicted Q-value of taking an action for a given state.


3. **Advantage Actor Critic (A2C):**

  “Actor-Critic” is a class of algorithms that satisfy the criteria that there exists parameterized actors and critics. The actor is the policy while the critic computes the value function to assist the actor in learning.

  In our case, we have trained the network to solve the problem sequentially increasing the complexity by increasing the vocabulary size.


## Implementation choices

The state vector is an integer vector of size 417, one for the number of remaining turns, and the rest to represent the state. The neural network takes this vector as input, feeds it through an MLP with some hidden layers to an output layer of size 130. Because the output word has a fixed size (5), the vocabulary is one-hot encoded to get a 130-wide one-hot representation for the word (26*5).

This is essentially constraining the value of each word, given an input state, to be the sum of its letters. For Deep Q learning, we use this as the predicted Q-value of taking this action in the given state. For policy gradients, we pass this through a softmax layer to get probabilities.



## Future work

In the future, we want to extend this work to be able to solve more complex versions of Wordle, namely:

1. Extending the code so that the agent can how to solve Wordle for 6-letter words. We will require a bigger dataset of 6-letter words and adding new constraints for the agent to learn from. We would also like to determine the best 6-letter word to start guessing with, as a result.

2. Extending the code so that the agent can learn to guess a variable-length word, mimicking the game Semantle. We would require a much larger dataset and many more constraints for the agent to guess the word correctly. 

3. We could also extend this code to solve Quordle, another game inspired by Wordle where the user has to guess 4 words at the same time in 8 tries. 





