import sys
import site

def add_site_dir(site_dirs):
    prev_sys_path = list(sys.path) 
    for directory in site_dirs:
        site.addsitedir(directory)
    new_sys_path = [] 
    for item in list(sys.path): 
        if item not in prev_sys_path: 
            new_sys_path.append(item) 
            sys.path.remove(item) 
    sys.path[:0] = new_sys_path 
