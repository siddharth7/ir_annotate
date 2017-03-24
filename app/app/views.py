from django.contrib.auth.models import User
from django.http import Http404
from django.http import HttpResponseForbidden
from .models import TweetInfo
from django.shortcuts import render_to_response,get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext  
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect


@login_required(login_url="login/")
@csrf_exempt
def home(request):
	context = RequestContext(request)
	if(request.method=='POST'):
		if request.POST.get("No"):
			unannotated_tweets = TweetInfo.objects.all().filter(user=request.user, tweet_agression = '2')
			# unannotated_tweets[0].tweet_agression='-1'
			# unannotated_tweets[0].save([])
			print "dad",unannotated_tweets[0]
			t = TweetInfo.objects.get(tweet_id=unannotated_tweets[0])
			t.tweet_agression='-1'
			t.save()
		elif request.POST.get("Un"):
			print 'Un'
			unannotated_tweets = TweetInfo.objects.all().filter(user=request.user, tweet_agression = '2')
			unannotated_tweets.tweet_agression='0'
			unannotated_tweets.save()
		elif request.POST.get("Yes"):
			print 'Yes'
			unannotated_tweets = TweetInfo.objects.all().filter(user=request.user, tweet_agression = '2')
			unannotated_tweets.tweet_agression='1'
			unannotated_tweets.save()
	print request.user
	# tweets = TweetInfo.objects.all().filter(user=request.user)
	unannotated_tweets = TweetInfo.objects.all().filter(user=request.user, tweet_agression = '2')
	print "len", len(unannotated_tweets)
	# for tweet in tweets:
	# 	print tweet.tweet_id
	return render(request,'app/home.html',{'tweet' : unannotated_tweets[0]})

@csrf_exempt
def login_user(request):
    csrfContext = RequestContext(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render_to_response('app/login.html', csrfContext)


def logout_view(request):
    logout(request)
    return redirect('home')


# def add_data(request):
# 	f=open('/Users/siddharth/Desktop/IR-Project-master/newdata.dat')

# 	# TweetInfo.objects.all().delete()
# 	lines = f.readlines()
# 	# for lines in f:
# 	users = User.objects.all()
# 	print users
# 	print len(lines)
# 	counter=0
# 	for line in lines:
# 		if(counter==80002):
# 			break
# 		try:
# 			line = line.split(",")
# 			# print line
# 			tweet = TweetInfo(user = users[counter%8] , tweet_id=line[0], tweet_text=line[1], tweet_agression='2')
# 			tweet.save()
# 			counter=counter+1
# 		except:
# 			pass
# 	return HttpResponse("Done")

