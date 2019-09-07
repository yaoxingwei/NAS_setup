# author : yaoxingwei@gmail.com
# date : 2019/09/07
# description: use to auto update aria2 trackers
#
import os
import tempfile

conf_file = 'aria2_yxw.conf'
folder_path = '/home/yxw/github/trackerslist'
trackfile = 'trackers_best.txt'
full_path = folder_path + '/' + trackfile

# check if the trackers file exist
def find_file():
    if os.path.exists(folder_path):
        if os.path.exists(full_path):
            print("find %s at %s" %(trackfile, folder_path))
            return 0
        else:
            print("can't find %s at %s" %(trackfile, folder_path))
    else:
        print("can't find path %s" %folder_path)
    return -1

# format trackers file to aria2 config format
def format_file(rfile, wfile):
    lines = rfile.readlines()
    for line in lines:
        if line == '\n':
            continue
        wfile.write(line.replace('\n', ';'))

    # add bt-tracker header
    wfile.seek(0, 0)
    data = wfile.read()
    wfile.seek(0, 0)
    wfile.write('bt-tracker=' + data)

    # remove the laster ';' char
    wfile.seek(-1, os.SEEK_END)
    wfile.truncate()

def adjust_conf_file(wfile):
    with open(conf_file, 'r') as r_cf:
        lines = r_cf.readlines()
    with open(conf_file, 'w') as w_cf:
        for line in lines:
            if 'bt-tracker' in line:
                continue
            w_cf.write(line)
        w_cf.write(wfile.read())

def main():
    result = find_file()
    if result:
        print('find file error!')
        return -1

    with open(full_path, 'r') as rf:
        with tempfile.TemporaryFile('w+t') as tempf:
            format_file(rf, tempf)
            tempf.seek(0)
            adjust_conf_file(tempf)


if __name__ == '__main__':
    main()
