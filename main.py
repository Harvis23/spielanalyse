from utils import read_video, save_video 

def main():
    # Read Video
    video_frames = read_video('/Users/harviscastellanos/Documents/Projects/spielanalyse/input_videos/08fd33_4.mp4')

    # Save video
    save_video(video_frames, 'output_videos/output_video.avi')



if __name__ == '__main__':
    main()
