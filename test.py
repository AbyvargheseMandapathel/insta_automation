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
fontScale = 3
fontColor = (255, 255, 255)
lineType = 2

# Calculate the position for center of the screen
text = 'Software Engineer (New graduates) Hiring At Sansan'
max_width = int(0.9 * width)  # Maximum width for the text
text_lines = []
text_line = ''
for word in text.split():
    # Add words to the current line until it exceeds max_width
    if cv2.getTextSize(text_line + ' ' + word, font, fontScale, lineType)[0][0] <= max_width:
        text_line += ' ' + word
    else:
        # Start a new line if the current line exceeds max_width
        text_lines.append(text_line.strip())
        text_line = word

# Add the last line
if text_line:
    text_lines.append(text_line.strip())

# Calculate the position for center of the screen
text_height = cv2.getTextSize(text_lines[0], font, fontScale, lineType)[0][1] * len(text_lines)
text_position_x = int((width - max_width) / 2)
text_position_y = int((height - text_height) / 2)

# Read and process each frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Add text overlay at the calculated position
    for i, line in enumerate(text_lines):
        cv2.putText(frame, line, 
                    (text_position_x, text_position_y + i * int(text_height / len(text_lines))), 
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
