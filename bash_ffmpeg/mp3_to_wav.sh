#!/usr/bin/env bash
ffmpeg -i ../assets/WashingRice.mp3 -vn -ac 2 -ar 44100 -acodec pcm_s16le -f wav ../assets/WashingRice.wav