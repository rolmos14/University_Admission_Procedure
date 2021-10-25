class Admission:

    def __init__(self, max_accepted, departments_exams):
        self.applicants = []
        self.max_accepted = max_accepted
        self.departments = sorted(departments_exams.keys())
        self.departments_lists = [[] for _ in self.departments]
        self.departments_exams = departments_exams

    def submit_applicants(self, file_name):
        # Read the file with one applicant per line
        with open(file_name) as file:
            file_lines = file.read().splitlines()  # list with lines without '\n'
        # Store applicants as nested lists with 3 elements per applicant:
        # [['full_name',
        #   [physics_score, chemistry_score, math_score, computer_science_score],
        #   ['1st_dept', '2nd_dept', '3rd_dept']],
        #   ['full_name', [physics_score, chemistry_score, ... ]]
        for applicant in file_lines:
            first_name, last_name, phy_sc, chem_sc, math_sc, comp_sc, dep_1, dep_2, dep_3 = applicant.split()
            self.applicants.append([first_name + " " + last_name,
                                    [float(phy_sc), float(chem_sc), float(math_sc), float(comp_sc)],
                                    [dep_1, dep_2, dep_3]])

    def accepted_applicants(self):
        # Loop through all the priorities
        for priority_n in range(3):
            # Loop through all the departments
            for n, dep in enumerate(self.departments):
                dep_list = self.departments_lists[n]
                if len(dep_list) == self.max_accepted:
                    continue  # department full
                # Get all the applicants' full_name + scores whose priority_n equals the current department
                dep_applicants = [applicant[:2]
                                  for applicant in self.applicants if applicant[-1][priority_n] == dep]
                still_available = self.max_accepted - len(dep_list)
                # Sort them by corresponding exam score & full_name and get as many as possible
                dep_exam_pos = self.departments_exams[dep]
                dep_applicants = sorted(dep_applicants, key=lambda x: (-x[1][dep_exam_pos], x[0]))[:still_available]
                # Assign applicants to the department list
                self.departments_lists[n].extend(dep_applicants)
                # Remove accepted applicants from main list
                accepted = [applicant[0] for applicant in dep_applicants]
                self.applicants = [applicant for applicant in self.applicants if applicant[0] not in accepted]

        # Print departments and their accepted students, sorting them again first to sort by exam score & full_name
        for n, dep in enumerate(self.departments):
            print('\n' + dep)
            dep_exam_pos = self.departments_exams[dep]
            self.departments_lists[n] = sorted(self.departments_lists[n], key=lambda x: (-x[1][dep_exam_pos], x[0]))
            for student in self.departments_lists[n]:
                # 'full_name' + department's exam score
                print(student[0], student[1][dep_exam_pos])


dep_exams = {'Mathematics': 2,
             'Physics': 0,
             'Biotech': 1,
             'Chemistry': 1,
             'Engineering': 3}
admission = Admission(int(input()), dep_exams)
admission.submit_applicants("applicants.txt")
admission.accepted_applicants()
