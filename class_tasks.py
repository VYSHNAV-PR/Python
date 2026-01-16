class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def average(self):
         return sum(self.mark.values())/len(self.mark)
    def display_grade(self):
        avg=self.average()
        if avg>=80:
             return "A grade"
        elif avg>=70:
             return "B grade"
        elif avg>=60:
             return "C grade"
        elif avg>=50:
             return "D grade"
        else:
            return "Failed!!"
       
student1=Student("Vyshnav",{"Maths":80,"English":90,"Science":65,"IT":79})
print(
    f"Name: {student1.name}\n"
    f"Marks: {student1.mark}\n"
    f"Average: {student1.average():.2f}\n"
    f"Grade: {student1.display_grade()}"
)