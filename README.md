# crunchFiles.py

The Windows File History feature is very useful, especially if you want to revert a file to a previous version. This feature is built into Windows File Explorer. However, there are some cases where you might need to restore the entire backup to a new computer. In that case File Explorer may not help.  
If you have a Windows File History backup, but need to restore the directories and files to a new computer use this script.  

* Install Python
* Copy the crunchFiles.py to your computer in for example, c:\temp\crunchFiles.py. 
* Then change directories to c:\temp and run the program. 

```
> cd \temp
> python crunchFiles.py
```

You will be prompted for the full path to the root directory that you want to consolidate. 
For example, you might have a directory with UTC timestamps on them and you only want the latest file but also with timestamps stripped off.

```
leaf (2022_01_12 01_06_30 UTC).svg
leaf (2022_01_12 15_11_41 UTC).svg
leaf (2022_01_12 16_11_50 UTC).svg
leaf (2022_01_12 20_15_11 UTC).svg
```
You would end up with: 
```
leaf.svg
```
This script deletes and renames files, so use at your own risk. Test first on a backup. 

