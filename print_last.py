
## Script to print last column of a file in terminal.
#dt .09.02.2023.
# python3 print.last.py filename
#additional parameters:
# -o : Output file name
# --sorted : Sorted values (True/False)
############################################################

# Terminal script for running this code.
# python3 print_last.py filename.tsv   --sorted True
#or
#python3 print_last.py filename.tsv -o output_file --sorted True


###########################################################

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
parser.add_argument("-o","--outputfile",default="result")
parser.add_argument("--sorted",default="False")
args = parser.parse_args()

# check for the input file type.

def the_type_filder(args):
    if args.inputfile.endswith(".csv"):
        filetype = ","
    elif args.inputfile.endswith(".tsv") or  (args.inputfile.endswith(".txt")):
        filetype = '\t'
    else:
        filetype = ","
    return filetype

# separated the last column and remove the header.
def lastcal(file_path):
    with open(file_path,'r') as f:
        file = f.read()
    op = []
    for i in file.split("\n"):
        values = i.split(the_type_filder(args))
        target_value = values[-1]
        try:
            op.append(eval(target_value))
        except:
            pass
    return(op)

 
 # sorted the file. 
 # print the last column.  
   
def result_writing(op,args):
    if args.sorted == "True":
        op = sorted(op)
    else:
        pass
    if (args.outputfile != "result"):
        with open(f"{args.outputfile}.txt",'w') as k:
            for i in op:
                    k.write(f"{i}\n")
                    print(i)
    else:
        for i in op:
            print(i)
op = lastcal(args.inputfile)
result_writing(op,args)
