import sublime, sublime_plugin, re

re_quotes = re.compile("^([\"])(.*)\\1$")

re_singlequotes = re.compile("^(['])(.*)\\1$")

class MultiQuoteCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # Check for quotes
        v = self.view
        # Get current selection 
        (r,c) = self.view.rowcol(self.view.sel()[0].begin())

        a = 0

        if v.sel()[0].size() == 0:
            v.run_command("expand_selection", {"to": "scope"})

        for sel in v.sel():
            text = v.substr(sel)
            res = re_quotes.match(text)
            if res:
                # Double Quotes
                print("Double Quotes")
                a = 1
                continue         
            if not res:
                for sel in v.sel():
                    text = v.substr(sel)
                    res = re_singlequotes.match(text)
                    if res:
                        # Single Quotes
                        a = 0
                        print("is a single quote")
                        continue
                    if not res:
                        # Unselect everything
                        target = self.view.text_point(r, c)
                        self.view.sel().clear()
                        self.view.sel().add(sublime.Region(target))
                        self.view.show(target)

                        # Add the enter if needed
                        cursorPos = self.view.sel()[0].begin()
                        self.view.insert(edit, cursorPos, "\n")
                        return

        # Get end of cursor position
        cursorPos = self.view.sel()[0].end()
        
        for region in self.view.sel():
            
            # Get the line
            line = self.view.line(region) 

            # Add a newline inside the quote
            newline = '\\' + "n"
            self.view.insert(edit, cursorPos-1, newline)


            # Add the + and newline
            cursorPos = self.view.sel()[0].end()
            line_contents = ' ' + '+' + '\n'
            self.view.insert(edit, cursorPos, line_contents)


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

            # Insert the white space
            self.view.insert(edit, target, indent)

            # Insert the quotes
            if a:
                line_conts = '"' + '"'
                self.view.insert(edit, self.view.sel()[0].begin(), line_conts)
            if not a:
                line_conts = '\'' + '\''
                self.view.insert(edit, self.view.sel()[0].begin(), line_conts)                

            # Move cursor inside quotes
            (row,col) = self.view.rowcol(self.view.sel()[0].begin())
            target = self.view.text_point(row, col-1)
            self.view.sel().clear()
            self.view.sel().add(sublime.Region(target))
            self.view.show(target)



class MultiLineQuoteListener(sublime_plugin.EventListener):

    def on_text_command(self, view, command, args):
       
        # If enter is pressed
        print(args)
        if "insert" in command:
            if "{'characters': '\\n'}" in str(args):
                # Run multi_quote
                print("Running MultiQuote")
                view.run_command("multi_quote")
                # Remove the enter
                return("insert","\n")




