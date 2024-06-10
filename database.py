import sqlite3

def db_creation(db_name):
    database = """
    PRAGMA foreign_keys = ON;

    CREATE TABLE IF NOT EXISTS Subject (
        SubjectID TEXT PRIMARY KEY,
        Race TEXT,
        Sex TEXT,
        Age REAL,
        BMI REAL,
        SSPG REAL,
        IR_IS_Classification TEXT
    );

    CREATE TABLE IF NOT EXISTS Metabolome (
        PeakID TEXT,
        Metabolite TEXT,
        KEGG TEXT,
        HMDB TEXT,
        Chemical_Class TEXT,
        Pathway TEXT
    );

    CREATE TABLE IF NOT EXISTS Visit (
        VisitID TEXT,
        SubjectID TEXT,
        PRIMARY KEY (VisitID, SubjectID),
        FOREIGN KEY (SubjectID) REFERENCES Subject(SubjectID)
    );

    CREATE TABLE IF NOT EXISTS Sample (
        SampleID TEXT,
        SubjectID TEXT,
        VisitID TEXT,
        FOREIGN KEY (SubjectID) REFERENCES Subject(SubjectID),
        FOREIGN KEY (VisitID) REFERENCES Visit(VisitID)
    );

    CREATE TABLE IF NOT EXISTS Metabolome_Abundance (
        SampleID TEXT PRIMARY KEY,
        FOREIGN KEY (SampleID) REFERENCES Sample(SampleID)
    );

    CREATE TABLE IF NOT EXISTS Transcriptome_Abundance (
        SampleID TEXT PRIMARY KEY,
        A1BG REAL,
        FOREIGN KEY (SampleID) REFERENCES Sample(SampleID)
    );
    """

    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.executescript(database)
        db.commit()


