# Conway's Game of Life
This is an implementation of Conway's Game of Life with python and tkinter. The game of life was first invented by
Cambridge mathematician John Horton Conway in the 1970s.
It is a two-dimensional cellular automaton. The environment is a grid with vertical and horizontal axes. The grid
usually extends to infinity, but I have implemented it in a bounded space.
The rules of the game are as follows:
* Each cell in the grid has two states: alive or dead. These are denoted by different colours.
* Each cell has eight neighbours, corresponding to the eight directions north, south, east, west, north-west,
north-east, south-west, south-east.
* Given an initial configuration of alive and dead cells, any alive cell will survive to the next generation only if
it has two or three alive neighbours.
* Any alive cell that has four or more than four alive neighbours will die in the next generation. Alternately, any
alive cell with less than two neighbours will also die.
* Any dead cell that has exactly three neighbours will come to life in the next generation.

This simple set of rules has yielded a fascinating model which has been fancied by various mathematicians for many
years. What initial configuration will converge to a stable state and which of them will grow without bounds is an
active area of study.
