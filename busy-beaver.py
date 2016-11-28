#!/usr/bin/python

import sys
from itertools import *
from turing_machine import TuringMachine

directions = "LR"
readable = "01"
writable = "1"
blank = " "

# generate ordered list of possible transitions for n-state turing machine
def generate_transitions(states):
  possible_transition_inputs = list(product(states, readable))
  possible_transition_outputs = list(product(states, writable, directions))
  possible_transition_funcs = [
    zip(possible_transition_inputs, item) for item in product(
      possible_transition_outputs, 
      repeat=len(list(possible_transition_inputs))
    )
  ]
  return possible_transition_funcs

# for a given turing machine, return the number of ones in its final tape
def get_ones(tm, max_steps):
  i = 0
  while not tm.final():
    if i > max_steps:
      break
    else:
      i += 1
    tm.step()
  tape = tm.get_tape()
  return tape.count('1')

def busy_beaver(n, max_steps):
  states = list(map(str, xrange(n)))
  possible_transition_funcs = generate_transitions(states)
  max_ones = -1

  for t in possible_transition_funcs:
    print(str(dict(t)))
    tm = TuringMachine("0" * max_steps, 
      initial_state = '0', 
      final_states = {states[n - 1]},
      transition_function=dict(t)
    )
    ones = get_ones(tm, max_steps)
    if ones > max_ones:
      max_ones = ones
  return max_ones

# Parse commandline input and pass to busy beaver method
def main():
  n = int(sys.argv[1])
  max_steps = int(sys.argv[2])

  print 'Received arguments', str(n), str(max_steps)

  if n < 1 or max_steps < 1:
    print 'Error: n and max_steps must both be positive'
  else:
    max_ones = busy_beaver(n, max_steps)
    print 'Busy beaver complete, got max value of', str(max_ones)

# Executable section of code
main()