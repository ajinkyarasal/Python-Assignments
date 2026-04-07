import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def student_performance_model(data_path):
    border = "-"*30
    #Load Dataset
    df = pd.read_csv(data_path)
    print(border)
    print("Printing first few records:")
    print(border)
    print(df.head())
    print("Shape of dataset : ",df.shape)
    print("Check for empty values : ")
    print(df.isnull().sum())
    print(border)
    print("Separate independent and dependent variables")
    print(border)

    X = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]]
    Y = df["FinalResult"]

    print("Shape of X :",X.shape)
    print("Shape of Y :",Y.shape)

    print(border)
    print("Split the data for training and testing")
    print(border)

    X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    print("Shape of X train : ",X_train.shape)
    print("Shape of X test : ",X_test.shape)
    print("Shape of Y train : ",Y_train.shape)
    print("Shape of Y test : ",Y_test.shape)

    print(border)
    print("Create and train the model:")
    print(border)

    model =  DecisionTreeClassifier()



def main():
    student_performance_model('student_performance_ml.csv')
    

if __name__ == "__main__":
    main()