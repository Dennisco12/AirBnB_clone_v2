#!/usr/bin/python3
"""This creates and distributes an archive to my web servers"""

from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy

env.hosts = ['100.26.53.11', '18.204.10.149']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def deploy():
    """This calls the function do_pack and store the path of
    the created archive"""
    archive_path = do_pack()
    if archive_path is None:
        return False

    ret = do_deploy(archive_path)
    return ret
