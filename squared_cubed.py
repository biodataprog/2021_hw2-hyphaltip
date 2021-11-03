#!/usr/bin/env python3

# you can change this for experimentation
MaxNum = 100

# this will print a header
print("\t".join(["N","Squared","Cubed"]))

print(n,n**2,n**3,sep="\t")

for n in range(MaxNum):
    print("\t".join([str(n),str(n**2),str(n**3)]))

print("\n")
#print("\t".join(["N","Squared","Cubed"]))
#for n in range(MaxNum):
#    print("\t".join([str(n),"%e"%(n**2),"%g"%(n**3)]))

print("\n")
print("{}\t{}\t{}".format("N","Squared","Cubed"))
for n in range(MaxNum):
    print("{}\t{}\t{}".format(n,n**2,n**3,"notes"))
#    print("%d\t%d\t%g".format(n,n**2,n**3))
#    print("\t".join([str(n),"%e"%(n**2),"%g"%(n**3)]))
import csv
import sys
csvwriter = csv.writer(sys.stdout, delimiter=',',quoting=csv.QUOTE_MINIMAL)

csvwriter.writerow(["N","Squared","Cubed"])
for n in range(MaxNum):
    row = [n,n**2,n**3,"extra notes"]
    if n > 3:
        row.append("more notes")
    csvwriter.writerow(row)

# write your code below you can use
# range(MaxNum)
# as a way to get numbers from 0...MaxNum
# eg
# for n in range(MaxNum):
#    # code here
# to convert a number into strings
# numstring = str(number)
# or
# numstring = "%d"%(number)
# if you wanted to show scientific notation when num get very large
# numstring = "%g"%(number)
