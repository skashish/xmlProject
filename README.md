# xmlProject

Written in Django Framework, xmlProject is an app which takes the path of a folder as input and returns a well formed directory structure in xml format.

The xml file contains all the files and directories inside the given directory recursively.
All the files also have their md5sum along with their names.

# How to install (on Debian/Ubuntu family)

1. Make sure python3 is installed.
   If not installed, install using 
   
   `sudo apt-get install python3` 

2. Install python package manager pip.
  
   `sudo apt-get install python-pip`

3. Install Django
   
   `sudo pip3 install django`

4. Download this repository using
   
   `git clone https://github.com/skashish/xmlProject.git`

5. Change Working Directory. 
   
   `cd ./xmlProject/mysite`.

6. Run the server using 
   
   `python3 manage.py runserver`.

At this point, hopefully the server should be up and running. Visit http://127.0.0.1:8000 
on your browser to visit the website.

# Screenshots

<p align="left" style="margin: 20px">
  <img src="http://i.imgur.com/6L7wV7l.png" width="250"/>
  <img align = "right" src="http://i.imgur.com/4mAbHz0.png" width="300"/>
</p>
<br/>
<p align="center">
   <img src="http://i.imgur.com/OAYcUM3.png">
</p>
