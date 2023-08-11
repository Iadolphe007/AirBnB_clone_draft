<h1>Air BnB Clone Project</h1>

<h3>Project Description</h3>
<br>
<p>This is the first part of the AirBnB clone project where we worked on the backend of the project whiles</p>
<p>interfacing it with a console application with the help of the cmd module in python.</p>
<br>
<h3>Description of the command interprete</h3>
<br>
<p>The interface of the application is just like the Bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website.</p>
<p>This command line interpreter serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.</p>
<p>Some of the commands available are:</p>
<ul>
<li>show</li>
<li>create</li>
<li>destroy</li>
<li>count</li>
</ul>

<h3>How to use it</h3>
<h4> <strong>interactive mode</strong></h4>
<div>
$ ./console.py
(hbnb) help

<p>Documented commands (type help <topic>):</p>
</p>========================================</p>
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
</div>
<h4><strong>non-interactive mode</strong></h4>
<div>
$ echo "help" | ./console.py
(hbnb)

<p>Documented commands (type help <topic>):</p>
<p>========================================</p>
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

<p>Documented commands (type help <topic>):</p>
<p>========================================</p>
EOF  help  quit
(hbnb) 
$
</h4>

