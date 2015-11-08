from django.shortcuts import render
from .models import Auth
from django.http import HttpResponse
# Create your views here.
def view(request):
	latest = Auth.objects.all()
	context = {'latest': latest, 'tweets': getTweets()}
	return render(request, 'socialfeed/index.html', context)
def getTweets():
        tweets = []
        try:
                import twitter
                api = twitter.Api(consumer_key='bgY8u0GrdDnN1mRjau4BmyPB1',consumer_secret='PgXe9uCBpQ70w3EqaydrLxcF8jM7TEqV9hFCxKSCrncNTQGGg4',access_token_key='2184870032-RpgC5Akz8m0fmkuDS6s2poGsu3NivtNhfP2uEq3',access_token_secret='QD0c3agaI3lhylK2zY4Eu2U3oHVtCtv4kCBk8oUxbJzy4')
                latest = api.GetUserTimeline()
                for t in latest:
                        tweets.append(t.text)
        except:
                tweets.append("No Status!")

        return tweets
