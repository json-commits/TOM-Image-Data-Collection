# import cv2
# import asyncio
# import time
#
# # while True:
# #     for i in range(2):
# #         ret, frame = video_capture_first_half[i].read()
# #         if ret:
# #             cv2.imshow(f'Camera {i}', frame)
# #
# #         ret, frame = video_capture_second_half[i].read()
# #         if ret:
# #             cv2.imshow(f'Camera {i+2}', frame)
# #
# #
# #     key = cv2.waitKey(20)
# #     if key == 27:  # exit on ESC
# #         break
#
#
# def display_frame(video_capture, cam_index):
#     while True:
#         ret, frame = video_capture.read()
#         if ret:
#             break
#
#     cv2.imshow(f'Camera {cam_index}', frame)
#     video_capture.release()
#     return frame
#
#
# async def main():
#     while True:
#         video_captures = [cv2.VideoCapture(x) for x in range(4)]
#         for i in range(2):
#             task = asyncio.create_task(display_frame(video_captures[i], i))
#             task2 = asyncio.create_task(display_frame(video_captures[i+1], i+1))
#
#             await asyncio.wait([task, task2])
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
# if __name__ == '__main__':
#     asyncio.run(main())
#     cv2.destroyAllWindows()


import cv2
from skimage import exposure
import os
import shutil

# loop = True

folder_name = "breaker4 [12-09-2023]"  # change this value to what you're testing
shutil.copytree('saved images template', f'saved images ({folder_name})')

for repeat in range(5):
    for i in range(0, 4, 1):
        cap = cv2.VideoCapture(i)
        ret, frame = cap.read()
        if ret:
            # frame = exposure.adjust_gamma(frame, 3)
            cv2.imshow(f'Camera {i}', frame)
            cv2.imwrite(f"saved images ({folder_name})/{i + 1}/{repeat}.jpg", frame)
        cap.release()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            # loop = False
            break
cv2.destroyAllWindows()
