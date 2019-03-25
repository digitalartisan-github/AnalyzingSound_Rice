#!/usr/bin/env bash
ffmpeg -framerate 30 -start_number 0 -i ../result/graph/%05d.png -r 30 -an -vcodec libx264 -pix_fmt yuv420p ../result/out.mp4