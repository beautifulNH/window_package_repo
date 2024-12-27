import os

dir_list = os.listdir('./')

for i in dir_list:
    if '.avif' in i or '.png' in i or '.jpg' in i:
        print(i)
        this_type = os.popen(f'''file ./{i}''').read()
        if 'AVIF' in this_type:
            os.popen(f'''mv ./{i} ./{i[:-4]}.avif''')
        elif 'PNG' in this_type:
            os.popen(f'''mv ./{i} ./{i[:-4]}.png''')
        elif 'JPEG' in this_type:
            os.popen(f'''mv ./{i} ./{i[:-4]}.jpg''')
        else:
            os.popen(f'''mv ./{i} ./{i[:-4]}.none''')
