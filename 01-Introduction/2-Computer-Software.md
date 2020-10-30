# Computer software

Software is intructions for hardware.

A number of instructions is called a program. Software is ***vital*** to the computer, without it, it is useless.

## Computer language

Computer works using binary system, meaning it only has the knowledge of 0's and 1's. All the data, all the programs, every image, video and sound is stores using two values: either 0 or 1. 

A single digit (0 or 1) is called a bit and is the smallest unit of information. A byte consists of 8 bits.

Each string or character is represented using a number of bits. Two most used encodings are: ASCII (1 byte per character) and Unicode (2 bytes per character, used for emojis 💻, foreign language symbols etc.).

### Binary Number System
The system that we use in every day life is called ***Decimal***. It has 10 digits from 0 to 9. When we want to represent numbers bigger than 9, we add 1 and reset 9 to start from zero:

0..7,8,9,***10***,***11*** etc.

The same principle applies for binary numbers.
We start with 0 and 1, when we want to represent the next number, we add 1 and reset the first one, so:

0,1,***10***,***11***,***100*** etc.

> Please note, that this is not 10 or 11, this is read as one-zero and one-one, to not confuse with decimal system.

### Programming language types
Computers can not use human languages, and  programming in the binary language of computers is a very difficult, tedious process.

Therefore, most programs are written using a programming language and are converted to the binary language used by the computer.

Three major categories of prog languages:
 - Machine Language 
 - Assembly Language
 - High level Language

#### Machine language
1. Natural language of a particular computer
2. The instructions are in the form of binary code
3. Any other types of languages must be translated down to this level.

#### Assembly Languages
1. English-like Abbreviations used for operations (Load R1, R8)
2. Assembly languages were developed to make programming easier
3. The computer cannot understand assembly language - a program called assembler is used to convert assembly language programs into machine code

#### High Level Languages
1. English-like and easy to learn and program
2. Common mathematical notation
Total Cost = Price + Tax;
area = 5 * 5 * 3.1415;
3. Java, C, C++, Python, JavaScript


### High-Level language to Machine Language
Since the computer only works with Machine Language (0's and 1's), when writing our programs in High-Level language, we need to be able to convert to low-level Machine Language. This process is called ***compilation of source code***.

The program that converts our source code to machine language is called a ***compiler***. 

Since the process of compilation happens on a specific machine with specific set of instructions available to that machine (cpu, ram), programs often have to be compiled for multiple architectures (different cpu types, disk types etc.). Nowadays, this is not such a common practice, since we have high-level languages like Java, JavaScript and Python that run on any platform regardless of operating system and architecture.

### What is Programming?
- Programming – the creation of an ordered set of instructions to solve a problem with a computer.

- Only about 100 instructions that the computer understands - Different programs will just use these instructions in different orders and combinations and build on top of each other.

- The most valuable part of learning to program is learning how to think about arranging the sequence of instructions to solve the problem or carry out the task
