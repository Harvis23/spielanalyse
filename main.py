from utils import read_video, save_video 
from trackers import Tracker
from team_asssigner import TeamAssigner
import cv2

def main():
    # Read Video
    video_frames = read_video('input_videos/08fd33_8.mp4')

    # Initialize Tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=True,
                                       stub_path='stubs/track_stubs.pkl')
    
    #Assign player team
    team_assigner = TeamAssigner()
    team_assigner.assing_team_color(video_frames[0],
                                    tracks["players"][0])
    
    for frame_num, player_track in enumerate(tracks["players"]):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num],   
                                                 track['bbox'],
                                                 player_id)
            tracks['players'][frame_num][player_id]['team'] = team 
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]



    
    #Draw output
    ##Draw object tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks)
    
    # Save video
    save_video(output_video_frames, 'output_videos/output_video.avi')



if __name__ == '__main__':
    main()
 