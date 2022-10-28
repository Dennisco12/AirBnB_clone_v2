#!/usr/bin/python3
"""This generates a .tgz archive from the contents of the
web_static folder using the function do_pack"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """The prototype for the function"""
    current_date = datetime.now()
    current_date = current_date.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions/")
    filepath = 'versions/web_static_' + current_date + '.tgz'
    ret = local("tar -czvf {} web_static/".format(filepath))

    if ret.succeeded:
        return filepath
    else:
        return None
