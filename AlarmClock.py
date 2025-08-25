import time
import datetime
import pygame


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "Data/Alarm.mp3"
    is_running = True

    while is_running: #The program keeps checking time every second in this loop.
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP! 😴")

            pygame.mixer.init() #starts the sound system.
            pygame.mixer.music.load(sound_file) #loads the MP3.
            pygame.mixer.music.play() #plays the sound. 🎧

            # The loop keeps the program running until the alarm finishes.
            while pygame.mixer.music.get_busy(): # returns True while music is still playing.
                time.sleep(1)

            is_running = False

        time.sleep(1) #Inside the loop → ensures it doesn’t check the time thousands of times per second (CPU overload).


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)