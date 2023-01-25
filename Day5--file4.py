class faculty1:
    def sub(self):
        print("Theory")
class faculty2:
    def sub(self):
        print("Lab")
class student(faculty1, faculty2):
    pass
stu=student()
print(stu.sub())
