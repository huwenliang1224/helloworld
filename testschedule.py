#!/usr/bin/python
# coding=utf-8

import schedule
import time
import threading

global i
i = 0


def job():
    global i
    i += 1
    print(i)

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
