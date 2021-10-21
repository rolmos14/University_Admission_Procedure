class Admission:

    def __init__(self, max_accepted, departments):
        self.applicants = []
        self.max_accepted = max_accepted
        self.departments = sorted(departments)
        self.departments_lists = [[] for _ in departments]

    def submit_applicants(self, file_name):
        # Read the file with one applicant per line
        with open(file_name) as file:
            file_lines = file.read().splitlines()  # list with lines without '\n'
        # Store applicants as nested lists with 3 elements per applicant:
        # [['full_name', GPA, ['1st_dept', '2nd_dept', '3rd_dept']], ['full_name', GPA, ... ]]
        for applicant in file_lines:
            first_name, last_name, gpa, dep_1, dep_2, dep_3 = applicant.split()
            self.applicants.append([first_name + " " + last_name, float(gpa), [dep_1, dep_2, dep_3]])

    def accepted_applicants(self):
        # Loop through all the priorities
        for priority_n in range(3):
            # Loop through all the departments
            for n, dep in enumerate(self.departments):
                dep_list = self.departments_lists[n]
                if len(dep_list) == self.max_accepted:
                    continue  # department full
                # Get all the applicants' (full_name + GPA) whose priority_n equals the current department
                dep_applicants = [applicant[:2]
                                  for applicant in self.applicants if applicant[-1][priority_n] == dep]
                still_available = self.max_accepted - len(dep_list)
                # Sort them by GPA & full_name and get as many as possible
                dep_applicants = sorted(dep_applicants, key=lambda x: (-x[1], x[0]))[:still_available]
                # Assign applicants to the department list
                self.departments_lists[n].extend(dep_applicants)
                # Remove accepted applicants from main list
                self.applicants = [applicant for applicant in self.applicants if applicant[0] not in dep_applicants]

        # Print departments and their accepted students
        for n, dep in enumerate(self.departments):
            print('\n' + dep)
            for student in self.departments_lists[n]:
                # 'full_name' + GPA
                print(student[0], student[1])


admission = Admission(int(input()), ['Mathematics', 'Physics', 'Biotech', 'Chemistry', 'Engineering'])
admission.submit_applicants("applicant_list.txt")
admission.accepted_applicants()
