def main(): 
    from crontab import CronTab
    cron = CronTab(user=True)
    job = cron.new(command = "python /Users/Ian/Documents/WebscraperFiles/tweetFortune.py")
    job.minute.every(1)
    cron.write()

if __name__ == '__main__':
    main()
    print("here")
