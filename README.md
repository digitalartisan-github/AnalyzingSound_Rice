# AnalyzingSound_Rice


ffmpeg -framerate 30 -start_number 0 -i output-%05d.png -r 30 -an -vcodec libx264 -pix_fmt yuv420p ../out1.mp4

ffmpeg -i out1.mp4  -i ../../Desktop/output.mp3 -c:v copy -c:a aac -strict experimental -map 0:v -map 1:a AddSound.mp4
