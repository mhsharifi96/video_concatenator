from moviepy.editor import VideoFileClip, concatenate_videoclips,ImageClip,CompositeVideoClip
myClip = VideoFileClip("r1.mp4")
# myClip.resize( (460,720) ) # New resolution: (460,720)
# myClip.resize(0.8) # width and heigth multiplied by 0.6
# myClip.resize(width=800) # height comp
clip3 = VideoFileClip("sample3.mp4").resize(1080,1080)
logo = (ImageClip("safine.png")
          .set_duration(10)
          .resize(height=200) # if you need to resize...
          .margin(right=8, top=8, opacity=0) # (optional) logo-border padding
          .set_pos(("right","top")))
# clip3.resize( (460,720) ) # New resolution: (460,720)
# clip3.resize(0.8) # width and heigth multiplied by 0.6
# clip3.resize(width=800) # height comp
final = CompositeVideoClip([clip3, logo])
final_clip = concatenate_videoclips([myClip,final],method='compose')
final_clip.write_videofile("out4.mp4")



