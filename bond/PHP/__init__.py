from bond import *
import os
import shlex
import warnings

def PHP(cmd=None, args=None, xargs='', cwd=None, env=os.environ,
        trans_except=False, protocol=None, compat=None, timeout=60, logfile=None):
    warnings.warn("Language constructors are deprecated."
                  " Please use ``bond.make_bond()`` directly.",
                  DeprecationWarning)

    if args is not None: args = shlex.split(args)
    if xargs is not None: xargs = shlex.split(xargs)
    return bond('PHP', cmd, args, xargs, cwd=cwd, env=env,
                trans_except=trans_except, timeout=timeout, logfile=logfile)
