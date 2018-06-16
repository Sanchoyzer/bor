from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from datetime import datetime

from .models import Quote, Comment


def index(request):
    today_min = datetime.combine(datetime.today(), datetime.min.time())
    today_max = datetime.combine(datetime.today(), datetime.max.time())
    return render(
        request,
        'bor/index.html',
        context = {
            'count_quotes_all': Quote.objects.all().count(),
            'count_quotes_new': Quote.objects.filter(date__range=(today_min, today_max)).count(),
            'count_quotes_hide_bad': Quote.objects.filter(rating__gte=0).count()
        },
    )


def change_rating(request, pk, val):
    quote = get_object_or_404(Quote, pk = pk)
    quote.rating += val
    quote.save()
    return redirect('quotes-all')


def quote_rulez(request, pk):
    return change_rating(request, pk, 1)


def quote_sux(request, pk):
    return change_rating(request, pk, -1)


def quote_bayan(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    quote.copyPasteRating += 1
    quote.save()
    return redirect('quotes-all')


class QuoteDetailView(generic.DetailView):
    model = Quote
    context_object_name = 'quote'
    template_name = 'bor/quote_detail.html'


class QuotesBaseListView(generic.ListView):
    model = Quote
    context_object_name = 'quotes'


class QuotesAllListView(QuotesBaseListView):
    queryset = Quote.objects.order_by('id')
    template_name = 'bor/quotes_all_list.html'
    paginate_by = 2


class QuotesHideBadListView(QuotesBaseListView):
    queryset = Quote.objects.filter(rating__gte=0).order_by('id')
    template_name = 'bor/quotes_hide_bad_list.html'


class QuotesRandomListView(QuotesBaseListView):
    queryset = Quote.objects.order_by('?')[:5]
    template_name = 'bor/quotes_random_list.html'


class QuotesNewListView(QuotesBaseListView):
    queryset = Quote.objects.filter(date__range=
        (datetime.combine(datetime.today(), datetime.min.time()),
         datetime.combine(datetime.today(), datetime.max.time()))
                                    ).order_by('id')
    template_name = 'bor/quotes_new_list.html'


class QuotesByRatingListView(QuotesAllListView):
    queryset = Quote.objects.order_by('-rating')


class CommentDetailView(generic.DetailView):
    model = Comment
    context_object_name = 'comment'
    template_name = 'bor/comment_detail.html'
