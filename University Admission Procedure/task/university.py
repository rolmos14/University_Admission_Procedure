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

    def accepted_applicants(self):
        # Sort applicants with high GPA first. If GPA is the same, sort by full name
        sorted_applicants = sorted(self.applicants, key=lambda x: (-x[2], x[0], x[1]))
        departments = sorted(['Mathematics', 'Physics', 'Biotech', 'Chemistry', 'Engineering'])
        departments_lists = [[] for _ in departments]  # initialize departments lists
        # Loop through sorted_applicants to assign each applicant to its first option, second if first is full and so on
        for applicant in sorted_applicants:
            for department in applicant[3:6]:
                if len(departments_lists[departments.index(department)]) < self.max_accepted:
                    # Store 'first_name' + 'last_name' + GPA for each applicant
                    departments_lists[departments.index(department)].append(applicant[:3])
                    break
        # Print departments and their accepted students
        for idx, department in enumerate(departments):
            print('\n' + department)
            for student in departments_lists[idx]:
                # 'first_name' + 'last_name' + GPA
                print(student[0], student[1], student[2])


admission = Admission(int(input()))
admission.submit_applicants("applicant_list.txt")
admission.accepted_applicants()
