#By: Dae Kim
import random

a=[]
count = 0

#Check how many people are in the list by counting 'new line'
thefile = open("ppl_list.txt", 'r')
while 1:
    buffer = thefile.read(8192*1024)
    if not buffer: break
    count += buffer.count('\n')
thefile.close()

#open files to read and write to
# if you want to save each week's ride list change the name of the wfile
# example: change "ride_list.txt" to "thefilenameyouwant.txt"
# don't forget to add '.txt' to the file name
#dfile = open("driv_list.txt","r")
rfile = open("ppl_list.txt","r")
wfile = open("ride_list.txt", "w")
#dwfile = open("drv_assign","w")

#add all the lines in the read file to array a
for i in range (count):
    line = rfile.readline()
    a.append (line)

#randomize the order of the names in the array
random.shuffle(a)

#just for readability 
wfile.write ("Car 1:")
wfile.write("\n")

#start writing each name into wfile from 1 to the length of list
for n in range (1, count):
    n_4 = str(int((n/4)+1))
    wfile.write (a[n])

#every 4 people skip a line and write car and number of car
    if ((n != 0) and (n%4 == 0)):
        wfile.write ("\n")
        wfile.write ("Car ")
        wfile.write (n_4)
        wfile.write (":")
        wfile.write("\n")
#write the first person last
wfile.write(a[0])

#checking to see if all the names are in the array
#for n in range (count):
#print (a[n])

#close the files
rfile.close()
wfile.close()
#dfile.close()
#dwfile.close()

    


