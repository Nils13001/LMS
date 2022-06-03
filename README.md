<h1> Library Management System </h1>
<p>The project is based on the connectivity between Python and MySQL, through pymysql module of python. This project is based on Library management system (LMS).
<p>This Project has been developed using the PYTHON programming Language through IDLE 3.7.4 (64 bits) and MYSQL 5.1 database at the backend. 
<p>This system will control all details related to a LIBRARY like Book Issue/Return, Add/Delete/Edit New Member/Books, View all issued books etc.
<p>In our project, we are storing data of :
<li>All the books present in library
<li>All the members of library
<li>Books issued by the members
<p> <b>Here, only those can issue the books, who are the members of library.</b>
<p>The tables storing the above mentioned data are "books"," members" and "issue" respectively, created in database "project_library_management". The "books" table has column "b_code" as primary key and "members" table has column "ID_NO" as primary key. Through these two columns, the tables are individually linked with table "issue" using concept of Foreign key. The tables of MySQL  acts as only a medium for storing and retrieving data. All the major input/output work is being done in Python.  
<p>In Python, we have created four modules, each handling the work of Book Management (book_op.py), Member Management (mem_op.py), Books issued/returned (is_or_re.py) and the last for showing the main menu and taking choice input from user (menu.py). All these modules are integrated in a single, MAIN file, LMS.py, which makes use of all these modules to present the final project.
  
  <h3><b>  Modules Created:</b></h3>

<li>book_op.py
<li>mem_op.py
<li>is_or_re.py
<li>menu.py
 <p> <b> Note: LMS is also a module but its the main program</b>

  <h3>In-Built Modules Used:</h3>

  <li><b>pymysql:</b> (For establishing connectivity between MySQL and Python)
  <li><b>datetime:</b> (For converting string into date)

  <h3>Database Created:</h3>
  <li>Project_library_management

<h3>Tables Created: </h3>
<li>books
<li>members
<li>issue

  <h2> Structure of Tables Created and Sample Data.</h2>
  <h3><u>books</u></h3>
  
![image](https://user-images.githubusercontent.com/73545828/171647195-9f29031b-420a-43ad-978a-44b28e126586.png)
  
![image](https://user-images.githubusercontent.com/73545828/171647913-042d27ed-54b4-4ece-9871-0f623c055a54.png)

  <h3>issue</h3>
  
![image](https://user-images.githubusercontent.com/73545828/171648313-dad54945-aa4f-4939-afee-f7fe0b792c1a.png)
  
![image](https://user-images.githubusercontent.com/73545828/171648399-cf48de96-7121-4f1b-8b19-99ff849c98bc.png)

  
  <h3>members</h3>
  
![image](https://user-images.githubusercontent.com/73545828/171648548-883585ef-12d5-470b-9c21-72534c0716dd.png)
  
![image](https://user-images.githubusercontent.com/73545828/171648659-eda8964d-b96f-414b-8ced-a0c1bfc54f68.png)

  <h3>Output Screenshots</h3>
  
  ![image](https://user-images.githubusercontent.com/73545828/171651367-4b0c900c-7de4-4801-ae4f-da46f4b69a87.png)
  
  ![image](https://user-images.githubusercontent.com/73545828/171651588-80748330-0e47-482e-88c5-06f799a2da0b.png)
  ![image](https://user-images.githubusercontent.com/73545828/171652117-1e05b8b2-e779-4032-8437-9a1667ecc592.png)

  ![image](https://user-images.githubusercontent.com/73545828/171652399-32b51d26-ac6b-443a-977f-f56f3c652659.png)
  
  ![image](https://user-images.githubusercontent.com/73545828/171655750-00b3ea60-e7ef-4da3-aaea-310d83acd8a5.png)
  
  ![image](https://user-images.githubusercontent.com/73545828/171656021-b853377e-1a34-4acd-aa20-e59b87291e73.png)
