#!/usr/bin/python
#
# Chris D'Angelo
# 7/11/13
# 
# This function is intended to be called via lldb (Apple's Debugger)
# It should be paired with an application that is utilizing the Django Framework
# When the application receives a response from the server (in our application named "data")
# This function tests to see if it has an html tag and if it does it saves the string
# (an html file) to the desktop and opens a web browser automatically to view it.
# 
# Invaluable Resources: 
# 	http://www.libertypages.com/clarktech/?p=4303
# 	http://lldb.llvm.org
# 

# expectation is that .lldbinit is in place (see README)
import lldb, os
import webbrowser

def deliverDjangoError(debugger,user_input,result,unused):
	"""Saves any Django error to the desktop and opens the file in your browser in a new tab"""

	# This is how we might obtain thread and function name information
	# but not necessary for our goals
	# 
	# thread = debugger.GetSelectedTarget().GetProcess().GetSelectedThread()
	# name = thread.GetFrameAtIndex(0).function.name
 
	djangoErrorHtml = lldb.frame.FindVariable("data").GetObjectDescription()

	if djangoErrorHtml.find('<!DOCTYPE html>') > 0:
		# write the error to file
		absolutePath = os.path.expanduser('~/Desktop/djangoError.html')
		outFile = open(absolutePath, 'w+')
		htmlString = str(djangoErrorHtml)
		outFile.write(htmlString)
		outFile.close()
		
		print 'Uh Oh! Django Error! Your browser should contain the Django Error. The error document has been saved to %s' % absolutePath
		
		# open the file in the browser
		localUrl = 'file://' + absolutePath
		webbrowser.open_new_tab(localUrl)

		# print >>result, "depth: " + str(name)
	else:
		print 'We did not receive a response from the server that included the string <!DOCTYPE html> so I do not think we received a Django Error.'
