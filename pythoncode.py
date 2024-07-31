import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("dataset.csv")
def classa(classname):
    classdf=df[df["Class"]==classname].copy()
    classdf["Average"]=classdf[['Exam1','Exam2','Exam3','Exam4','Exam5']].mean(axis=1)
    leastid=classdf.loc[classdf["Average"].idxmin()]['Rollno']
    leastname=classdf.loc[classdf["Average"].idxmin()]['Name']
    mostid=classdf.loc[classdf["Average"].idxmax()]['Rollno']
    mostname=classdf.loc[classdf["Average"].idxmax()]['Name']
    classavg=classdf[['Exam1','Exam2','Exam3','Exam4','Exam5']].mean()
    print("Least score:-\n","ID:",leastid,"\tName:",leastname)
    print("Most score:-\n","ID:",mostid,"\tName:",mostname)
    print("Class Averages:")
    print(classavg)
    classavg.plot(kind='bar')
    plt.title('Class Performance Analysis Graph')
    plt.xlabel('Exam')
    plt.ylabel('Average')
    plt.xticks(rotation=0)
    plt.ylim(0,100)
    plt.show()
def stud(studentid):
    studentdf=df[df["Rollno"]==studentid].copy()
    scores=studentdf[['Exam1','Exam2','Exam3','Exam4','Exam5']].iloc[0]
    name=studentdf[['Name']].iloc[0]
    print("Student name:",name)
    scores.plot(kind='bar')
    plt.title('Student Performance Analysis Graph')
    plt.xlabel('Exam')
    plt.ylabel('Score')
    plt.xticks(rotation=0)
    plt.ylim(0,100)
    plt.show()
def main():
    choice=int(input("Would you like to analyse class performance(Enter 1) or student performance(Enter 2)?"))
    if choice==1:
        c=input("Which class?:").strip()
        classa(c)
    elif choice==2:
        r=int(input("Enter student roll number:").strip())
        stud(r)
    else:
        print("Invalid choice!")
if __name__ == "__main__":
    main()
