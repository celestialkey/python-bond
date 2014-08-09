### python-bond Python interface loader
### NOTE: use ### for comments *only*, as this code is reduced as much as
###       possible to be injected into the interpreter *without parsing*.

def __PY_BOND_stage1():
    import sys, tty

    if sys.stdin.isatty():
        tty.setraw(sys.stdin)
    sys.stdout.write("STAGE2\n")

    line = sys.stdin.readline().rstrip()
    stage2 = eval(line)
    exec(stage2['code'], globals())
    eval(stage2['func'], globals())(*stage2['args'])

__PY_BOND_stage1()
