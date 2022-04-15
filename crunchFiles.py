import os, re
# This script will remove duplicates files and the UTC timestamp from Windows backups.
# It deletes files, so use at your own risk!!! Test a small directory first. 

prevFilename = ""
count = 0
fileSet = []

def stip(fileList):
       # loop through list delete all but last item
       # rename last file
       index=0
       for x in fileList:
           index +=1
           if index == len(fileList):
               fromFile = x.get("path") + "/" + x.get("fullFilename")
               toFile = x.get("path") + "/" + x.get("baseFilename") + x.get("extension")
               altFile = x.get("path") + "/" + x.get("baseFilename") + "(1)" + x.get("extension")
               try:
                 os.rename(fromFile, toFile)
               except:
                 os.rename(fromFile, altFile)
           else:
               delFile = x.get("path") + "/" + x.get("fullFilename")
               os.remove(delFile)

print("\n\nThis program deletes files! Use at your own risk. Test first! \n")
STARTDIR = input ("Enter the full path of the starting directory (use forward slashes): ")
isdir = os.path.isdir(STARTDIR)
if not isdir:
    print("That directory does not exist!!!!")
    quit() 
# assumes files are sorted by name
for root, dirs, files in os.walk(STARTDIR, topdown=False):
   files.sort()
   for name in files:
      count +=1
      # regular expression to break up parts of the file name.
      what = re.search(r"(.*?)(\(\d{4}\_\d{2}_\d{2}\s\d{2}\_\d{2}\_\d{2}\sutc\))(\..*)", name, re.I)
      if what != None:
        filename = what.group(1).strip()
        utcDate = what.group(2).strip()
        extension = what.group(3).strip()
        if prevFilename != filename:
            if count > 1:
              if fileSet:
                 stip(fileSet)        
                 fileSet = []
            prevFilename = filename
        fileSet.append({'path': root, 'fullFilename': name, 'baseFilename': filename, 'extension': extension})

   # handle last series
   if fileSet:
       stip(fileSet)        
       fileSet = []

   count=0