class Admission:

    def __init__(self, applicants, accepted):
        self.applicants = []
        self.total_applicants = applicants
        self.total_accepted = accepted

    def submit_applicants(self):
        for _ in range(self.total_applicants):
            first_name, last_name, gpa = input().split()
            self.applicants.append([first_name, last_name, float(gpa)])

    def accepted_applicants(self):
        print("Successful applicants:")
        sorted_applicants = sorted(self.applicants, key=lambda x: (-x[2], x[0], x[1]))
        for applicant in sorted_applicants[:self.total_accepted]:
            first_name, last_name = applicant[0], applicant[1]
            print(first_name, last_name)


admission = Admission(int(input()), int(input()))
admission.submit_applicants()
admission.accepted_applicants()
