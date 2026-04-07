import pandas as pd
def student_performance_model(data_path):
    df = pd.read_csv(data_path)

    print("First 5 records:")
    print(df.head())

    print("Last 5 records:")
    print(df.tail())

    print("Total rows and columns:")
    print(df.shape)

    print("List of column names:")
    print(df.columns)

    print("Data type of each column:")
    for col in df.columns:
        print(f"Type of {col} is : ",type(col))

    print("Display total number of students in dataset.")
    total_students_count = df.shape[0]
    print(df.shape[0])
    print(len(df))

    print("Count how many students passed.")
    student_passed = lambda a : a == 1
    no_passed_students = len(list(filter(student_passed,df["FinalResult"])))
    print(no_passed_students)

    print("Count how many students failed.")
    student_failed = lambda a : a == 0
    no_failed_students = len(list(filter(student_failed,df["FinalResult"])))
    print(no_failed_students)

    print("Average Study hours:")
    print(df["StudyHours"].mean())

    print("Average attendance:")
    print(df["Attendance"].mean())

    print("Maximum Previous Score:")
    print(df["PreviousScore"].max())

    print("Minimum SleepHours:")
    print(df["SleepHours"].min())

    print("Class Distribution (Final Result count)")
    print(df["FinalResult"].value_counts())

    passed_student_percent = (no_passed_students / total_students_count) * 100
    failed_student_percent = (no_failed_students / total_students_count) * 100

    print("Passed student percent : ",passed_student_percent)
    print("Failed student percent : ",failed_student_percent)

    print("""
The data set is not perfectly balanced and the passed student dataset is 60% and 
for the failed student it is 40%.
"""
    )

    import matplotlib.pyplot as plt
    import seaborn as sns
    print("Relation between study hours and pass result")
    sns.scatterplot(x = df["Attendance"], y=df["FinalResult"])
    plt.show()

    print("Histogram of study hours")
    sns.histplot(data = df["StudyHours"])
    plt.show()

    
    print("Scatter plot between Study hours and Previous Score.")
    plt.figure(figsize=(7,5))


    for sp in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == sp]
        plt.scatter(temp["StudyHours"], temp["PreviousScore"], label = sp)

    plt.title("Student : Study Hour Vs Previous Score")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")

    plt.legend()
    plt.grid(True)
    plt.show()

    print("Boxplot for attendance:")
    plt.boxplot(x= df["Attendance"])
    plt.show()

    print("Relation between Assignment Completed and final result:")
    sns.scatterplot(x= df["AssignmentsCompleted"],y= df["FinalResult"])
    plt.show()

    sns.boxplot(x="FinalResult", y="AssignmentsCompleted", data=df)
    plt.show()

    sns.countplot(x="AssignmentsCompleted", hue="FinalResult", data=df)
    plt.show()

    print("Observation : For the students who completed more than 5 assignments have passed. Less than 5 Assignments students has failed.")

    print("Plot Sleeping hours vs Final Result")
    sns.scatterplot(x=df["SleepHours"], y=df["FinalResult"])
    plt.show()

    print("Observation : For a student to pass it is observed that atleast 6 hours of sleep is required.")

def main():
    student_performance_model("Assignment38-40/student_performance_ml.csv")
    

if __name__ == "__main__":
    main()