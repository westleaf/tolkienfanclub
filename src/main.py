from textnode import *
import os
import shutil
from utils import copy_files
from generator import generate_page, generate_page_recursive
import sys

dir_static = "./static"
dir_public = "./docs"


if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"


def main():
    cleanup_public()
    copy_static_files()
    generate_page_recursive("content", "template.html", dir_public, basepath)


def cleanup_public():
    if os.path.exists(dir_public):
        shutil.rmtree(dir_public)
    os.makedirs(dir_public)
    os.makedirs(os.path.join(dir_public, "images"))
    os.makedirs(os.path.join(dir_public, "styles"))

def copy_static_files():
    copy_files(dir_static, dir_public)

if __name__ == "__main__":
    main()
