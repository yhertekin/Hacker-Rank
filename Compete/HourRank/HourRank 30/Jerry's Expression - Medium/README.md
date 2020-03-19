# Jerry's Expression #
This problem revolves around the Polish notation.

Polish notation is the way to write parenthesis-free expressions. Its distinguishing feature is that it places operators to the left of their operands.

    expression ::= number | (operator expression expression)
    operator ::=  + | - | x | / | …
    For example: "(A + B) x (C - D)" is "x+AB-CD".

You are given a Polish notation expression. Operators can be only + and -. Each number in expression is replaced with ?. You have to replace each ? with positive integer number, so that value of expression was 0. Also, you have to make the biggest number in expression as small as possible.

#### Input Format ####

The only line contains string with expression (string will contain only '?', '+' and '-').

#### Constraints ####

    3 <= string length <= 10^6.
#### Output Format ####

    Return an integer array, kth number should be the number for kth '?' in the string. If there are many solutions print any.

#### Sample Input 0 ####

    -?-??

#### Sample Output 0 ####

    1
    2
    1
#### Explanation 0 ####

    - 1 - 2 1   is   1-(2-1) = 0
