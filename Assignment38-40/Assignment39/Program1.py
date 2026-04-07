import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

def main():
    border = "-"*50

    print(border)
    print(" Step 1 : Load dataset")
    print(border)

    df = pd.read_csv("Assignment38-40/student_performance_ml.csv")
    print(df.head())

    print(border)
    print("Step 2 : Decide Independent and Dependent variable")
    print(border)

    X = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]]
    Y = df["FinalResult"]

    print("Shape of Independent variables : ",X.shape)
    print("Shape of Dependent variables : ",Y.shape)

    print(border)
    print("Step 3 : Split test train data")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)
    print("Shape of X_train : ",X_train.shape)
    print("Shape of X_test : ",X_test.shape)
    print("Shape of Y_test : ",Y_test.shape)
    print("Shape of Y_train : ",Y_train.shape)

    print(border)
    print("Step 4 : Model Selection and Training")
    print(border)

    model = DecisionTreeClassifier()
    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    print(border)
    print("Step 5 : Calculate Accuracy Score:")
    print(border)

    accuracy_org = accuracy_score(Y_test,Y_pred)
    print(f"Accuracy of the model is {accuracy_org * 100} %" )

    print(border)
    print("Confusion Matrix")
    print(border)

    cm = confusion_matrix(Y_test,Y_pred)
    print(cm)

    print(border)
    print("Plot confusion matrix")
    print(border)

    data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
    data.plot()

    plt.title("Confusion matrix for Student performance.")
    plt.show()

    print(border)
    print("Calculate Training accuracy")
    print(border)
    Y_train_pred = model.predict(X_train)
    print(accuracy_score(Y_train,Y_train_pred))

    print(border)
    print("Calculate accuracy with different max depth values:")
    print(border)
    print("Model with max_depth as None accuracy score is : ", accuracy_org)
    model1 = DecisionTreeClassifier(max_depth=1)
    model1.fit(X_train,Y_train)
    Y_pred1 = model1.predict(X_test)
    print("Model1 with max_depth as 1 accuracy score is : ", accuracy_score(Y_test,Y_pred1))

    model2 = DecisionTreeClassifier(max_depth=2)
    model2.fit(X_train,Y_train)
    Y_pred2 = model2.predict(X_test)
    print("Model2 with max_depth as 2 accuracy score is : ", accuracy_score(Y_test,Y_pred2))

    print(border)
    print("Test model on external data:")

    X_test_ext = {
        "StudyHours" : [6],
        "Attendance" : [85],
        "PreviousScore" : [66],
        "AssignmentsCompleted" : [7],
        "SleepHours" : [7]
    }
    df = pd.DataFrame(X_test_ext)
    y_pred_ext = model.predict(df)
    if y_pred_ext[0] == 1:
        print("The student is predicted to be passed.")
    else:
        print("The student is predicted to be failed.")

    


if __name__ == "__main__":
    main()