import os

dir_list = os.listdir('./')

for i in dir_list:
    if i[-4:] == '.png' or i[-4:] == '.jpg':
        print(i)
        print(os.popen(f'''file ./{i}'''))
        os.popen(f'''mv ./{i} ./{i[:-4]}.avif''')
