from zipfile import ZipFile
  
file_name = "uploads/main_branch.zip"

with ZipFile(file_name, 'r') as zip:
    zip.printdir()

    print('Extracting all the files now...')
    a = zip.extractall()
    print(a)

