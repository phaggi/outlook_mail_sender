import schedule
import time

'''
def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
'''


def set_every_5_sec(job):
    """
    set scheduler every 5 sec start job
    :param job:
    :return:
    """

    def wrapper():
        schedule.every(5).seconds.do(job)

    return wrapper

def set_at_time(times):
    """
    set scheduler every day at time at times start job
    :param times:
    :return:
    """
    def at_time(job):
        """
        :param job:
        :return:
        """
        def wrapper():
            for t in times:
                schedule.every().day.at(t).do(job)

        return wrapper
    return at_time

def start_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == '__main__':
    """
    @every_5_sec
    def check():
        print('Check test')
        return True
    check()
    """


    #print(check_mail())