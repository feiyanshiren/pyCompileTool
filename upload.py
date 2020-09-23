import os

import paramiko

send_list = [[("xxx.xxx.xxx.xxx", 7000), "user", "pwd"]]

local_path = "./dist_update"
remove_path = "/home/xxx/xxx/"

os.chdir(local_path)

for the_send in send_list:

    try:
        print(str(the_send) + " start===")
        transport = paramiko.Transport(the_send[0])
        transport.connect(username=the_send[1], password=the_send[2])

        sftp = paramiko.SFTPClient.from_transport(transport)

        all_list = ["."]
        the_list = []
        for the_dir in os.listdir():
            if os.path.isdir(the_dir):
                the_list.append(the_dir)

        while len(the_list) != 0:
            the_dir = the_list.pop()
            for li in os.listdir(the_dir):
                if os.path.isdir(the_dir + os.sep + li):
                    the_list.append(the_dir + os.sep + li)
            all_list.append(the_dir)

        for the_path in all_list:
            try:
                for f in os.listdir(the_path):
                    if f.endswith(".pyc"):
                        sftp.put(the_path + "/" + f, remove_path + the_path + "/" + f)
                        print(the_path + "/" + f)
            except Exception as e:
                print('upload exception:', e)

        transport.close()
        print(str(the_send) + " end")
    except:
        print(str(the_send) + " link err")
