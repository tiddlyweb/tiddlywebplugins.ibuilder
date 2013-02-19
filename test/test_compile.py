


def test_compile():
    try:
        import tiddlywebplugins.ibuilder
        assert True
    except ImportError, exc:
        assert False, exc
