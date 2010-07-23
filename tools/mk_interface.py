#! /usr/bin/env python

#try:
import sys

header = sys.argv[1]
sol_name = header[header.rfind('/')+1:header.rfind('.')]
interface = open( './python/'+sol_name+'.i', 'w' )


interface.write('/* File: '+sol_name+'.i,'+' generated by mk_interface.py */\n')
interface.write('%module '+sol_name+' \n\n%{\n#include <'+sol_name+'.hpp>\n')

#declarations = '%}\n\n%include "carrays.i"\n%array_functions(MiniSatExpression*, VarArray);\n%array_functions(int, IntArray);\n'
declarations = '%}\n\n'
extern_keyword = False
for line in open(header):
    splitted = line.split()
    #print line,
    if len(splitted) > 0:
        #print splitted
        if extern_keyword == True:
            #print 'extern body'
            interface.write(line)
            if splitted[0] == '}':
                #print 'extern end'
                extern_keyword = False
        elif splitted[0] == '#include':
            #print 'include'
            interface.write(line)
        elif splitted[0] == 'extern':
            #print 'extern start'
            interface.write(line)
            extern_keyword = True
        elif splitted[0] == "//python":
            declarations += line[8:]
        elif splitted[0][0] != '#' :
            #print 'body'
            declarations += line
    else:
        #print 'nothing'
        declarations += line

interface.write(declarations)

interface.write('\n%template('+sol_name+'ExpArray) '+sol_name+'Array< '+sol_name+'_Expression* >;\n%template('+sol_name+'IntArray) '+sol_name+'Array< int >;\n%template('+sol_name+'DoubleArray) '+sol_name+'Array< double >;\n\n')

#except:
#    print 'abort'
#    pass
