#!/usr/bin/python3
"""This creates and distributes an archive to my web servers"""

from fabric.api import *
from os import path
from datetime import datetime

env.hosts = ['100.26.53.11', '18.204.10.149']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


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


def do_deploy(archive_path):
    """This distributes an archive to my web servers using the function
    do_deploy"""
    if not (path.exists(archive_path)):
        return False

    try:
        # upload archive to /tmp/ directory of server
        put(archive_path, "/tmp/")

        # create the target directory
        run('sudo mkdir -p /data/web_static/releases/web_static_{}/'
            .format(filename))

        # uncompress the archive file to the directory
        filename = archive_path.split('/')
        filename = filename[-1]
        filename = filename.split('.')[0]

        run("sudo tar -xvf {} -C /data/web_static/releases/{}"
            .format(filename, filename))

        # Delete the archive from the web
        run("sudo rm /tmp/web_static_{}.tgz".format(filename))

        # delete the symbolic link from the web server
        run("sudo rm -rf /data/web_static/current")

        # Create a new symbolic link to the new version of my code
        run("sudo ln -s /data/web_static/releases/web_static_{}\
            /data/web_static/current".format(filename))
        return True
    except Exception:
        return False


def deploy():
    """This calls the function do_pack and store the path of
    the created archive"""
    archive_path = do_pack()
    if archive_path is None:
        return False

    ret = do_deploy(archive_path)
    return ret
