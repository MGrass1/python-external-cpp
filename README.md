# python-external-cpp
A test using code written in cpp as python libraries for benchmarking efficiency differences

A small test for the speed differences of large calculations between functions built natively in Python vs imported compiled cpp code as libraries.

Results on finding primes show that the cpp imported library is 2-3 times faster for computing primes than python native functions.
Using python 3.6.6.


Almost no requirements necessary, if recompiling is necessary see instructions for how to do it and rename the path to the compiled 
library in the imports section of benchmark.py
