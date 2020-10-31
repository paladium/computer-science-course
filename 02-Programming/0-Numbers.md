# Computer number bases
Remember number sustem consists of two digits: 0 and 1.
There are other number systems, such as decimal (base-10), hexadecimal(base-16).

Binary = 0 and 1
Decimal = 0 to 9
Hexadecimal = 0 to 9, A, B, C, D, E, F

## Decimal to binary

It is easy to convert between different bases. Let's start with converting decimal number to a binary one.

The algorithm for converting a decimal number to a binary one is the following:
1. Divide the decimal number by 2
2. Take the remainder as the left-most digit of the number
3. Divide the quotient of the previous divide by 2
4. Take the remainder as the left-most digit of the number
5. Repeat until the result becomes zero

The last remainder will be the most significant digit (right-most).

For example, let's convert number 33 to binary.

1. Divide 33 by 2, remainder = 1, result = 16
2. Divide 16 by 2, remainder = 0, result = 8
3. Divide 8 by 2, remainder = 0, result = 4
4. Divide 4 by 2, remainder = 0, result = 2
5. Divide 2 by 2, remainder = 0, result = 1
6. Divide 1 by 2, remainder = 1, result = 0

Now, take the remainders from the end and combine them into: 100001. So 33(base10)=100001(base2).

## Binary to decimal

The algorithm for converting binary number to a decimal one is the following:
1. Determine the position of each digit
2. Multiple the value by the power of 2 to the position of that digit (starting from the left).
3. Add all values together

Let's take the number 100111.
1. Positions: (1 * 2^5) + (0 * 2^4) + (0 * 2^3) + (1 * 2^2) + (1 * 2^1) + (1 * 2^0)
2. (32 + 0 + 0 + 4 + 2 + 1)
3. 39

## Decimal to hexadecimal

Same steps as before for the binary, but instead divide by the 16(base-16).
Take the number 145.
1. Divide 145 by 16, remainder = 1, result = 9
2. Divide 9 by 16, remainder = 9, result = 0 

So then we combine the number from the end, it becomes 91. So 145(base-10) is 91(base-16).

## Hexadecimal to decimal

Same steps as for binary, by take 16 to the power of position. Let's say we have a hexadecimal number 4F. Let's convert it to decimal:
1. Positions: (4 * 16^1) + (F * 16 ^ 0)
2. As we remember F equals to 15, so (4 * 16) + (15)
3. The result = 79

So 4F in hexadecimal is 79 in decimal.

## Hexadecimal to binary

1. Convert each hexadecimal digit to a 4-digit binary number.
2. Combine the result into a single binary number.

The table:
0 - 0000
1 - 0001
2 - 0010
3 - 0011
4 - 0100
5 - 0101
6 - 0110
7 - 0111
8 - 1000
9 - 1001
A - 1010
B - 1011
C - 1100
D - 1101
E - 1110
F - 1111

For example the number 3A:
1. 3 = 0011, A = 1010
2. The result is 00111010

By removing leading zeros, we get, 3A in hexadecimal is 111010 in binary.

## Binary to hexadecimal

Divide the binary number into groups of 4. Add leading zeros to make it divisible by 4. Convert each group into a hexadecimal number. Combine the result.

For example, we have a number: 110101.

1. 0011 0101
2. 0011 = 3 and 0101 = 5
3. The result is 35 in hexadecimal.

So the number 110101 in binary is 35 in hexadecimal.

> Homework
Convert the following numbers to another base, also show your workings:
1. 10100111(binary) to decimal
2. 44F (hex) to binary
3. 456 (decimal) to hexadecimal
4. 10001100(binary) to hex
5. 223(decimal) to binary
6. AA12 (hex) to decimal