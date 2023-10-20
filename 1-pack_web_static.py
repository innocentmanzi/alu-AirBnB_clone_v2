#!/usr/bin/python3
"""
<<<<<<< HEAD
Fabric script to genereate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *
=======
    script that generates '.tgz' archive from the contents of the 'web_static'
"""
from fabric.api import local
from datetime import datetime
>>>>>>> e6467fa06798e2dc91f6db07d6418a553b4dd644


def do_pack():
    """
<<<<<<< HEAD
    making an archive on web_static folder
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
=======
        function to compress directory into .tgz archive
        Return: Success - '.tgz' archive path
                Failure - None
    """
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + now + '.tgz'

    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(archive_path))

    if result.succeeded:
        return archive_path
    return None
>>>>>>> e6467fa06798e2dc91f6db07d6418a553b4dd644
