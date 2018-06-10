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


class QuotesAllListView(generic.ListView):
    model = Quote
    queryset = Quote.objects.order_by('id')
    context_object_name = 'quotes'
    template_name = 'bor/quotes_all_list.html'
    paginate_by = 2


class QuotesHideBadListView(QuotesAllListView):
    queryset = Quote.objects.filter(rating__gte=0).order_by('id')


class CommentDetailView(generic.DetailView):
    model = Comment
    context_object_name = 'comment'
    template_name = 'bor/comment_detail.html'
