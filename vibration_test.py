from time import sleep
from bhaptics import better_haptic_player as player
import keyboard
import cv2
from prepare import idx_ui
import numpy as np
import pickle

player.initialize()
sleep(10)
print('connect')
interval = 0.5
durationMillis = 500
intensity = 100

A1 = [1, 5, 9, 13, 17]
A2 = [0, 4, 8, 12, 16]
A3 = [0, 4, 8, 12, 16]
A4 = [1, 5, 9, 13, 17]
B1 = [2, 6, 10, 14, 18]
B2 = [3, 7, 11, 15, 19]
B3 = [3, 7, 11, 15, 19]
B4 = [2, 6, 10, 14, 18]
H1 = [1, 0, 0, 1, 2, 3, 3, 2]
H2 = [5, 4, 4, 5, 6, 7, 7, 6]
H3 = [9, 8, 8, 9, 10, 11, 11, 10]
H4 = [13, 12, 12, 13, 14, 15, 15, 14]
H5 = [17, 16, 16, 17, 18, 19, 19, 18]

idx = np.zeros([5, 8])
h = 480
w = 720
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter(f'vibration_test2.avi', fourcc, 50, (int(w) * 2, int(h)))
idx_list = [[1, 0, 0, 1, 2, 3, 3, 2], [5, 4, 4, 5, 6, 7, 7, 6], [9, 8, 8, 9, 10, 11, 11, 10], [13, 12, 12, 13, 14, 15, 15, 14], [17, 16, 16, 17, 18, 19, 19, 18]]

def play(index):
    if index == 1:  # A1
        for n, i in enumerate(A1):
            idx_arr = idx.copy()
            idx_arr[n, 3] = 1
            player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'A1')
            out.write(bg)
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 2:    # A2
        for n, i in enumerate(A2):
            idx_arr = idx.copy()
            idx_arr[n, 2] = 1
            player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'A2')
            out.write(bg)
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 3:    # A3
        for n, i in enumerate(A3):
            idx_arr = idx.copy()
            idx_arr[n, 1] = 1
            player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'A3')
            out.write(bg)
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 4:    # A4
        for n, i in enumerate(A4):
            idx_arr = idx.copy()
            idx_arr[n, 0] = 1
            player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'A4')
            out.write(bg)
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 5:    # B1
        for n, i in enumerate(B1):
            idx_arr = idx.copy()
            idx_arr[n, 4] = 1
            player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'B1')
            out.write(bg)
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 6:    # B2
        for n, i in enumerate(B2):
            idx_arr = idx.copy()
            idx_arr[n, 5] = 1
            player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'B2')
            out.write(bg)
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 7:    # B3
        for n, i in enumerate(B3):
            idx_arr = idx.copy()
            idx_arr[n, 6] = 1
            player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'B3')
            out.write(bg)
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 8:    # B4
        for n, i in enumerate(B4):
            idx_arr = idx.copy()
            idx_arr[n, 7] = 1
            player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'B4')
            out.write(bg)
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 9:  # H1
        for n, i in enumerate(H1):
            idx_arr = idx.copy()
            idx_arr[0][n] = 1
            if n in [2, 3, 4, 5]:
                player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            else:
                player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'H1')
            out.write(bg)
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 10:  # H2
        for n, i in enumerate(H2):
            idx_arr = idx.copy()
            idx_arr[1][n] = 1
            if n in [2, 3, 4, 5]:
                player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            else:
                player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'H2')
            out.write(bg)
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 11:  # H3
        for n, i in enumerate(H3):
            idx_arr = idx.copy()
            idx_arr[2][n] = 1
            if n in [2, 3, 4, 5]:
                player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            else:
                player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'H3')
            out.write(bg)
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 12:  # H4
        for n, i in enumerate(H4):
            idx_arr = idx.copy()
            idx_arr[3][n] = 1
            if n in [2, 3, 4, 5]:
                player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            else:
                player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'H4')
            out.write(bg)
            cv2.imshow('bg', bg)

            cv2.waitKey(1)
            sleep(interval)

    elif index == 13:  # H5
        for n, i in enumerate(H5):
            idx_arr = idx.copy()
            idx_arr[4][n] = 1
            if n in [2, 3, 4, 5]:
                player.submit_dot("frontFrame", "VestFront", [{"index": i, "intensity": intensity}], durationMillis)
            else:
                player.submit_dot("backFrame", "VestBack", [{"index": i, "intensity": intensity}], durationMillis)
            bg = idx_ui(idx_arr, 'H5')
            out.write(bg)
            cv2.imshow('bg', bg)
            cv2.waitKey(1)
            sleep(interval)

    elif index == 14: # testvideo
        img_h = 480
        img_w = 720
        with open(f'testvideo/testvideo', 'rb') as fr:
            mag_arrs = pickle.load(fr)
        cap = cv2.VideoCapture('testvideo/testvideo.mp4')

        for mag_arr in mag_arrs:
            test_bg = np.full((img_h, img_w, 3), 0, np.uint8)
            x = img_w // 8 // 2
            y = img_h // 5 // 2
            dotFrame_F = {
                "Position": "VestFront",
                "DotPoints": [],
                "DurationMillis": 30
            }
            dotFrame_B = {
                "Position": "VestBack",
                "DotPoints": [],
                "DurationMillis": 30
            }
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (img_w, img_h), interpolation=cv2.INTER_CUBIC)
            v = 0
            for i in range(5):
                for j in range(8):
                    print(mag_arr)
                    if mag_arr[i][j] > 80:
                        mag_arr[i][j] = 80
                    elif mag_arr[i][j] < 10:
                        mag_arr[i][j] = 0
                    # mag_arr[i][j] = mag_arr[i][j] * 0.3
                    if 2 <= j <= 5:
                        dotPint = {
                            "Index": idx_list[i][j],
                            "Intensity": int(mag_arr[i][j])
                        }
                        dotFrame_F["DotPoints"].append(dotPint)
                    else:
                        dotPint = {
                            "Index": idx_list[i][j],
                            "Intensity": int(mag_arr[i][j])
                        }
                        dotFrame_B["DotPoints"].append(dotPint)

                    if mag_arr[i][j] == 0:
                        c = 255
                        cv2.circle(test_bg, (x, y), img_h // 12, (c, c, c))
                    else:
                        c = 255 * int(mag_arr[i][j]) / 100
                        cv2.circle(test_bg, (x, y), img_h // 12, (c, c, c), -1)
                    x += img_w // 8
                    if (v + 1) % 8 == 0:
                        x = img_w // 8 // 2
                        y = y + img_h // 5
                    v += 1
                player.submit("dotPoint_F", dotFrame_F)
                player.submit("dotPoint_B", dotFrame_B)
            concat = np.concatenate((frame, test_bg), axis=1)
            out.write(concat)
            cv2.imshow('bg', concat)
            if cv2.waitKey(30) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


def run():

    while True:
        bg = idx_ui(idx, 0)

        cv2.imshow('bg', bg)
        cv2.waitKey(1)
        key = keyboard.read_key()
        if key == "z":
            break
        elif key == "1":
            play(1)
        elif key == "2":
            play(2)
        elif key == "3":
            play(3)
        elif key == "4":
            play(4)
        elif key == "5":
            play(5)
        elif key == "6":
            play(6)
        elif key == "7":
            play(7)
        elif key == "8":
            play(8)
        elif key == "q":
            play(9)
        elif key == "w":
            play(10)
        elif key == "e":
            play(11)
        elif key == "r":
            play(12)
        elif key == "t":
            play(13)
        elif key == "a":
            play(14)
    cv2.destroyAllWindows()


#        if cv2.waitKey(1) == ord('q'):
#            break



if __name__ == "__main__":

    run()
