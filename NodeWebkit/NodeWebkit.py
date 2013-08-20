import os, sublime_plugin, re, sublime
class NodeWebkitCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        fileName = self.view.file_name()
        path = fileName.split("\\")
        currentDriver = path[0]
        path.pop()
        currentDirectory = "\\".join(path)
        dirs = self.view.window().folders()

        for (i, d) in enumerate(dirs):
	        d = re.sub("\\\\", "\\\\\\\\", d)
	        matchObj = re.match(d, currentDirectory)

        	if matchObj:
        		command = "nw " + dirs[i]
        		sublime.status_message(command)
	        	os.system(command)
	        	break