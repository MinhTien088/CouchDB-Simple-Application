# CouchDB-Simple-Application

This repository contains a JSP Servlet project that demonstrates the implementation of basic CRUD (Create, Read, Update, Delete) operations with CouchDB, a NoSQL database management system.

## Contents

1. `project_demo_couchdb`: A directory containing the JSP Servlet application for interacting with CouchDB.
2. `script_Python.py`: A Python script that allows you to import and export data from JSON files to CouchDB.
3. JSON files:
  - `demo_bigdata.json`: A sample JSON file containing data for demonstration purposes.
  - `demo_database.json`: Another sample JSON file with data for demonstration purposes.
  - `stocks.json`: A JSON file containing stock-related data.

## Prerequisites

Before running the project, ensure that you have the following software installed:

- Java Development Kit (JDK)
- Apache Tomcat (or any other compatible web server)
- Python (for running the `script_Python.py` file)
- CouchDB installed and running on your system

## Getting Started

1. Clone the repository to your local machine.
2. Import the `project_demo_couchdb` directory into your preferred Java Integrated Development Environment (IDE).
3. Configure the project to run on your web server (e.g., Apache Tomcat).
4. Start the CouchDB server on your system.
5. Deploy the JSP Servlet application to your web server.
6. Access the application through your web browser using the appropriate URL.

## Using the Python Script

The `script_Python.py` file allows you to import and export data from JSON files to CouchDB. To use the script, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory containing the `script_Python.py` file.
3. Run the script using the following command: `python script_Python.py`
4. Follow the prompts in the script to import or export data from/to the JSON files.

## Sample JSON Files

The repository includes the following sample JSON files:

- `demo_bigdata.json`: This file contains sample data for demonstration purposes.
- `demo_database.json`: Another file with sample data for demonstration purposes.
- `stocks.json`: This file contains stock-related data.

You can use these JSON files to populate your CouchDB database or modify them as needed for your specific use case.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

Special thanks to [nguyenhoanthao](https://github.com/nguyenhoanthao) for his contributions to this project.

## License

This project is licensed under the [MIT License](LICENSE).
