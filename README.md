Django Error Helper LLDB Command
================================

This handful of python scripts is intended to be used as a new LLDB command for conveniently delivering a received Django error in a browser.

The intended purpose is to setup a break point with a break point action from within a project (like an iOS app). The breakpoint should be placed at a point when Django returns to your project a response string. This response string could be saved into a variable named `responseString`. The breakpoint action should be setup to call the debugger command `dde` ("Deliver Django Error") with the response string as an argument (i.e. `dde responseString`). Installation details below.

This new LLDB command uses a variable passed in such as `dde responseString`. If such a variable is found and if it contains an html tag then the function will save the html file to the desktop and open the document with a browser.

For more information on using the lldb debugger I highly recommend watching [WWDC session videos on LLDB](https://developer.apple.com/wwdc/videos/) and also checking out the [LLDB documentation](http://lldb.llvm.org)

Enjoy!

==============

### To install: ###

1. Save all the files to your `~/Documents/lldb-python-scripts` directory.
2. Move the .lldbinit file to your `~` directory. Start Xcode.
3. Add a breakpoint where you receive a Django response into a NSString variable. Add a breakpoint action to this breakpoint: debugger command `dde responseString` (in this example `responseString` is the NSString containing the server response). I recommend adding this breakpoint with breakpoint action from the Xcode UI but you can also add this breakpoint with breakpoint action from the command line. Below is an example of adding the breakpoint in our project via command line.

```
(lldb) breakpoint set --file BoomsetDoormanOrientationViewController.m --line 581
Breakpoint 11: where = Checkin`-[BoomsetDoormanOrientationViewController doneGuestlistStatus:] + 311 at BoomsetDoormanOrientationViewController.m:585, address = 0x00075047
(lldb) breakpoint command add 11
Enter your debugger command(s).  Type 'DONE' to end.
> dde responseString
> DONE
We did not receive a response from the server that included the string <!DOCTYPE html> so I do not think we received a Django Error.
(lldb) 
```
