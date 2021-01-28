# 파이썬 아스키 아트 생성기

파이썬으로 만든 비디오를 아스키 아트로 변환하는 프로그램

## 요구사항

Python **3.6** 이상

-   moviepy
-   numpy
-   pillow
-   click
-   equests
-   ffmpeg

## 사용법

```
main.py videofile.mp4
```

## 옵션

```
--chars_width : 비디오의 문자 너비 [기본값 : 80]
--fps : 비디오의 프레임 [기본값 : 10]
--pixels : 비디오 제작에 사용할 문자
--t_start : 비디오 변환 시작 시간(초)
--t_end : 비디오 변환 종료 시간(초)
--output : 출력할 파일의 이름 [기본값 : output.mp4]
```

**프레임 수를 높이면 비디오 제작에 시간이 많이 들어갑니다**

### 참고한 레파지토리 : https://github.com/ryan4yin/video2chars
