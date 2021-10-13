class Admission:

    def __init__(self):
        self.scores = []

    def submit_scores(self):
        self.scores = [int(input()) for _ in range(3)]

    def mean_score(self):
        return sum(self.scores) / len(self.scores)

    def print_result(self):
        print(self.mean_score())
        print("Congratulations, you are accepted!")


candidate = Admission()
candidate.submit_scores()
candidate.print_result()
