# PocketbookAnnotations

This repository provides a way to extract annotations from PocketBook sqlite database.

Current functionality:

* Tested on Ubuntu 16.04 with PocketBook Touch HD 2. I'll be glad to add some other platforms, but I need someone to give me database for testing.
* VueJS+HTML UI, in plans adding desktop interface 
* Allows to view annotations by book and export them in one Markdown file
* Tested on Ubuntu 16.04 with python 3.6+
* Open PDF files on annotated page (Ubuntu based systems only)
* Worked on Windows with some limitations:

    * Opening PDF editor not allowed. Only viewing and downloading annotations

Plans:

* Port on MacOS systems
* Desktop UI and executable bundle
* Mark annotations as processed and don't show them (save state on the disk)

### Requirements:

* python 3.6+
* pipenv
* Linux based system (Tested on Ubuntu 16.04)

### Installation:

1. You should check you have pipenv installed.
2. Clone this project:
```
git clone git@github.com:sallyruthstruik/PocketbookAnnotations.git
cd PocketbookAnnotations/
``` 
3. Install requirements: 
```
pipenv install
```

4. Connect your device and get device root path

5. Execute:
```
pipenv run python guis/run.py browser <path to mounted pocketbook>
```

this command will run webbrowser with books page. Books are sorted by annotations count. On that page you can download all annotations per book, or click on "Annorations" button and explore.

### Interface

On the main page you'll see all books in the system sorted by annotation count:

![](http://wwwscr.digitalaccess.ru/screen-20181211-961f0.jpg)

You can download all annotations per book (by clicking Download button), or watch them (by clicking Annotations button):

![](http://wwwscr.digitalaccess.ru/screen-20181211-4eacb.jpg)
