# -*-coding:utf-8-*-

import os,glob
import os.path as path

def check_source():
    if path.exists('./widget_collection.csv'):
        return 0
    else:
        return gen_err('cannot find widget_collection.csv in current directory!')
    
def check_single(src,tar):
    if not path.isdir(tar):
        return gen_err('target directory not exist!')
    elif not path.isfile(src):
        return gen_err('file not exist!')
    elif src[-4:]!='.xml':
        return gen_err('not a xml file!')
    else:
        return 0
    
def check_project(src,tar):
    if not path.isdir(tar):
        return gen_err('target directory not exist!')
    elif not path.isdir(src):
        return gen_err('directory not exist!')
    else:
        files=glob.glob(src+'/*.xml')
        if not len(files):
            return gen_err('no xml files in the specified directory!')
        else:
            return 0
    
def gen_err(s):
    return 'error:'+s