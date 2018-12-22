import socket

# 文件传输
def send_file_2_client(new_client_socket,client_addr)
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端（%s）需要下载文件是：%s" % (str(client_addr),file_name))

    file_content = None

    try:
        f = open(file_name,"rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print(没有要下载的文件（%s）% file_name)

    if file_content:
        new_client_socket.send(file_content)

def main():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    
    
    dest_ip = input("请输入ip")
    dest_port = int(input("请输入服务区port"))

    tcp_socket.connect((dest_ip,dest_port))

    download_file_name = input("请输入要下载的文件名字：")

    tcp_socket.send(download_file_name.encode("utf-8"))
    
    recv_data = tcp_socket.recv(1024)
    
    with open("[新]"+ download_file_name,"wb") as f:
        f.write(recv_data)
    tcp_socket.close()

if __name__ == "__main__":
    main()
