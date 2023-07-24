from django.http import HttpResponse
import time, asyncio
from movies.models import Movie
from stories.models import Story
from asgiref.sync import sync_to_async

# helper func
def get_moveis():
    print("prepare to get movies")
    time.sleep(2)
    qs=Movie.objects.all()
    print(qs)   
    print('got all the moveis')


def get_stories():
    print("prepare to get stories")
    time.sleep(5)
    qs=Story.objects.all()
    print(qs)   
    print('got all the stories')


# async 
@sync_to_async
def get_moveis_async():
    print("prepare to get movies")
    time.sleep(2)
    qs=Movie.objects.all()
    print(qs)   
    print('got all the moveis')

@sync_to_async
def get_stories_async():
    print("prepare to get stories")
    time.sleep(5)
    qs=Story.objects.all()
    print(qs)   
    print('got all the stories')




# views
def home_view(requst):
    return HttpResponse("Welcome to the Home Page!")

def main_view(request):
    start_time = time.time()
    get_moveis()
    get_stories()
    total = (time.time()-start_time)
    print('total:', total)
    return HttpResponse('sync')

async def main_view_async(request):
    start_time = time.time()
    # task1 = asyncio.ensure_future(get_moveis_async())
    # task2 = asyncio.ensure_future(get_stories_async())
    # await asyncio.wait([task1, task2])
    await asyncio.gather(get_moveis_async(), get_stories_async())
    total = (time.time()-start_time)
    print('total:', total)
    return HttpResponse('async')