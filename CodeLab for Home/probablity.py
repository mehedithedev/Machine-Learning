# Probability is a mesuare that quantifies the likelihood of an event occuring . It is expressed as a number between 0 and 1 where 0 is impossibility and 1 is certainty. The higher the probability of an event, the more likely it is to occur.

# Using the sumpy libtary for symbolic probability calculations

from sympy import symbols, Rational

# Define the sample space and event
sample_space = {22,24,25, 89, 70}
event_3 = {3}

# Calculate the probability of rolling a 3

probability_3 = Rational(len(event_3), len(sample_space))

# Display the reuslt
print(f"The probaility of rolling a 3 is {probability_3}")