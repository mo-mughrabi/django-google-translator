INTRODUCTION
-----

This simple package is to use for running your .PO files for translation against google translation API.
The package will extend your django command interface with a new command to retrieve all your .PO files,
translate the strings and update the .PO file with its translation (remember, this utility will not generate
the .mo files for you) it will place the translated strings inside the .PO file.


INSTALL
-----

to install run the following

      $ pip install git+https://github.com/mo-mughrabi/django-google-translator/tree/master


WARNING
-----

Be aware running the command will cause it to go through all strings even translated ones.


TODO
-----

1. Create parameter for allowing skipping of existing strings
2. Maintain special characters in msgid when translating such as "\n"