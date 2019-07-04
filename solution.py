class Solution():
    def __init__(self, sequence, students):
        self.sequence = sequence
        self.length = len(sequence)
        self.counts = dict()
        for s in students:
            self.counts[s] = 0
        for seq in sequence:
            for elem in seq:
                self.counts[elem] += 1
        self.min_count = min(self.counts.values())
        self.students = students

    def pretty_print(self, verbose = False):
        print("Number of students: {}".format(len(self.students)))
        print("Number of valid groups in solution: {}".format(self.length))
        print("Minimum number of groups an individual can participate in: {}".format(self.min_count))
        print("-----------------------------------------------------------------")
        if verbose:
            print(self.sequence)
            for n in self.counts:
                print("Student {} participates in {} groups".format(n, self.counts[n]))
            print("-----------------------------------------------------------------")

