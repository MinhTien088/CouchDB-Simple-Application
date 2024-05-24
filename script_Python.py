import couchdb
import json
import pandas as pd
import sys

pd.set_option('display.max_columns', None)

def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        str_conn = f"http://{username}:{password}@localhost:5984"
        couch = couchdb.Server(str_conn)

        try:
            # Try connecting to CouchDB to authenticate the login
            couch.version()
            print("Logged in successfully.")
            return couch  # Return CouchDB instance upon successful login
        except couchdb.Unauthorized as e:
            if e:
                print("Login unsuccessful. Please try again.")
            else:
                print("An error occurred:", e)
                # In case of other errors, exit the loop or handle accordingly
                break

def display_first_10_documents(db):
    all_docs = []
    count = 0
    for doc_id in db:
        if count < 10:
            doc = db.get(doc_id)
            count += 1
            all_docs.append(doc)
        else:
            break
    
    df = pd.DataFrame(all_docs)
    print(df)

def display_all_documents(db):
    all_docs = []
    for doc_id in db:
        doc = db.get(doc_id)
        all_docs.append(doc)

    df = pd.DataFrame(all_docs)
    print(df)

def import_from_json_file(db, file_path):
    if file_path:
        with open(file_path) as jsonfile:
            for row in jsonfile:
                db_entry = json.loads(row)
                doc_id = db_entry.get('_id')

                if doc_id is None:
                    db.save(db_entry)
                else:
                    existing_doc = db.get(doc_id)
                    existing_doc.update(db_entry)
                    db.save(existing_doc)
        print("Successfully imported from JSON file.")
    else:
        print("File not selected.")

def export_to_json_file(db, db_name):
    all_docs = []
    for doc_id in db:
        doc = db.get(doc_id)
        all_docs.append(doc)

    df = pd.DataFrame(all_docs)
    df.to_json(f'{db_name}.json', orient='records', lines=True)
    print("Successfully exported to JSON file.")

def main():
    print("\nIMPORT, EXPORT, VIEW DATABASE DATA IN COUCHDB")
    couch = login()
    db_name = input("\nEnter database name: ")
    db = couch[db_name] if db_name in couch else couch.create(db_name)
    while True:
        print("\n---- MENU ----")
        print("1. View the first 10 documents")
        print("2. View all documents")
        print("3. Import from JSON file")
        print("4. Export to JSON file")
        print("5. Exit")
        choice = input("Select function (1-5): ")

        if choice == "1":
            display_first_10_documents(db)
        elif choice == "2":
            display_all_documents(db)
        elif choice == "3":
            file_path = input("Enter file path: ")
            import_from_json_file(db, file_path)
        elif choice == "4":
            export_to_json_file(db, db_name)
        elif choice == "5":
            db = None
            couch = None
            print("Thank you! Bye.")
            sys.exit()
        else:
            print("Chức năng không hợp lệ. Vui lòng chọn lại.")

if __name__ == '__main__':
    main()
