import webbrowser
import time


def breaks():
    """ Counts time between breaks, and opens a web page when time is up. The count variable counts the times that the browser has opened """
    print('This program started on ' + time.ctime())  # what time the breaks were taken
    time.sleep(60 * 60)   # counts 4 sec then opens the window, or (2 * 60 * 60) for 2 hours
    webbrowser.open('www.facebook.com')     # the webpage that it opens


breaks()


# ------------------------------THERE WAY---------------------------------------------------------------
# total_breaks = 3
# break_count = 0
# print('This program started on ' + time.ctime())
# while (break_count < total_breaks):
#     time.sleep(3)
#     webbrowser.open('http://www.youtube.com/wathc?v=dQw4w9WgXcQ')
#     break_count = break_count + 1
# ------------------------------------------------------------------------------------------------------
