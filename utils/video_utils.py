import cv2

def read_video(vid_path):
    cap = cv2.VideoCapture(vid_path)
    frames=[]
    while True :
        ret ,frame=cap.read() #ret is flag whether the vid ended or not 
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frames,output_video_path):
    fourcc=cv2.VideoWriter_fourcc(*'XVID') #fourcc :the output video type 
    out=cv2.VideoWriter(output_video_path,fourcc,24,(output_video_frames[0].shape[1],output_video_frames[0].shape[0])) #(width,height)
    for frame in output_video_frames:
        out.write(frame)
    out.release