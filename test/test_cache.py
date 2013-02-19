
from tiddlywebplugins.ibuilder import cache_tiddlers

import os
import shutil

def setup_module(module):
    try:
        shutil.rmtree('testpackage/resources')
    except:
        pass

def test_cache():
    cache_tiddlers('testpackage')

    assert os.path.exists('testpackage/resources/store')
    assert os.path.exists('testpackage/resources/store/bags/bagone/tiddlers/')



