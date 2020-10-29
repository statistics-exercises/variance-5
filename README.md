# Variance of mean

In the previous exercise you wrote code to calculate the variance of the sample mean:


In this exercise, we are going to investigate how this quantity varies as the number of variables that were used in the calculation of __the sample mean__ changes.  As in the previous exercise, you will need to complete the two functions:

1.  `sample_mean` - takes a single integer `m` in input.  It should return a sample mean that is computed by generating `m` uniform random variables that lie between 0 and 1.
2. `variance` - takes two integers in input `m` and `n`.  This function should return an estimate of the variance for a sample mean computed from `m` uniform random variables that lie between 0 and 1.  This variance should be calculated by generating `n` estimates of the sample mean.

You then need to write the internals of the loop that I have started to set the variables `xvals` and `yvals`:

1. The first element of `xvals` should be set equal to 1, the second element should be set to two and so on.
2. The first element of `yvals` should be set equal to an estimate of the variance for a sample mean computed from one random variable, the second element should be set equal to an estimate of the sample variance for a sample mean computed from two random variables, the third element should be set equal to an estimate of the sample variance for a sample mean computed from three random variables.  This process should be continued until you have an estimate of the sample variance for a sample mean computed from 200 random variables.

All your estimates for the sample variance should be computed from 10 random variables.  

When you have completed the exercise you should have a graph showing how the variance of the sample mean decreases as you compute the sample mean from more random variables.
