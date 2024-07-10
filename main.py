from utils import read_video, save_video 
from trackers import Tracker
import cv2

def main():
    # Read Video
    video_frames = read_video('input_videos/08fd33_8.mp4')

    # Initialize Tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=True,
                                       stub_path='stubs/track_stubs.pkl')
    
    #Saved cropped image of the players
    for track_id, player in tracks['players'][0].items():
        bbox = player['bbox']
        frame = video_frames[0]

        #cropped bbox from frame
        croppped_image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]

        #save it
        cv2.imwrite(f'output_videos/cropped_image.jpg', croppped_image)
        break

    
    #Draw output
    ##Draw object tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks)
    
    # Save video
    save_video(output_video_frames, 'output_videos/output_video.avi')



if __name__ == '__main__':
    main()
 