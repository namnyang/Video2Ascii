# -*- coding:utf-8 -*-

import click

from nyvideo2ascii.converter import nyvideo2ascii


@click.command()
@click.option("--chars_width", default=100, help='비디오의 문자 너비 [기본값 : 80]')
@click.option("--fps", default=8, help='비디오의 프레임 [기본값 : 10]')
@click.option("--pixels", default=None, type=str, help='비디오 제작에 사용할 문자')
@click.option("--t_start", default=0, help="비디오 변환 시작 시간(초)")
@click.option("--t_end", default=None, type=int, help="비디오 변환 종료 시간(초)")
@click.option("--output", default="output.mp4", help='출력할 파일의 이름 [기본값 : output.mp4]')
@click.argument("filename")
def convert(filename, chars_width, fps, pixels, output, t_start, t_end):
    converter = nyvideo2ascii(video_path=filename,
                              fps=fps,
                              chars_width=chars_width,
                              t_start=t_start,
                              t_end=t_end,
                              pixels=pixels)

    clip = converter.generate_chars_video()
    clip.write_videofile(output)
