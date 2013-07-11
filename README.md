Django Error Helper LLDB Command
================================

This handful of python scripts is intended to be used as a new LLDB command for conveniently delivering a received Django error in a browser.

The intended purpose is to setup a break point with a break point action from within a project (like an iOS app). The breakpoint should be placed at a point when Django returns to your project a response string. This response string should be saved into a variable named `data` in order for this function to work without changes. The breakpoint action should be setup to call the debugger command `dde` ("Deliver Django Error"). Installation details below.

This new LLDB command then searches for the variable named `data`. If such a variable is found and if it contains an html tag then the function will save the html file to the desktop and open the document with a browser.

For more information on using the lldb debugger I highly recommend watching [WWDC session videos on LLDB](https://developer.apple.com/wwdc/videos/) and also checking out the [LLDB documentation](http://lldb.llvm.org)

Enjoy!

==============

### To install: ###

1. Save all the files to your `~/Documents` directory.
2. Move the .lldbinit file to your `~` directory. Start Xcode.
3. From Xcode create a breakpoint where you receive a Django response to a variable named `data`. Add a breakpoint action to this breakpoint: debugger command `dde`.
