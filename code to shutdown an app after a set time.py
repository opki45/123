import time
import subprocess


def shutdown_app():
    app_command = 'your_app.exe'

    try:
        subprocess.run(app_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error shutting down the app: {e}")


def countdown_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1


    shutdown_app()


countdown_timer(1)