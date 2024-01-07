"""
多线程编程的使用
"""
import time
import threading


def sing(msg):
    while True:
        print(msg + 'sing...')
        time.sleep(1)


def dance(msg):
    while True:
        print(msg + '...')
        time.sleep(1)


if __name__ == '__main__':
    # 创建sing线程
    sing_thread = threading.Thread(target=sing, args=('唱歌',))
    dance_tread = threading.Thread(target=dance, kwargs={'msg':'道家无上心法'})
    sing_thread.start()
    dance_tread.start()
