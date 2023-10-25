
def dgbuild_bundle_list():
    import pathlib
    datadir = ( pathlib.Path(__file__).absolute().parent / 'data' ).absolute().resolve()
    return [ datadir / 'pkgs' / 'dgbuild.cfg', datadir / 'pkgs_val' / 'dgbuild.cfg' ]
