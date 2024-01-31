#!/usr/bin/python3
"""
Write a Fabric script that creates and
distributes an archive to your web servers,
using the function deploy
"""

from fabric.api import run, put, env
from os.path import exists
from fabric import
import time


env.host = ['54.237.86.2', '52.86.58.243']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """
    function to for local operations
    """
    date_time = time.strftime("%Y%m%d%H%M%S")
    try:
        local('mkdir -p version')
        local('tar -cvzf ersion/web_static_{}.tgz web_static/'
              .format(date_time))
        return ('return "version/web_static_{}tgz'.format(date_time))
    except Exception as e:
        return None


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
        file = archive_path.split('/')[-1]
        file_split = file.split('.')[0]
        path = "/data/web_static/releases/"
        put('sudo mkdir -p {}{}/'.format(file, file_split))
        run('sudo tar -xzf /tmp/{} -C {}{}'.format(file, path, file_split))
        run('sudo rm /tmp/{}'.format(file))
        run('sudo mv {0}{1}/web_static/* {0}{1}'.format(path, file_split))
        run('sudo rm -rf {}{}web_static'.format(path, file_split))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'
            .format(path, file_split))
        return True
    except Exception as e:
        return False


def deploy():
    """
    function to create and distribute archive
    """
    try:
        creat_archive = do_pack()
        use_archive = do_deploy(creat_archive)
        return use_archive
    except Exception as e:
        return False
