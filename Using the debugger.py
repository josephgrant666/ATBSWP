print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')
second = input()
print('Enter the third number to add:')
third = input()
print('The sum is ' + first + second + third) 

# The debugger here has revealed that the problem with this program is that it is performing string concatenation rather than adding the integers
# The debgugger has 5 main functions:
# Go- Runs the program fully without pause
# Step- Executes entire arguments without pausing on each one of their function calls/ steps over an indentation
# Over- Executes each piece of code one by one, step by step
# Out- Jumps outside of an indentation by executing the rest of the code and jumping to the next argument offered
# Quit- Stops the program entirely

# Breakpoints can also be used to stop the debugger at certain parts of the code. This is done by right clicking on a line and selecting 'set breakpoint'.This is the line highlighted in yellow.
