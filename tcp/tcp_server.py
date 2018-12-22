import socket


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
