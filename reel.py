from ensta import Host

# username = "jobsandcourses"
username = "hirewave.gg"

host = Host(username, password)

host.upload_reel(
    video_path="2.mp4",
    thumbnail_path="godlike.jpg",
    caption="Testing video"
)