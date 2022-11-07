import os

# if(os.path.exists('file')):
#     pass
# else:
#     os.makedirs('file')
#os.rename('file','files')
#os.rmdir('files')

file = open('myfile.txt','a+')
file.write('adeolu')
print(file.fileno())
os. close(3)