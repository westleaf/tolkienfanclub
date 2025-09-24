from textnode import *
import os
import shutil
from utils import copy_files
from generator import generate_page

dir_static = "./static"
dir_public = "./public"

def main():
    cleanup_public()
    copy_static_files()
    generate_page("content/index.md", "template.html", os.path.join(dir_public, "index.html"))


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
