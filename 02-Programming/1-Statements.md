# Programming statements

There are three fundamental types of code execution:

1. Sequential processing
2. Conditional processing
3. Repetition

## Sequential
![Rover](./img/rover.jpg)
Let's say you need to send a mars rover. These are the steps:
1. Load the rover onto the rocket
2. Launch the rocket
3. When approaching to Mars, detach the rover
4. Land the rover by opening the parachutes
5. Send a success signal to base on Earth

Each instruction is executed one after another. Each step has to follow after another one.

## Conditional
Let's assume that the rover is already landed on Mars. However, it gets struct in Mars debris. So it has the following algorithm in its system:
1. If get stuck
2. Try to get out by steering back
3. If steering does not work, try to move to the left and to the right
4. If none of these ways work, send a SOS signal to Earth

Depending on the situation and its result, we execute different instructions. We still use sequential statements within those parts, however we execute only a part of them depending on our inputs.

## Repetition
Coming back to our rover, once it finds the rock with water, it has an algorithm to do the following
1. If the rock with water is found, then record current position
2. Then move 1 meter forward, backwards, left and right
3. If the water is found, continue moving
4. If no water is found, stop looking for it

So in this case, we execute an algorithm of finding water around it, once we find it somewhere. The idea of repetition is we repeat a certain number of actions until something is true, in this case until the water is found.

## Conclusion
All the computer algorithms and programs use these three types of statements. These are fundamental parts of writing any application.

> Homework: Write a step-by step algorithm that includes: 3 sequential, 2 repetitions and 1 conditional statements.