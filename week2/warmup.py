class Student:
    def __init__(self, name):
        self.name = name
        self.left_student = None
        self.right_student = None


class Classroom:
    def __init__(self, first:Student):
        if first is not isinstance(Student):
            raise ValueError()
        self.first = first

    def add_student_to_front(self, student):
        if type(student) is not Student:
            return

        student.right_student = self.first
        self.first = student

    def add_student_to_end(self, student:Student):
        if self.first is None:
            return
        else:
            placement = False
            current = self.first
            while placement == False:
                if current.right_student is None:
                    current.right_student = student
                    placement = True
                else:
                    current = current.right_student

    def find_student(self, student_name):
        current = self.first
        searching = True
        while searching:
            if current.name == student_name:
                searching = False
            else:
                current = current.right_student
        return current
