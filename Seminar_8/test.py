import os

dir_inp = 'E:\GB\Python\Seminar\Seminar_8'

def get_info(dir):
    data: list = []
    for i in os.listdir(dir):
        path = dir + '\\' + i
        if os.path.isfile(path):
            data.append({'name':i, 'type':'file', 'size':os.path.getsize(path),
                         'files':None, 'parent':path.split('\\')[-2]})
        if os.path.isdir(path):
            data.append({'name':i, 'type':'folder', 'size':None,
                         'files':len(os.listdir(path)), 'parent':None})
            get_info(path)
    print(data)

get_info(dir_inp)        