from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Path to the input video file
input_video_path = '1.mp4'

# Path to the output video file
output_video_path = 'output_video.mp4'

# Load the input video clip
video_clip = VideoFileClip(input_video_path)

# Define the text you want to add
text = "Software Engineer (New graduates) Hiring At Sansan"

# Create a TextClip with the specified text
text_clip = TextClip(text, fontsize=50, color='white', font='Arial', align='center').set_duration(video_clip.duration)

# Add the text clip above the video clip
composite_clip = CompositeVideoClip([video_clip, text_clip.set_position(('center', 'top'))])

# Write the composite clip to an output video file
composite_clip.write_videofile(output_video_path, codec='libx264', fps=video_clip.fps)

# Close all clips to free up resources
video_clip.close()
text_clip.close()
composite_clip.close()
