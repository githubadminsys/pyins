def iinput(cue='',var=None,error=''):
  _input = input(str(cue))
  try:
    if var != None:
      var = int(_input)
      return int(_input)
    else:
      return int(_input)
  except TypeError:
    if error != '':
      return str(error)
    else:
      return "error"
print(iinput(cue='Input:'))
