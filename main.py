import sqlite3
import argparse
from functions import *
from queries import *
from database import *
from inserting_data import *


def main():
    parser = argparse.ArgumentParser(description= "Database Assignment 2&3" , allow_abbrev = False )
    parser.add_argument("db_name", type =db_format , help="Database name")
    parser.add_argument("--createdb", action="store_true", help="Creating the database structure")
    parser.add_argument("--loaddb", action="store_true", help="Loading data into the database")
    parser.add_argument("--querydb", type=int, help="Run a specific query between 1-9)")
    args = parser.parse_args()

    if args.createdb:
        db_creation(args.db_name)
        

    if args.loaddb:
        inserting_subject(args.db_name)
        inserting_metabolome_annotation(args.db_name)
        inserting_metabolome_abundance(args.db_name)
        inserting_proteome_abundance(args.db_name)
        inserting_transcriptome_abundance(args.db_name)
        

    if args.querydb is not None:
        
        with sqlite3.connect(args.db_name) as db:
            cursor = db.cursor()
            if args.querydb == 1:
                results = query_1(cursor)
                for result in results:
                    print(result)
            elif args.querydb == 2:
                results = query_2(cursor)
                for result in results:
                    print(result)
            elif args.querydb == 3:
                results = query_3(cursor)
                for result in results:
                    print(result)
            elif args.querydb == 4:
                results = query_4(cursor)
                for result in results:
                    print(result)
            elif args.querydb == 5:
                results = query_5(cursor)
                for result in results:
                    print(result)
            elif args.querydb == 6:
                results = query_6(cursor)
                for result in results:
                    print(result)
            elif args.querydb == 7:
                results = query_7(cursor)
                for result in results:
                    print(result)
            elif args.querydb == 8:
                results = query_8(cursor)
                print(results)
            elif args.querydb == 9:
                query_and_plot(cursor, args.db_name)
                results = query_9(cursor)
                for result in results:
                    print(result)
            else:
                print(f'Query number that you type is not in the range, please right numbers between 1-9')

if __name__ == "__main__":
    main()


