# essa funcao deve ser copiada para o seu codigo python
# para usa-la, use comando read_params(params) no iniitialize

def read_params(a,j=''):
  if j=='':
    print "### Printing GUI parameters ###"
  for i in a:
    if (type(a[i])!=type({'a':1})):
      print j+"['"+str(i)+"']="+str(a[i])+" type: "+str(type(a[i]))
    else:
      read_params(a[i],j+"['"+str(i)+"']")



