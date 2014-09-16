MultiLineEdit
============
-----------

MultiLineEdit is a plugin for Sublime Text 3 which adds multi-line quote functionality to Sublime, much like that found in Android Studio.


###Support###

The Plugin supports single and double quotes.
The plugin will keep inside functions (see examples).

###Installation###


Go to your Sublime Text 3 Packages directory and clone the repository using the command below:

```
git clone git@github.com:Shazib/MultiLineQuotes.git
```

Don't forget to regularly check for updates.
 

###Examples###

**Example 1**

```sh
// With the cursor inside the quote (shown by | )
String myString = "Hello this is my string|"
// Press: Ctrl + Q
// Result is:
String myString = "Hello this is my String" +
"|"

```

**Example 2**

Works inside functions etc too

```sh
// With the cursor inside the quote
myButton.setText("This is a lot of text |");
// Press Ctrl + Q
// Result is:
myButton.setText("This is a lot of text " +
"|");
```

###Version Log###

- **1.0.0**  _16th September 2014_
 - First Release
- **1.0.1** _16th September 2014_
 - Single Quote Support
 
