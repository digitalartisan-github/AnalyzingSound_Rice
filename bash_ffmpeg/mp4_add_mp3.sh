#!/usr/bin/env bash
ffmpeg -i ../result/out.mp4  -i ../assets/WashingRice.mp3 -c:v copy -c:a aac -strict experimental -map 0:v -map 1:a ../result/AddSound.mp4