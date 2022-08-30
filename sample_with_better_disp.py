from time import sleep
import pickle
import cv2
import os
import random
import time
from bhaptics import better_haptic_player as player

player.initialize()
sleep(10)
subject = input('이름 : ')
answer = {}


idx_list = [[1, 0, 0, 1, 2, 3, 3, 2], [5, 4, 4, 5, 6, 7, 7, 6], [9, 8, 8, 9, 10, 11, 11, 10], [13, 12, 12, 13, 14, 15, 15, 14], [17, 16, 16, 17, 18, 19, 19, 18]]

nn = 150
A = cv2.imread('first_frame/A.jpg')
B = cv2.imread('first_frame/B.jpg')
A = cv2.resize(A, (nn, nn))
B = cv2.resize(B, (nn, nn))

path = 'video_data/'
# video_list = os.listdir(path)
video_list = ['car.mp4', 'butter2.mp4', 'plane2.mp4', 'ball2.mp4', 'fishingbird.mp4']

split_list = ['flow', 'edge']

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter(f'disp.avi', fourcc, 50, (int(1280), int(720)))
#video_path = 'C:/Users/heat/ONNX-RAFT-Optical-Flow-Estimation/doc/data/traffic.mp4'
for video in video_list:
    video_path = path + video

    video_name = video_path.split('/')[-1][:-4]

    mag_arr_list = {}

    with open(f'mag_flow/{video_name}', 'rb') as fr:
        mag_arr_flow = pickle.load(fr)
        mag_arr_list['flow'] = mag_arr_flow
    with open(f'mag_edge/edge_{video_name}', 'rb') as fr:
        mag_arr_edge = pickle.load(fr)
        mag_arr_list['edge'] = mag_arr_edge

    w = 1280
    h = 720
    random.shuffle(split_list)

    disp_interval = 50 # ms

    for fr, split in enumerate(split_list):
        print(split_list)
        if fr == 0:
            ab = 'a'
            abab = A
        else:
            ab = 'b'
            abab = B
        mag_arrs = mag_arr_list[split]
        cap = cv2.VideoCapture(video_path)
        for i in range(3):
            first_frame = cv2.imread(f'first_frame/{video_name}_{ab}_{3-i}.png')
            first_frame = cv2.resize(first_frame, (w, h), interpolation=cv2.INTER_CUBIC)
            for k in range(30):
                out.write(first_frame)
            cv2.imshow('test', first_frame)
            cv2.waitKey(1500)

        for mag_arr in mag_arrs:


            # print(mag_arr)
            t_start = time.time()

            sub1_start = time.time()
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (w, h), interpolation=cv2.INTER_CUBIC)
            frame[0:nn, w-nn:w] = abab

            sub1_end = time.time() - sub1_start

            sub2_start = time.time()
            vest_w = 8
            vest_h = 5

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

            for i in range(vest_h):
                for j in range(vest_w):

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
                    # print(dotPint['Index'], dotPint['Intensity'])
            # print(dotFrame_F)
            # print(dotFrame_B)
            # print(mag_arr)

            sub2_end = time.time() - sub2_start
            t_end = time.time() - t_start

            player.submit("dotPoint_F", dotFrame_F)
            player.submit("dotPoint_B", dotFrame_B)

            if (t_end*1000 < disp_interval):
                # print("sleep:",(disp_interval - t_end*1000), sub1_end*1000, sub2_end*1000)
                sleep((disp_interval - t_end*1000)/1000)
            out.write(frame)
            cv2.imshow('test', frame)
            # sleep(0.03)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    print('\nA와 B 중, 영상과 진동이 더 많이 일치하는 것을 고르시오.')
    # print(' 일치X              일치O')
    # print('<------           ------>')
    # print('  1    2    3    4    5')
    ans = input('다음 동영상으로 이동 : ')
    answer[f'{video_name}_{split_list}'] = ans


with open(f'survey_result/{subject}', 'wb') as fw:
    pickle.dump(answer, fw)

cap.release()
cv2.destroyAllWindows()

with open(f'survey_result/{subject}', 'rb') as fr:
    p = pickle.load(fr)

print(p)

