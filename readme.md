# Poisson distribution added

Now the model changed. We

# Replication of Frank(1998)

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
* Stop working on graphs.
* Get into time based models!
* Get into agent-based simulation!
* Build a standardised model!
