#!/usr/bin/python3
"""
Write a Fabric script that
generates a .tgz archive
"""

from fabric.api import local
import time


def do_pack():
    """
    generates a .tgz archive from the
    contents of the web_static folder
    """

    date_time = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf version/web_static_{}.tgz web_static/"
              .format(date_time))
        return "version/web_static_{}tgz".format(date_time)

    except Exception as e:
        return None
