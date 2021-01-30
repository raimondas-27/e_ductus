import builtins
import inspect
import sys
from itertools import chain
from itertools import islice
from typing import Iterator
import pprintpp
from pygments import highlight
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.python import PythonLexer


def formatter():
    return Terminal256Formatter(style='vim')


def pp(obj):
    if isinstance(obj, Iterator):
        out = list(islice(obj, 10))
        out = '<generator> ' + pprintpp.pformat(out)
        obj = chain(out, obj)
    else:
        out = pprintpp.pformat(obj)
    frame = inspect.currentframe()
    frame = inspect.getouterframes(frame)[1]
    line = inspect.getframeinfo(frame[0]).code_context[0].strip()
    if line.endswith(')'):
        arg = line[line.find('(') + 1:-1]
        out = f'{arg} = {out}'
    out = highlight(out, PythonLexer(), formatter())
    print()
    print(out, file=sys.__stderr__)
    return obj


builtins.pp = pp
