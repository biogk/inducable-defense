# 0.4 Probably the last vwersion
The code used to generate the images is poisson2.py and perfectdefence.py.

Mathematical corrections was made.

See commits.

# 0.3.1 The last model was wrong
Even though you do not induce a defence, you pay a cost since you grow as your self.

# 0.3 A Improved model with poisson distribution

The previous poisson model is not biologically sensitive. Thus I created a model from scratch, but referring Frank(1998).

The model calculates the fitness of individual with behaviour, y, in population with average behaviour, z.

# 0.2 Poisson distribution added

Now the model has been changed. I simulate the prey as a random event that follows poisson distribution.

The model can be understood as several processes.
- 'First impact' kills who have not developed the defence.
- Wear down the defence of who have it.
- Who then survive pays the cost.

Now replacing the a value to the probability of attack at lease once in poisson distribution and add another selection to those who survived, it seems that the optimal probability of inducing a defence only depends on the distribution of attack. This is a obvious result, since everything except the probabilities are constants, while the uniform selection seems adding nothing useful.



# 0.1 Replication of Frank(1998)

This file describes the function file refrankfig1.py

In this programme, the following libraries are required
* numpy
  To generate a matrix

* matplotlib
  To make a plot

* multiprocessing
  To enhance processing productivity
  (Useless)

The function of this programme is to solve a equation and plot all the solutions in given range. In this case specifically the function provided by Frank(1997).

## Initiation

First, the precision of solving the equation is defined. This depends on the expected size of output image. The precision value is the size of the output matrix.

Then, a standard matrix is created in order to give x and y values to each point. It can be transposed to represent the other axis.

The final matrix to be used for plotting is also created at this stage.

## Functions

Two functions are defined in this piece of code.

### solve

The solve function receives a(the probability of attack) as input and uses the pre-generated x and y gradients to create a new matrix. The new matrix collects the values on the right in Frank's equation which equals 0 when a solution reaches. The new matrix shows the equality of the equation by showing how small the right side is.

### mapZeros

This function receives a matrix as input.
When the input value at a specific position is small enough, it let the corresponding position in line matrix to be 1.

## Calling Functions and Get Result
The solve function is called multiple times to make the solution for different values.

## Limitations
* Inefficient using scatter plot to draw curves.
* Require two huge matrix to solve equaton.(fine)

## Future plan
* ~~Stop working on graphs.~~
* Kin selection in virulence
* Partial dispersal offspring
* Build a standardised model!(unlikely)
