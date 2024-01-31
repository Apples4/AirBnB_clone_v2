#!/usr/bin/python3
"""
Write a Fabric script
that distributes an archive to your web servers
"""

from fabric.api import run, put, env
from os.path import exists


def do_deploy(archive_path):
    """
    Write a Fabric script
    (based on the file 1-pack_web_static.py)

    params:
    archive_path - file path
    """
    if exists(archive_path) is False:
        return False
    try:
        file = archive_path.split("/")[-1]
        file_split = file.split(".")[0]
        path = "/data/web_static/releases/"
        put('mkdir -p {}{}/'.format(file, file_split))
        run('tar -xzf /tmp/{} -C {}{}'.format(file, path, file_split))
        run('rm /tmp/{}'.format(file))
        run('mv {0}{1}/web_static/* {0}{1}'.format(path, file_split))
        run('rm -rf {}{}web_static'.format(path, file_split))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, file_split))
        return True
    except Exception as e:
        return False
