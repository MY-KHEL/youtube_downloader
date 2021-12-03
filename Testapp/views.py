from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from pytube import YouTube , Stream, monostate
# Create your views here.
def home(request):
    return render(request,'index.html')



def submit(request):
    url = request.GET['inp']
    url2 =url[32:]
    video = YouTube(url)

    video_type = video.streams.filter(progressive=True,file_extension='mp4')
    res = []
    for x in video_type:
        res.append(x.resolution)
    res = list(dict.fromkeys(res))
    
    embed = url.replace('watch?v=','embed/')
    context={
        'url':url,
        'embed':embed,
        'res':res,   
        'url2':url2,   
         }
    return render(request,'submit.html',context)
import os
def download(request,pixel):
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    #SAVE_PATH = "C:/" #to_dopath = 'C:/downloads'
    num = pixel.find('p')
    num = num+1
 
    pi = pixel[:num]
    val = pixel[num:]
    video = None
    #print(type(stream))
    #stream.download()
    #print('Successfully Downloaded')
    strg = 'https://www.youtube.com/watch?v='+val
    print(strg)
    try:
	# object creation using YouTube
	# which was imported in the beginning
	    video = YouTube(strg)
        
    except:
	    print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
    #mp4files = yt.streams.filter('mp4')
    video_type = video.streams.filter(progressive=True,file_extension='mp4')

    stream =video.streams.get_by_resolution(pi)

    try:
	# downloading the video
        if stream==None:
            # print(stream)
            messages.error(request, 'The resolution of the video selected cannot be download therefore select a higher resolution')
            return redirect('home')
        else:
            
	        stream.download(download_path)
    except:
	    print("Some Error!")

    print('Task Completed!')
    print(type(stream))
    context={
       'saver':download_path
    }
    return render(request,'done.html')
import os
def test(request): 
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    
    strg ="https://www.youtube.com/watch?v=OTCuykFHBeA"
    val = strg[32:]
    myVideo = YouTube(strg)
   
    vid =myVideo.streams.first().download(download_path)
    
    
    print(myVideo.title)
    print('.............................')
    print(download_path)
    return redirect('home')