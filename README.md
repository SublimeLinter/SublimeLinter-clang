SublimeLinter-clang
=========================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter3) provides an interface to [clang](http://clang.llvm.org/). It will be used with files that have the C/C Improved/C++ syntax.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, you must ensure that `clang` is installed on your system.

- Mac OS X: clang should be already bundled.
- Linux: clang can be easily installed using most package managers.
- Windows: the situation is a little trickier, especially with C++. One way to go is to install [mingw with clang](http://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/rubenvb/). Both gcc and clang packages should be installed into the same directory.

Once `clang` is installed, you must ensure it is in your system PATH so that SublimeLinter can find it. The docs cover [troubleshooting PATH configuration](http://sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable)

## Settings
- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html

Additional SublimeLinter-clang settings:

|Setting|Description|
|:------|:----------|
|include_dirs|A list of directories to be added to the header search paths (-I is not needed).|
|extra_flags|A string with extra flags to pass to clang. These should be used carefully, as they may cause linting to fail.|

In project-specific settings, '$project_folder' or '${project_folder}' can be used to specify relative path.
```
"SublimeLinter":
{
    "linters":
    {
        "clang": {
            "extra_flags": "-Wall -I${project_folder}/foo",
            "include_dirs": [
                "${project_folder}/3rdparty/bar/include",
                "${project_folder}/3rdparty/baz"
            ]
        }
    }
},
```

## Troubleshooting
C/C++ linting is not always straightforward. A few things to try when there's (almost) no linting information available:
- Try to compile from the command line, and verify it works.
- The linter might be missing some header files. They can be added with "include_dirs".
- Sometimes clang fails to locate the C++ standard library headers.
Assuming the compilation works when executed via command line, try to compile with `clang++ -v`.
This will display all of the hidden flags clang uses. As a last resort, they can all be added as "extra_flags".

