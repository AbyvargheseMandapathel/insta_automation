import cv2

# Path to the input video file
input_video_path = '1.mp4'

# Path to the output video file
output_video_path = 'output_video.mp4'

# Open the video file
cap = cv2.VideoCapture(input_video_path)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

font_path = 'Barlow-ExtraBold.ttf' 
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 80
fontColor = (255, 255, 255)
lineType = 2

# Calculate the position for center of the screen
text = 'Software Engineer (New graduates) Hiring At Sansan'
text_size = cv2.getTextSize(text, font, fontScale, lineType)[0]
text_width, text_height = text_size
text_position_x = int((width - text_width) / 2)
text_position_y = int((height - text_height) / 2)

# Read and process each frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Add text overlay at the calculated position
    cv2.putText(frame, 'Software Engineer (New graduates) Hiring At Sansan', 
                (text_position_x, text_position_y), 
                font, 
                fontScale,
                fontColor,
                lineType)
    
    # Write the frame to the output video
    out.write(frame)

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
