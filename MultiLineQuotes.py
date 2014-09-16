"""
import sublime, sublime_plugin

class DuplicateLineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                line = self.view.line(region)
                line_contents = self.view.substr(line) + '\n'
                self.view.insert(edit, line.begin(), line_contents)
            else:
                self.view.insert(edit, region.begin(), self.view.substr(region))
"""

import sublime, sublime_plugin
class MultiQuotesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Get Current Selection
      for region in self.view.sel():
        # If selection is empty, i.e. cursor is on a line with nothing selected
        if region.empty(): 
            # Get the line
            line = self.view.line(region) 

            # add the +
            line_contents = ' ' + '+' 
            self.view.insert(edit, line.end(), line_contents)

            #get line numbers to move cursor
            (row,col) = self.view.rowcol(line.begin())
            indent_region = self.view.find('^\s+', self.view.text_point(row, 0))
            if self.view.rowcol(indent_region.begin())[0] == row:
                indent = self.view.substr(indent_region)
            else:
                indent = ''

            #move cursor

            target = self.view.text_point(row+1, col)
            self.view.sel().clear()
            self.view.sel().add(sublime.Region(target))
            self.view.show(target)

            self.view.insert(edit, target, indent)
            line_conts = '"' + '"'
            self.view.insert(edit, self.view.sel()[0].begin(), line_conts)

            
           # move cursor inside quotes

            (row,col) = self.view.rowcol(self.view.sel()[0].begin())
            target = self.view.text_point(row, col-1)
            self.view.sel().clear()
            self.view.sel().add(sublime.Region(target))
            self.view.show(target)

            
            #self.view.insert(edit, self.view.text_point, line_conts)
