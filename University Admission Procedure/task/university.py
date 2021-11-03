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
        #   [physics_score, chemistry_score, math_score, computer_science_score, special_score],
        #   ['1st_dept', '2nd_dept', '3rd_dept']],
        #   ['full_name', [physics_score, chemistry_score, ... ]]
        for applicant in file_lines:
            first_name, last_name, phy_sc, chem_sc, math_sc, comp_sc, spec_sc, dep_1, dep_2, dep_3 = applicant.split()
            self.applicants.append([first_name + " " + last_name,
                                    [float(phy_sc), float(chem_sc), float(math_sc), float(comp_sc), float(spec_sc)],
                                    [dep_1, dep_2, dep_3]])

    def accepted_applicants(self):

        def mean(numbers):
            return sum(numbers) / len(numbers)

        # Loop through all the priorities
        for priority_n in range(3):
            # Loop through all the departments
            for n, dep in enumerate(self.departments):
                dep_list = self.departments_lists[n]
                if len(dep_list) == self.max_accepted:
                    continue  # department full
                # Get all the applicants' full_name + scores / mean score + special score
                # whose priority_n equals the current department
                dep_applicants = [[applicant[0]] +
                                  [mean([applicant[1][dep_exam] for dep_exam in self.departments_exams[dep]])] +
                                  [applicant[1][-1]]
                                  for applicant in self.applicants if applicant[-1][priority_n] == dep]
                # Get best score for each applicant between mean score and special exam score
                dep_applicants = [[applicant[0]] + [max(applicant[1:3])] for applicant in dep_applicants]
                print(dep_applicants)
                # Sort them by corresponding exams mean / special exam & full_name and get as many as possible
                still_available = self.max_accepted - len(dep_list)
                dep_applicants = sorted(dep_applicants, key=lambda x: (-x[1], x[0]))[:still_available]
                # Assign applicants to the department list
                self.departments_lists[n].extend(dep_applicants)
                # Remove accepted applicants from main list
                accepted = [applicant[0] for applicant in dep_applicants]
                self.applicants = [applicant for applicant in self.applicants if applicant[0] not in accepted]

        # Write accepted students to files, one per department
        for n, dep in enumerate(self.departments):
            # Sort them again first to sort by mean score / special score & full_name
            self.departments_lists[n] = sorted(self.departments_lists[n], key=lambda x: (-x[1], x[0]))
            with open(dep.lower() + ".txt", "w") as file:
                for student in self.departments_lists[n]:
                    # 'full_name' + department's exam / mean score
                    file.write(student[0] + " " + str(student[1]) + "\n")


dep_exams = {'Mathematics': [2],
             'Physics': [0, 2],
             'Biotech': [0, 1],
             'Chemistry': [1],
             'Engineering': [2, 3]}
admission = Admission(int(input()), dep_exams)
admission.submit_applicants("applicants.txt")
admission.accepted_applicants()
