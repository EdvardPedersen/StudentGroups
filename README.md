# StudentGroups

Approaches to solve the student group problem:

Which groups of 3 can you make of N students such that:
- No pair of students is ever grouped more than once
- Each student participates in the maximum number of groups

# Relationship to Steiner triples

For `N = 6k + 1` and `N = 6k + 3`, the optimal solutions are [Steiner triples](https://en.wikipedia.org/wiki/Steiner_system).

This means that for these values of N, a "perfect" solution exists.

# Implemented algorithms

## Lowest least used

Gives a solution which attempts to equalize group participation

- For each digit
-- Take the least used element - if multiple are least used, take the lowest of the least used
-- If this element is not legal to use in the current group, go to the next element
- Add the group
- Continue until no more legal groups can be created

## Brute force

Gives all optimal solutions

- Generate every combination
- For each starting group, try every other valid group
- For each subsequent group, try every other valid group

# Utilities

`create_pairs_for_meetings.py` reads a file `participants.txt`, containing 1 name per line, and generates pairs until everyone has paired up with everyone else, in such a way that the maximum number of people can meet per week.
