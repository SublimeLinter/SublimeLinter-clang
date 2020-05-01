SublimeLinter-clang
=========================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter3) provides an interface to [clang](http://clang.llvm.org/).
It will be used with files that have the C/C Improved/C++ syntax.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, ensure that `clang` is installed on your system.
- Mac OS X: clang should be already bundled.
- Linux: clang can be easily installed using most package managers.
- Windows: the situation is a little trickier, especially with C++. One way to go is to install [mingw with clang](http://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/rubenvb/). Both gcc and clang packages should be installed into the same directory.

Once `clang` is installed, ensure it is in your system PATH so that SublimeLinter can find it.
The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable)

## Settings

We have two settings sections. 'clang' for c files, and 'clang++' to configure the linter for c++ files. E.g.

```
{
    "linters":
    {
        "clang": {
            "args": "-fvery-important",
            "I": [
                "${folder}/3rdparty/bar/include",
                "${folder}/3rdparty/baz"
            ]
        },
        "clang++": {
            "args": "-falso-important"
        }
    }
},
```

Note: 'args' has the default value '-Wall -fsyntax-only -fno-caret-diagnostics', so make sure to include them when overriding 'args'.

All common settings information can be found here:

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html

Additional settings for SublimeLinter-clang:

|Setting|Description|
|:------|:----------|
|I|A list of directories to be added to the header search paths.|
|isystem|A list of directories to be added to the system header search paths.|
|x|Automatically set depending on the file type.|

SublimeLinter allows [expansion variables](http://sublimelinter.readthedocs.io/en/latest/settings.html#settings-expansion). For example, '${folder}' can be used to specify a path relative to the project folder.

## Troubleshooting
C/C++ linting is not always straightforward. A few things to try when there's (almost) no linting information available:
- Try to compile from the command line, and verify it works.
- The linter might be missing some header files. They can be added with "include_dirs".
- Sometimes clang fails to locate the C++ standard library headers.
Assuming the compilation works when executed via command line, try to compile with `clang++ -v`.
This will display all of the hidden flags clang uses. As a last resort, they can all be added as "args".

