from fabric import Connection

send_list = [["xxx.xxx.xxx.xxx", 7001, "user", "pwd"]]
for the_send in send_list:
    print(str(the_send) + " start====")
    try:
        connect = Connection(the_send[0], the_send[2], the_send[1], connect_kwargs={"password": the_send[3]})
        connect.run(f"supervisorctl -u {the_send[2]} -p {the_send[3]} status")
        connect.close()
    except:
        print(str(the_send) + " link err")
