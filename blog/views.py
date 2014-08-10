from blog.models import Article
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.utils import timezone

# blog.views.index
def index(request):
    all_articles = Article.objects.all().order_by('-written_date')
    return render_to_response('index.html',
            {'all_articles' : all_articles, 'message' : 'write something'},
            context_instance=RequestContext(request))

# blog.views.submit
def submit(request):
    try:
        cont = request.POST['content']
    except (KeyError):
        return render_to_response('index.html',
                {'all_articles' : all_articles,
                    'message' : 'Failed to read content'}, context_instance=RequestContext(request))
    else:
        article = Article(content=cont, written_date=timezone.now())
        article.save()
        return HttpResponseRedirect('/blog')

# blog.views.remove
def remove(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.delete()
    return HttpResponseRedirect('/blog')


