# 

# Overview

This project is a tools like top, htop, etc. command in linux. 
It finds the utilisation of the CPU, the memory and the power of a particular process.

This project is made in python 3.8.5.

This project is only made for linux (for the moment).

This project is made by : Faucher Simon

# Summary

* [Contents](#Contents)
  * [Sources files and folders](#Sources-files-and-folders)
      * [Sources files](#Sources-files)
      * [Sources folders](#Sources-folders)
* [Installation](#installation)
  * [Requirements](#Requirements)
  * [Run the project](#Run-the-project)

## Contents

### Sources files and folders

#### Sources files
* [main.py](./main.py) : Main file to run the project

#### Sources folders
* [Power](./Power) : Folder containing the power module
* [Memory](./Memory) : Folder containing the memory module
* [CPU](./CPU) : Folder containing the CPU module
* [Read_File](./Read_File) : Folder containing the read_file module
* [Arguments](./Arguments) : Folder containing the arguments module

## Installation

### Requirements
csv : `pip install csv`

threading : `pip install threading`

matplotlib : `pip install matplotlib`

time : `pip install time`

argparse : `pip install argparse`

### Run the project
For run this project you need to have sudo rights. They are needed for the power module, to access to the power of the process.

run the main.py file with the command `sudo python main.py [option]` in the terminal.

#### Options are :
* Help :
  * -h / --help :  Print help message and exit
  * -v / --verbose : Activates verbose mode
  
* Obligatory :
  * -p / --pid : PID of the process to be inspected

* Optionnal :
  * -cpu / -- cpu : Displays CPU usage
  * -mem / --memory : Displays memory usage
  * -pow / --power  : Displays power usage
  * -a / --all : Displays all usage
  * -f / --frequency :  Sampling frequency in seconds
  * -n / --number : Number of samples
  * -plot / --plot : Displays graphics
  * -s / --save : Write the data in files

