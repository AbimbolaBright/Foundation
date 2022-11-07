# try:
#   fille=open('python.text', 'w')
#   fille.write('hello python class 2 for morning')
#   fille.close()
# finally:
#     fille.close()  
# with open('python. text','a') as file:
#     file.write('\n I love myself')
#     file. writelines('this is a new line')
#     file.writelines('this is another new line')


# with open ('docs/newText.doc','a')as file:
#     rs=file.writelines('Ado-ekiti is my city')
# f= open('muitiplication.text', 'w')
# for  i in range(1,10):
#     for j in range(1,10):
#         print(*(f'{i}x {j} = {i*j}'),file=f, end='\t')
 


# import os

# os.rename('python.text','glimpse.text')
import os


# os.mkdir('c:/johnson.text')

# print(os.listdir('c:'))


# os.mkdir('c:/Users/Public/Desktop/ newFolders')


# rs =os.listdir('c:')
# for x in rs:
#     print(x)

# os .mkdir('c:/users/public/Destop/new Folder')
os .makedirs('new folder')
with open('python/new.txt', 'w')as file:
    file.write('something')