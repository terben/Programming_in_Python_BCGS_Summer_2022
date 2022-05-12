#!/usr/bin/env python3

# Example module  with docstrings. This should  mainly demonstrate how
# docstrings are integrated in the Python-documentation environment.

"""
Module to simulate a reversed Polish Notation Calculator
"""

import sys
import numpy as np


def __apply_onearg(rpn_stack, rpn_element):
    """
    application of functions that take one arguments to an
    rpn_stack. If possible, the last element is used for function
    application and the result is put on the stack.  The original
    element is removed.  Retruns an empty stack on failure.
    """

    if len(rpn_stack) > 0:
        first = rpn_stack.pop()
        if rpn_element == 'sqr':
            return rpn_stack.append(first * first)
        if rpn_element == 'sqrt':
            return rpn_stack.append(np.sqrt(first))
        if rpn_element == 'sin':
            return rpn_stack.append(np.sin(first))
        if rpn_element == 'cos':
            return rpn_stack.append(np.cos(first))
    else:
        return []


def __apply_twoargs(rpn_stack, rpn_element):
    """
    application of functions that take two arguments to an
    rpn_stack. If possible, the last two numeric elements are used for
    function application and the result is put on the stack.  The
    original two elements are removed.  Retruns an empty stack on
    failure.
    """

    if len(rpn_stack) > 1:
        first = rpn_stack.pop()
        second = rpn_stack.pop()
        if rpn_element == '+':
            return rpn_stack.append(second + first)
        if rpn_element == '-':
            return rpn_stack.append(second - first)
        if rpn_element == '*':
            return rpn_stack.append(second * first)
        if rpn_element == '/':
            return rpn_stack.append(second / first)
    else:
        return []


def evaluate_rpn(rpn_string):
    """
    Routine to evaluate a string containing an RPN expression.
    On success the function returns a float with the result.
    On failure, 'None' is returned.

    Example:
    >>> x = evaluate_rpn('1 2 + 3 *')
    >>> print(x)
    """

    rpn_expression = rpn_string.split()
    rpn_stack = []

    for rpn_element in rpn_expression:
        done_op = 0

        # first try to append a number to the RPN stack.
        # If this fails the current RPN element must be
        # an operation:
        try:
            rpn_stack.append(float(rpn_element))
            done_op = 1
        except:
            if rpn_element in ['+', '-', '*', '/']:
                __apply_twoargs(rpn_stack, rpn_element)
                done_op = 1

            if rpn_element in ['sqr', 'sqrt', 'sin', 'cos']:
                __apply_onearg(rpn_stack, rpn_element)
                done_op = 1

            # If no operation was performed something is wrong.
            # The same if the stack is now empty:
            if (done_op == 0) or (len(rpn_stack) < 1):
                print("Error in RPN expression", file=sys.stderr)
                sys.exit(1)

    if len(rpn_stack) == 1:
        return rpn_stack[0]
    else:
        return None

if __name__ == '__main__':
    # Many modules perform tests if they are called as a script
    # I do this here by enabling RPN expressions on the command
    # line.
    if len(sys.argv) != 2:
        print("Synopsis: %s rpn_expression; e.g. %s '1 2 +'" %
              (sys.argv[0], sys.argv[0]))
    else:
        rpn_string = sys.argv[1]

        result = evaluate_rpn(rpn_string)
        if result is not None:
            print("The result of the RPN expression '%s' is %f" %
                  (rpn_string, result))
        else:
            print("Something wrong with the RPN stack at the end"
                  " of calculations!!", file=sys.stderr)
            sys.exit(1)
