# -*- coding:utf-8 -*-

from pkg_resources import resource_stream

import numpy as np
from moviepy.editor import *

from PIL import Image, ImageFont, ImageDraw


class nyvideo2ascii:
    def __init__(self, video_path, fps, pixels, chars_width, t_start=0, t_end=None):
        video_clip = VideoFileClip(video_path).subclip(t_start, t_end)

        self.fps = fps
        self.pixels = pixels if pixels else \
            "$#@&%ZYXWVUTSRQPONMLKJIHGFEDCBA098765432?][}{/)(><zyxwvutsrqponmlkjihgfedcba*+1-."

        self.chars_width = chars_width
        self.chars_height = int(chars_width / video_clip.aspect_ratio)

        self.video_clip: VideoClip = video_clip.resize(
            (self.chars_width, self.chars_height))

        font_fp = resource_stream("nyvideo2ascii", "DroidSansMono.ttf")
        self.font = ImageFont.truetype(font_fp, size=14)
        self.font_width = sum(self.font.getsize(
            "a")) // 2

        self.video_size = int(
            self.chars_width * self.font_width), int(self.chars_height * self.font_width)

    def get_char_by_gray(self, gray):
        percent = gray / 255
        index = int(percent * (len(self.pixels) - 1))
        return self.pixels[index]

    def get_chars_frame(self, t):
        img_np = self.video_clip.get_frame(t)
        img = Image.fromarray(img_np, "RGB")
        img_gray = img.convert(mode="L")

        img_chars = Image.new("RGB", self.video_size, color="white")
        brush = ImageDraw.Draw(img_chars)

        for y in range(self.chars_height):
            for x in range(self.chars_width):
                r, g, b = img_np[y][x]

                gray = img_gray.getpixel((x, y))
                char = self.get_char_by_gray(gray)

                position = x * self.font_width, y * self.font_width
                brush.text(position, char, fill=(r, g, b), font=self.font)

        return np.array(img_chars)

    def generate_chars_video(self):
        """生成字符视频对象"""
        clip = VideoClip(self.get_chars_frame,
                         duration=self.video_clip.duration)

        return (clip.set_fps(self.fps)
                .set_audio(self.video_clip.audio))
