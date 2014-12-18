'''This piece of code does the following steps:
    1. open an empty file with name "test_read_write" in the current directory.
    2. write in a few lines of plain text, close the file.
    3. reopen and print each line of the file in the terminal.
'''
infile_name='./test_read_write'
f=open(infile_name,'w')
f.write("hello world in the new file\n")
f.write("and another line\n")
f.close()

for line in open(infile_name,'r'):
    print line
f.close()