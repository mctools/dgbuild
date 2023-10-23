
import pathlib
def dgbuild_bundle_name():
    return 'g4framework'

def dgbuild_bundle_pkgroot():
    return ( pathlib.Path(__file__).parent / 'data' / 'pkgs' ).absolute().resolve()

def dgbuild_bundle_envpaths():
    return [ 'NCRYSTAL_DATA_PATH:<install>/data' ]
