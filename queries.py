import sqlite3
import matplotlib.pyplot as plt

def query_1(cursor):
    cursor.execute(
        """SELECT SubjectID, Age 
        FROM Subject 
        WHERE Age >70"""
        )
    return [f"{row[0]} {row[1]}" for row in cursor.fetchall()]
        

def query_2(cursor):
    cursor.execute(
        """SELECT SubjectID
        FROM Subject
        WHERE Sex='F' AND BMI BETWEEN 18.5 AND 24.9
        ORDER BY BMI DESC"""
        )
    return [f"{row[0]}" for row in cursor.fetchall()]


def query_3(cursor):
    cursor.execute(
        """SELECT VisitID
        FROM Visit
        WHERE SubjectID = 'ZNQOVZV'
        """
        )
    return [f"{row[0]}" for row in cursor.fetchall()]


def query_4(cursor):
    cursor.execute(
        """SELECT DISTINCT Subject.SubjectID FROM Subject
        INNER JOIN Sample ON Subject.SubjectID = Sample.SubjectID
        INNER JOIN Metabolome_Abundance ON Sample.SampleID = Metabolome_Abundance.SampleID
        WHERE Subject.IR_IS_Classification = 'IR'           
        """
        )
    return [f"{row[0]}" for row in cursor.fetchall()]


def query_5(cursor):
    cursor.execute(
        """SELECT DISTINCT KEGG 
        FROM Metabolome 
        WHERE PeakID 
        IN ('nHILIC_121.0505_3.5', 'nHILIC_130.0872_6.3', 'nHILIC_133.0506_2.3', 'nHILIC_133.0506_4.4')
        """
        )
    return [f"{row[0]}" for row in cursor.fetchall()]


def query_6(cursor):
    cursor.execute(
        """SELECT MIN(Age) AS MinimumAge, MAX(Age) AS MaximumAge, AVG(Age) AS AverageAge
        FROM Subject"""    
        )
    results = cursor.fetchall()
    return [f"{row[0]} {row[1]} {row[2]:.2f}" for row in results]


def query_7(cursor):
    cursor.execute("""
        SELECT Pathway, COUNT(*) AS Count
        FROM Metabolome
        WHERE Pathway <> ''
        GROUP BY Pathway
        HAVING COUNT(*) >= 10
        ORDER BY COUNT(*) DESC
        """
        )
    return [f"{row[0]} {row[1]}" for row in cursor.fetchall()]


def query_8(cursor):
    cursor.execute(
        """SELECT MAX(A1BG) 
        FROM Transcriptome_Abundance
        JOIN Sample ON Transcriptome_Abundance.SampleID = Sample.SampleID
        WHERE Sample.SubjectID = 'ZOZOW1T'
        """
        )
    results = cursor.fetchone()
    return f"{results[0]}"


def query_9(cursor):
    cursor.execute(
        """SELECT SubjectID, Age, BMI
        FROM Subject
        WHERE Age IS NOT NULL AND BMI IS NOT NULL    
        """
        )
    return [f"{row[0]} {row[1]} {row[2]}" for row in cursor.fetchall()]


def query_and_plot(db_cursor, db_name):
    
    db_cursor.execute(
        """SELECT Age, BMI
        FROM Subject
        WHERE Age IS NOT NULL AND BMI IS NOT NULL    
        """
    )
    results = db_cursor.fetchall()

    age, bmi = zip(*results)

    
    plt.figure(figsize=(10, 6))
    plt.scatter(age, bmi, color='blue', alpha=0.5)
    plt.title('Scatter Plot of Age vs BMI')
    plt.xlabel('Age')
    plt.ylabel('BMI')
    plt.grid(True)

    
    plot_file = 'age_bmi_scatterplot.png' 
    plt.savefig(plot_file)