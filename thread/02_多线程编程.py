"""
多线程编程的使用
"""
import time
import threading

def sing():
    while True:
        print('sing...')
        time.sleep(1)

def dance():
    while True:
        print('dance...')
        time.sleep(1)

if __name__ == '__main__':
    # 创建sing线程
    sing_thread = threading.Thread(target=sing)
    dance_tread = threading.Thread(target=dance)
    sing_thread.start()
    dance_tread.start()
