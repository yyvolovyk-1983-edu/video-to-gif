import cv2
from PIL import Image

def video_frame_img(video_file, output_file):
    cap = cv2.VideoCapture(video_file)  # open video file

    if not cap.isOpened():
        print("Error: could not open video file")
        return

    frames = []        # list for saving frames
    max_frames = 20    # max number of frames to save
    frame_count = 0    # counter

    while frame_count < max_frames:
        success, frame = cap.read()  # read frame
        if not success:
            break  # no more frames, exit loop

        frame = cv2.resize(frame, (320, 240))  # resize frame
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert BGR → RGB
        img = Image.fromarray(frame_rgb)  # create PIL image
        frames.append(img)

        frame_count += 1

    cap.release()  # close video

    if len(frames) == 0:
        print("No frames found.")
        return

    # Save as GIF
    frames[0].save(
        output_file,
        save_all=True,
        append_images=frames[1:],
        duration=150,
        loop=0
    )

    print(f"GIF saved as: {output_file}")


# Виклик з правильним шляхом
video_frame_img(
    r"C:\Users\USER\Downloads\example_video.mp4",
    "output.gif"
)

