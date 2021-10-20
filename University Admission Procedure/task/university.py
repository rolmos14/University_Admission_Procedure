class Admission:

    def __init__(self, max_accepted):
        self.applicants = []
        self.max_accepted = max_accepted

    def submit_applicants(self, file_name):
        # Read the file with one applicant per line
        with open(file_name) as file:
            file_lines = file.read().splitlines()  # list with lines without '\n'
        # Store applicants as nested lists with 6 elements per applicant:
        # [['first_name', 'last_name', GPA, '1st_department', '2nd_department', '3rd_department'], ['first_name', ...]]
        for applicant in file_lines:
            first_name, last_name, gpa, dep_1, dep_2, dep_3 = applicant.split()
            self.applicants.append([first_name, last_name, float(gpa), dep_1, dep_2, dep_3])
        print(self.applicants)

    def accepted_applicants(self):
        print("Successful applicants:")
        sorted_applicants = sorted(self.applicants, key=lambda x: (-x[2], x[0], x[1]))
        for applicant in sorted_applicants[:self.total_accepted]:
            first_name, last_name = applicant[0], applicant[1]
            print(first_name, last_name)


admission = Admission(int(input()))
admission.submit_applicants("applicant_list.txt")
admission.accepted_applicants()
