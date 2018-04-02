konwey is a game-of-life-esque simulation I devised one evening. It is named konwey because I wasn't clever enough to find an actually useful name.

The basic unit of life in konwey is what I call a kon. A kon is an array of numbers. The numbers correspond to an index in the commands array. The commands array is an array of strings, where each string is a command that assigns to a variable x. It may or may not modify x, but it's more interesting that it does.

In Conway's game of life, the way each unit lives (or not) is decided by the status of surrounding cells. In konwey, they way each kon lives is inspired by the way DNA works, although DNA seems to be able to do more with less. Basically, in each kon's life, there is a variable 'x' that each one has. Each kon then goes through each number in its array and runs the string in the command array that corresponds to that number. After running all commands, 'x' has hopefully changed value.

At this point, the kon has lived its life. Next, the kon's array is mutated - meaning, either it has a new number added, a number edited, a number deleted, or maybe nothing happens. Then, the resulting value of 'x' from when it was run is how many times this new, mutated kon is run - each one being a new thread, to speed it up. This process can potentially run on forever, but I currently let it live a fixed number of generations. Another way it could potentially be run is running it until you hit a certain value of x, or running it until a kon with an array of a certain length is achieved.

In this way, the kons that tend to prosper are those which create a higher value of 'x'.

Since this is a work in progress, there are still some aspects that I want to work on, and so what I want to work on next is an alternative way to get rid of kons. Currently, the only way a kon doesn't survive to the next generation is if it produces an 'x' value of 0. I want to consider whether I should implement another way of killing kons, or if I should expand the commands array. Another thing I want to pursue is to find a very good way to display kons. Is just printing the array sufficient? Should I print length + final value?
