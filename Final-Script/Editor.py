from moviepy.editor import *


def editor(video):
    main_video = VideoFileClip(video)

    # If 720p then resize*3
    # If 1080p then resize*2

    height = main_video.h

    if height == 1080:
        finalised_video = main_video.resize(2)
        duration_final = finalised_video.duration
        logo = ImageClip('D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\logo-nobg.png')
        logo_resized = logo.resize(0.1)
        final_clip = CompositeVideoClip([finalised_video, logo_resized.set_position((1060, 5))])
        # final_clip.set_duration(5).preview(audio=False, fullscreen=True, fps=5)
        final_clip.set_duration(duration_final).write_videofile('D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\\final.mp4')
    else:
        finalised_video = main_video.resize(3)
        duration_final = finalised_video.duration
        logo = ImageClip('D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\logo-nobg.png')
        logo_resized = logo.resize(0.1)
        final_clip = CompositeVideoClip([finalised_video, logo_resized.set_position((1060, 5))])
        # final_clip.set_duration(5).preview(audio=False, fullscreen=True, fps=5)
        final_clip.set_duration(duration_final).write_videofile('D:\\a\TheGreatAutomation\TheGreatAutomation\Final-Script\Final-Script\\final.mp4')

