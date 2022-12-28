from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet


# homepage view.
def home_page_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "pages/home.html", context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "isUser": False,
        'response': tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    consume by JavaScript/Swift/Java/iOS/Android
    return json data
    :param request:
    :param tweet_id: The id of the tweet to retrieve
    :param args:
    :param kwargs:
    :return: JsonResponse
    """
    data = {
        "status": 200,
        "id": tweet_id,
        # "image_path": obj.image.url
    }
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        data["message"] = "Not found"
        data["status"] = 400
    return JsonResponse(data, status=data["status"])  # json.dumps content_type='application/json'
