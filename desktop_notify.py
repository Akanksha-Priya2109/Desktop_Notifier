from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title=" *** Take Rest ***",
            message="Taking rest helps us to prevent fatigue, improves focus, boosts productivity, and maintains overall health and well-being.",
            timeout=5)
        time.sleep(10)