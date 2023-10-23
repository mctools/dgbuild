
def main( prevent_env_setup_msg = False ):
    import sys
    if any( e.startswith('--env-') for e in sys.argv[1:] ):
        #Special short-circuit to efficiently enable standard --env-setup usage:
        if '--env-u' in sys.argv[1:]:
            #Enable --env-u[nsetup] usage, even outside a dgbuild project:
            from .envsetup import emit_envunsetup
            emit_envunsetup()
            raise SystemExit
        if '--env-s' in sys.argv[1:]:
            #Short-circuit to efficiently enable --env-setup call:
            from .envsetup import emit_envsetup
            emit_envsetup()
            raise SystemExit
    from . import frontend
    frontend.dgbuild_main( prevent_env_setup_msg = prevent_env_setup_msg )

def unwrapped_main():
    #For the unwrapped_dgbuild entry point, presumably only called from a bash
    #function taking care of the --env-setup.
    import sys
    sys.argv[0] = 'dgbuild2'#FIXME: after migration put to 'dgbuild'!
    main( prevent_env_setup_msg = True )

def dgenv_main():
    import sys
    args = sys.argv[1:]
    if not args:
        print("""Usage:

dgenv <program> [args]

Runs <program> within the dgbuild runtime environment. Note that if you wish to
make sure the codebase has been built first (with dgbuild) you should use dgrun
rather than dgenv.
""")
        sys.exit(1)
        return
    from .envsetup import create_install_env_clone
    run_env = create_install_env_clone()
    from . import utils
    import shlex
    cmd = ' '.join(shlex.quote(e) for e in args)
    utils.system(cmd,env=run_env)

def dgrun_main():
    import sys
    args = sys.argv[1:]
    if not args:
        print("""Usage:

dgrun <program> [args]

Runs dgbuild (quietly) and if it finishes successfully, then proceeds to launch
<program> within the dgbuild runtime environment.
""")
        sys.exit(1)
        return
    from .envsetup import create_install_env_clone
    run_env = create_install_env_clone()
    from . import utils
    import shlex
    cmd = ' '.join(shlex.quote(e) for e in args)
    from . import frontend
    frontend.dgbuild_main( argv = ['dgbuild2',#FIXME: after migration put to 'dgbuild'!
                                   '--quiet'],
                           prevent_env_setup_msg = True )
    utils.system(cmd,env=run_env)

if __name__=='__main__':
    main()
