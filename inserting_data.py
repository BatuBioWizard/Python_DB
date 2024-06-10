import sqlite3
import csv
from functions import *

def inserting_subject(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        
        try:
            with open('Subject.csv', "r") as file:
                reader = csv.reader(file)
                headers = next(reader)

                cleaned_subject = []
                for row in reader:
                    cleaned_row = [data_cleaning(value) for value in row]
                    cleaned_subject.append(cleaned_row)
            
                for row in cleaned_subject:
                    cursor.execute(
                    """INSERT INTO Subject (SubjectID, Race, Sex, Age, BMI, SSPG, IR_IS_Classification)
                    VALUES (?, ?, ?, ?, ?, ?, ?)""", tuple(row)                
                    )
                
            db.commit()
        except FileNotFoundError:
            print(f'File Subject.csv not found. Your database still loaded other files.')
            
def inserting_metabolome_annotation(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        try:
            with open('HMP_Metabolome_annotation.csv', "r") as file:
                reader = csv.DictReader(file)
            
                for row in reader:
                    peak_id = row['PeakID']
                    metabolite = row['Metabolite'].split('|')
                    kegg_list = row['KEGG'].split('|') if row['KEGG'] else ['']*len(metabolite)
                    hmdb_list = row['HMDB'].split('|') if row['HMDB'] else ['']*len(metabolite)
                    chemical_class = row['Chemical Class']
                    pathway = row['Pathway']
                    
                    
                    for i, meta_name in enumerate(metabolite):
                        cleaned_metabolite = merge_names(meta_name)
                        kegg = kegg_list[i] if len(kegg_list) else ''
                        hmdb = hmdb_list[i] if len(hmdb_list) else ''
                        
                        cursor.execute(
                        """INSERT INTO Metabolome (PeakID, Metabolite, KEGG, HMDB, Chemical_Class, Pathway)
                        VALUES (?, ?, ?, ?, ?, ?)""", (peak_id, cleaned_metabolite, kegg, hmdb, chemical_class, pathway)
                        )
                    
            db.commit()
        except FileNotFoundError:
            print(f'File HMP_metabolome_annotation.csv not found. Your database still loaded other files.')
            
def inserting_metabolome_abundance(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()    
        try:
            with open('HMP_metabolome_abundance.tsv', "r") as file:
                reader = csv.reader(file, delimiter='\t')
                headers = next(reader)
                
                for row in reader:
                    sample_id = row[0]
                    subject_id, visit_id = sample_id.split('-')
                    cursor.execute(
                    """INSERT OR IGNORE INTO Visit (VisitID, SubjectID)
                    VALUES (?, ?)""", (visit_id, subject_id)
                    )
                    cursor.execute(
                    """INSERT OR IGNORE INTO Sample (SampleID, SubjectID, VisitID)
                    VALUES (?, ?, ?)""", (sample_id, subject_id, visit_id)
                    )
                    cursor.execute(
                    """INSERT INTO Metabolome_Abundance (SampleID)
                    VALUES (?)""", (sample_id,)
                    )
                db.commit()

        except FileNotFoundError:
            print(f'File HHMP_metabolome_abundance.tsv not found. Your database still loaded other files.')
            
def inserting_proteome_abundance(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()           
        try:
            with open('HMP_proteome_abundance.tsv', "r") as file: 
                reader = csv.reader(file, delimiter='\t')
                headers = next(reader)
                
                for row in reader:
                    sample_id = row[0]
                    subject_id, visit_id = sample_id.split('-')
                    cursor.execute(
                    """INSERT OR IGNORE INTO Visit (VisitID, SubjectID)
                    VALUES (?, ?)""", (visit_id, subject_id)
                    )
                    cursor.execute(
                    """INSERT OR IGNORE INTO Sample (SampleID, SubjectID, VisitID)
                    VALUES (?, ?, ?)""", (sample_id, subject_id, visit_id)
                    )
                db.commit()

        except FileNotFoundError:
            print(f'File HMP_proteome_abundance.tsv not found. Your database still loaded other files.')
          
def inserting_transcriptome_abundance(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()               
        try:
            with open('HMP_transcriptome_abundance.tsv', "r") as file:
                reader = csv.reader(file, delimiter='\t')
                headers = next(reader)
                
                for row in reader:
                    sample_id = row[0]
                    subject_id, visit_id = sample_id.split('-')
                    a1bg = row[1]
                    cursor.execute(
                    """INSERT OR IGNORE INTO Visit (VisitID, SubjectID)
                    VALUES (?, ?)""", (visit_id, subject_id)
                    )
                    cursor.execute(
                    """INSERT OR IGNORE INTO Sample (SampleID, SubjectID, VisitID)
                    VALUES (?, ?, ?)""", (sample_id, subject_id, visit_id)
                    )
                    cursor.execute(
                    """INSERT INTO Transcriptome_Abundance (SampleID, A1BG)
                    VALUES (?, ?)""", (sample_id, a1bg)
                    ) 
                    
                db.commit()

        except FileNotFoundError:
            print(f'File HMP_transcriptome_abundance.tsv not found. Your database still loaded other files.')
            




