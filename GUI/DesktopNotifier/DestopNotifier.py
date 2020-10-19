import time
from plyer import notification

a = time.strftime('%H:%M:%S', time.localtime())

if a:
    print(a)

    n = notification

    n.notify(
        title = "Hello",
        message = "This is a notifier",
        timeout = 5
    )