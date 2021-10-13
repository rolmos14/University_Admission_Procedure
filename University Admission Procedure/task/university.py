class Admission:

    def __init__(self):
        self.scores = []

    def submit_scores(self):
        self.scores = [int(input()) for _ in range(3)]

    def mean_score(self):
        return sum(self.scores) / len(self.scores)

    def accepted(self):
        return self.mean_score() >= 60.0

    def print_result(self):
        print(self.mean_score())
        if self.accepted():
            print("Congratulations, you are accepted!")
        else:
            print("We regret to inform you that we will not be able to offer you admission.")


candidate = Admission()
candidate.submit_scores()
candidate.print_result()
