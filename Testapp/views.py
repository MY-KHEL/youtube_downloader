from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from pytube import YouTube
# Create your views here.
def home(request):
    return render(request,'index.html')

def submit(request):
    url = request.GET['inp']
    url2 =url[32:]
    obj = YouTube(url)

    streams = obj.streams.filter(progressive=True)
    res = []
    for x in streams:
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
def download(request,pixel):
    #SAVE_PATH = "C:/" #to_dopath = 'C:/downloads'
    num = pixel.find('p')
    num = num+1

    pi = pixel[:num]
    val = pixel[num:]

    #print(type(stream))
    #stream.download()
    #print('Successfully Downloaded')
    strg = 'https://www.youtube.com/watch?v='+val
    print(strg)
    try:
	# object creation using YouTube
	# which was imported in the beginning
	    yt = YouTube(strg)
        
    except:
	    print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
    #mp4files = yt.streams.filter('mp4')


    stream =yt.streams.get_by_resolution(pi)

    try:
	# downloading the video
        if stream==None:
            # print(stream)
            messages.error(request, 'The resolution of the video selected cannot be download therefore select a higher resolution')
            return redirect('home')
        else:
            
	        stream.download("C:/Videos/")
    except:
	    print("Some Error!")

    print('Task Completed!')
    print(type(stream))

    return render(request,'done.html')

def test(request):
    myVideo = YouTube("https://www.youtube.com/watch?v=OTCuykFHBeA")
    myVideo.streams.first().download("C:/Videos/")
    print(myVideo.title)
    return redirect('home')