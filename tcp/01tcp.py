# udp稳定性不好，tcp对包有检查建立通道 建立连接 上传流量以部分是上传的应答
# 这之中还包括超时重传，错误校验，流量控制和阻塞管理。文件分块传输
import socket

def main():
    # 1.创建tcp的套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.链接服务器
    # tcp_socket.connect(("192.168.17.12"，6666))
    server_ip = input("请输入要连接的服务器的ip：")
    server_port = int(input("请输入要连接的服务器的port："))
    
    server_addr = (server_ip,server_port)
    tcp_socket.connect(server_addr)
    
    # 3.发送数据/接受数据
    send_data = input("请输入要发送的数据：")
    tcp_socket.send(send_data.encode("utf-8"))
    # 4.关闭套接zi
    tcp_socket.close()

if __name__ == "__main__":
    main()
