def chk_prop_name(grid,testname):
    lst_props_grid=sgems.get_property_list(grid)
    if (testname in lst_props_grid):
      flag=0
      i=1
      while (flag==0):
        test_new_name=testname+'-'+str(i)
        if (test_new_name not in lst_props_grid):
          flag=1
          testname=test_new_name
      i=i+1
    return testname
