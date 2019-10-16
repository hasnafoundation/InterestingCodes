import os
from datetime import datetime

def os_name():
    print(os.uname())

def loggin_user():
    print(os.getlogin()
    
def current_path():
    print(os.getcwd())

def dir_list():
    print(os.listdir())
          
def current_dir_info():
    print(os.stat('.'))
          
def change_dir(path):
    os.chdir(path)
    print(os.getcwd())
          
def last_modifition_time(path):
    print(datetime.fromtimestamp(os.path.getmtime(path))
        
def find_file_byExtension(keyWoard, extension):
          print(glob.glob(f"[{keyWord}]{extension})")
        
          