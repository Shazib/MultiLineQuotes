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

import re 


re_quotes = re.compile("^(['\"])(.*)\\1$")

class MultiQuotesCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # Check for quotes
        v = self.view

        # Get current selection 
        (r,c) = self.view.rowcol(self.view.sel()[0].begin())

        # Get end of cursor position
        cursorPos = self.view.sel()[0].end()

        if v.sel()[0].size() == 0:
            v.run_command("expand_selection", {"to": "scope"})

        for sel in v.sel():
            text = v.substr(sel)
            res = re_quotes.match(text)
            if not res:
                # The current selection has no quotes
                # De-Select
                
                t = self.view.text_point(r,c);
                self.view.sel().clear()
                self.view.sel().add(sublime.Region(t))
                self.view.show(t)

                return

        
        for region in self.view.sel():
            
            # Get the line
            line = self.view.line(region) 

            # Add the +
            line_contents = ' ' + '+' '\n'
            self.view.insert(edit, cursorPos+1, line_contents)

            # Get line numbers and white space
            (row,col) = self.view.rowcol(line.begin())
            indent_region = self.view.find('^\s+', self.view.text_point(row, 0))
            if self.view.rowcol(indent_region.begin())[0] == row:
                indent = self.view.substr(indent_region)
            else:
                indent = ''

            # Move cursor to next line
            target = self.view.text_point(row+1, col)
            self.view.sel().clear()
            self.view.sel().add(sublime.Region(target))
            self.view.show(target)


            # Insert the quotes
            self.view.insert(edit, target, indent)
            line_conts = '"' + '"'
            self.view.insert(edit, self.view.sel()[0].begin(), line_conts)


            # Move cursor inside quotes
            (row,col) = self.view.rowcol(self.view.sel()[0].begin())
            target = self.view.text_point(row, col-1)
            self.view.sel().clear()
            self.view.sel().add(sublime.Region(target))
            self.view.show(target)

