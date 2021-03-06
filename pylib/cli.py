'''一些在命令行上使用的便捷函数'''

import os
from lilypath import path

def findbroken(p):
  '''递归寻找断掉的软链接'''
  ret = []

  for i in p.list():
    if i.isdir():
      ret.extend(findbroken(i))
    elif not i.exists():
      ret.append(i)

  return ret

def repl(local, histfile=None, banner=None):
  import readline
  import rlcompleter
  readline.parse_and_bind('tab: complete')
  if histfile is not None and os.path.exists(histfile):
    # avoid duplicate reading
    readline.clear_history()
    readline.set_history_length(10000)
    readline.read_history_file(histfile)
  import code
  readline.set_completer(rlcompleter.Completer(local).complete)
  code.interact(local=local, banner=banner)
  if histfile is not None:
    readline.write_history_file(histfile)

