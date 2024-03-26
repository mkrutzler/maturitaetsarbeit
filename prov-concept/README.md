# Usage of the Demo

All of the building and running is handeled by make. A Cross-Compiler is an absolute neccesity and without it the build won't work.
To run the programm you will need qemu. 

## Concept:

The PDF Document is under "docs";.

## Make Usage

The Options are:

-   make
    This will run "setup, iso, run"
-   make setup
    This will run c"lean "and than create the necessary build directories
-   make clean
    This deletes the build directory.
-   make iso
    This will run b"uild." After that is finished it creates the iso file
-   make build
    This will run o"bjs." Thank it will link the ."o "files and it tests if the build is multiboot compatible.
-   make objs
    This will create all the .o files
-   make run
    This will run the os.iso with qemu
-   make usb-write
    CAREFUL: This writes the iso to /dev/sdb => IT WILL ERASE EVERYTHING ON /dev/sdb. This requires sudo.

