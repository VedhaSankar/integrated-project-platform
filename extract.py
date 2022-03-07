from zipfile import ZipFile 
  
file_name = "uploads/main_branch.zip"

def extract_zip(file_name):
    with ZipFile(file_name, 'r') as zip:
        zip.extractall('uploads')


def main():

    extract_zip(file_name)

    
if __name__ == '__main__':
    main

