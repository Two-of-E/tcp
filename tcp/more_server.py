import socket

def main():
    # 1.买个手机，监听套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.插入手机卡
    tcp_server_socket.bind(("",7890))
    # 3.将手机设置为正常的响铃模式（让默认的套接字由主动变被动）
    tcp_server_socket.listen(128)

    while True:
        print("等待新的客户端到来")

        # 4.等待别人的的电话到来,新的套接字为顾客服务
        new_client_socket,client_addr = tcp_server_socket.accept()
        print("一个新的用户已经到来%s" % str(client_addr))
        
        while True:
            # 接受客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            print("客户端宋过来的请求是：%s" % recv_data.decode("utf-8"))
            # 如果recv解堵塞
            if recv_data:
                new_client_socket.send("hahaha".encode("utf-8"))
            else:
                break

        #关闭套接字
        new_client_socket.close()
        print("已经服务完毕")
    tcp_server_socket.close()


   

if __name__ == "__main__":
    main()
