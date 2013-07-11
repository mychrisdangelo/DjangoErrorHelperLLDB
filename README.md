DjangoErrorHelperLLDB
=====================

This handful of python scripts is intended to be used as a new LLDB command.

The intended purpose is to set a break point from within a project (like an iOS app) and when receiving a response string from the Django framework the breakpoint should have the breakpoint action to call the debugger command "dde" (which stands for Deliver Django Error").

This new LLDB command then searches fro the variable named "data". If such a variable is found and if it contains an html tag then the function will save the html file to the desktop and open the browser.

Enjoy!


To install:

1. Save all the files to your '~/Documents' directory
2. Move the .lldbinit file to your '~' directory. Start XCode. 
