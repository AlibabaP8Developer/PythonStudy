# 导入进程模块
import multiprocessing
import time


def coding():
    for i in range(3):
        print('coding')
        time.sleep(0.2)


def music():
    for i in range(3):
        print('music')
        time.sleep(0.2)


if __name__ == '__main__':
    # 通过进程类创建进程对象
    coding_process = multiprocessing.Process(target=coding)
    music_process = multiprocessing.Process(target=music)
    # 启动进程
    coding_process.start()
    music_process.start()
