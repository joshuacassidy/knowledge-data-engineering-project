MSc Computer Science - Intelligent Systems
Module: CS7IS1 KNOWLEDGE AND DATA ENGINEERING
Names: Claire Farrell, Joshua Cassidy, Yifan Pei, Siddhesh Kankekar
Student Numbers: 16319148, 20300057, 20303063, 20300810 
Project Github repository: https://github.com/joshuacassidy/knowledge-data-engineering-project


WIDICO Documentation: eirebnb/eirebnb_doc
Application Code: eirebnb/eirebnb_application
Original Dataset: eirebnb/data
Uplifted Dataset: eirebnb/eirebnb_ontology.ttl


Project Dependencies (Note the specific version of all the Python dependencies can be found in requirements.txt):
1. Python3 (Note: ensure you have python mapped to the python3 environment variable)
2. flask
3. gunicorn
4. requests
5. pip (Note: ensure you have pip mapped to the pip3 environment variable)
6. Apache Jena Fueski 
7. Bash (version 3.2.57)

Install the Projects dependancies
The following steps detail how to install the projects python dependencies:
1. Use the cd command in order to navigate to the directory where the project has been downloaded
2. Run the "pip3 install -r requirements.txt" command to install the project's python dependencies (Note: ensure that you are connected to the internet)

Running the Project
The following steps detail how to run the project:
1. Use the cd command in order to navigate to the eirebnb folder in the downloaded project
2. Open up a new terminal window in the same directory and run the "fueski-server" command
3. Navigate to port 3030, click the "manage datasets" tab and create a new dataset called "eirebnb"
4. Click the upload data button and select the eirebnb_ontology.ttl file and click the upload all button. The database with the ontology models data will now be running
5. Open up a new terminal window and naviage to the "eirebnb_documentation" folder and the "python3 -m http.server" to run the documentation server. (Visit http://0.0.0.0:8000/doc/index-en.html to view the documentation)
6. Open up a new terminal window and run gunicorn -b 0.0.0.0:5000 "eirebnb_application:create_app()" to start the application server.
7. Navigate to 0.0.0.0:5000 in your browser to start using the eirebnb ontology.


Note: the repository for this project on GitHub does not have the data due to github's file size limits a full version of the project can be found at: https://drive.google.com/file/d/11QrpSco0Mga-vC4aV_QX76DRMVbyutgz/view?usp=sharing