import statistics

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return statistics.mean(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)

class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if not self.students:
            return 0
        return statistics.mean([student.calculate_average() for student in self.students.values()])

    def display_student_performance(self):
        if not self.students:
            print("No students in the system.")
            return

        print("\nStudent Performance:")
        print("-" * 40)
        for name, student in self.students.items():
            avg = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"{name}: Average: {avg:.2f}, Status: {status}")
        
        class_avg = self.calculate_class_average()
        print(f"\nClass Average: {class_avg:.2f}")

    def view_stored_data(self):
        if not self.students:
            print("No students in the system.")
            return

        print("\nStored Student Data:")
        print("-" * 40)
        for name, student in self.students.items():
            print(f"Name: {name}")
            print(f"Scores: Math: {student.scores[0]}, Science: {student.scores[1]}, English: {student.scores[2]}")
            print("-" * 40)

def get_valid_score(subject):
    while True:
        try:
            score = int(input(f"Enter score for {subject}: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    tracker = PerformanceTracker()

    while True:
        print("\nOptions:")
        print("1. Add a student")
        print("2. View stored data")
        print("3. Display performance summary")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            name = input("Enter student name: ").strip()
            scores = []
            for subject in ['Math', 'Science', 'English']:
                score = get_valid_score(subject)
                scores.append(score)
            tracker.add_student(name, scores)
            print(f"Added {name} to the system.")
        elif choice == '2':
            tracker.view_stored_data()
        elif choice == '3':
            tracker.display_student_performance()
        elif choice == '4':
            print("Thank you for using the Student Performance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()