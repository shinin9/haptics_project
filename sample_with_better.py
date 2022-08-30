from time import sleep
from bhaptics import better_haptic_player as player
import pickle
import cv2
import os
import random


# player.initialize()


subject = input('이름 : ')
answer = {}

dotFrame_F = {
    "Position": "VestFront",
    "DotPoints": [],
    "DurationMillis": 1000
}
dotFrame_B = {
    "Position": "VestBack",
    "DotPoints": [],
    "DurationMillis": 1000
}

path = 'C:/Users/heat/ONNX-RAFT-Optical-Flow-Estimation/video_data_before/'
video_list = os.listdir(path)

split_list = ['flow', 'edge']
#video_path = 'C:/Users/heat/ONNX-RAFT-Optical-Flow-Estimation/doc/data/traffic.mp4'
for video in video_list:
    video_path = path + video
    video_name = video_path[59:-4]
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
    for fr, split in enumerate(split_list):
        mag_arrs = mag_arr_list[split]
        cap = cv2.VideoCapture(video_path)
        first_frame = cv2.imread(f'C:/Users/heat/ONNX-RAFT-Optical-Flow-Estimation/first_frame/{video_name}{fr+1}.png')
        first_frame = cv2.resize(first_frame, (w, h), interpolation=cv2.INTER_CUBIC)
        cv2.imshow('test', first_frame)
        cv2.waitKey(600)
        for mag_arr in mag_arrs:

            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (w, h), interpolation=cv2.INTER_CUBIC)

            vest_w = 8
            vest_h = 5
            v = 0
            for i in range(vest_h):
                for j in range(vest_w):
                    if mag_arr[i][j] > 100:
                        mag_arr[i][j] = 100
                    elif mag_arr[i][j] < 10:
                        mag_arr[i][j] = 0

                    if 2 <= j <= 5:
                        dotPint = {
                            "Index": int(v),
                            "Intensity": int(mag_arr[i][j])
                        }
                        dotFrame_F["DotPoints"].append(dotPint)
                    else:
                        dotPint = {
                            "Index": int(v),
                            "Intensity": int(mag_arr[i][j])
                        }
                        dotFrame_B["DotPoints"].append(dotPint)
                    v += 1

            cv2.imshow('test', frame)

            player.submit("dotPoint_F", dotFrame_F)
            player.submit("dotPoint_B", dotFrame_B)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        print('\n영상과 진동이 일치하는 정도를 평가해주세요.')
        print(' 일치X              일치O')
        print('<------           ------>')
        print('  1    2    3    4    5')
        ans = input('답 : ')
        answer[f'{split}_{video_name}'] = ans


with open(f'survey_result/{subject}', 'wb') as fw:
    pickle.dump(answer, fw)

cap.release()
cv2.destroyAllWindows()

with open(f'survey_result/{subject}', 'rb') as fr:
    p = pickle.load(fr)

print(p)

