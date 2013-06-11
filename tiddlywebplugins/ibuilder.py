"""
A collection of tools and functions for building tiddlywebplugins
packages come with pre-determined tiddlers, bags and recipes.

Use tiddlywebplugins.pkgstore to keep those entities in the
target package.
"""

from tiddlyweb.model.bag import Bag
from tiddlyweb.store import Store
from tiddlyweb.util import std_error_message
from tiddlywebplugins.twimport import recipe_to_urls, url_to_tiddler


__version__ = '0.1.3'


def cacher(args):
    """
    Called from the twibuilder command line tool to "cache"
    tiddler information into the local store.
    """
    package_name = args[0]
    cache_tiddlers(package_name)


def cache_tiddlers(package_name):
    """
    Stores instance tiddlers in the package.

    reads store_contents from <package>.instance

    tiddler files are stored in <package>/resources/store
    """
    instance_module = __import__("%s.instance" % package_name, None, None,
        ["instance"])
    store_contents = instance_module.store_contents

    target_store = Store('tiddlywebplugins.pkgstore',
            {'package': package_name, 'read_only': False}, {})

    sources = {}
    for bag, uris in store_contents.items():
        sources[bag] = []
        for uri in uris:
            if uri.endswith(".recipe"):
                urls = recipe_to_urls(uri)
                sources[bag].extend(urls)
            else:
                sources[bag].append(uri)

    for bag_name, uris in sources.items():
        bag = Bag(bag_name)
        target_store.put(bag)

        for uri in uris:
            std_error_message("retrieving %s" % uri)
            tiddler = url_to_tiddler(uri)
            tiddler.bag = bag.name
            target_store.put(tiddler)
