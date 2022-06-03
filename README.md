# wordle-drl-final-project

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

The data is the list of 12972 5-letter words from the Wordle dictionary. Pytorch modules, Colab IDE.
