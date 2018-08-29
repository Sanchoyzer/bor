from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.db.models import Q

from datetime import datetime

from .models import Quote, Comment


def index(request):
    today_min = datetime.combine(datetime.today(), datetime.min.time())
    today_max = datetime.combine(datetime.today(), datetime.max.time())
    return render(
        request,
        'bor/index.html',
        context = {
            'count_quotes_all': Quote.objects.filter(isApproved=True, isHided=False).count(),
            'count_quotes_new': Quote.objects.filter(isApproved=True, isHided=False, date__range=(today_min, today_max)).count(),
            'count_quotes_hide_bad': Quote.objects.filter(isApproved=True, isHided=False, rating__gte=0).count(),
            'count_quotes_abyss': Quote.objects.filter(isApproved=False, isHided=False).count()
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
    queryset = Quote.objects.filter(isApproved=True, isHided=False).order_by('id')
    template_name = 'bor/quotes_all_list.html'
    paginate_by = 2


class QuotesHideBadListView(QuotesAllListView):
    queryset = Quote.objects.filter(isApproved=True, isHided=False, rating__gte=0).order_by('id')
    template_name = 'bor/quotes_hide_bad_list.html'


class QuotesRandomListView(QuotesBaseListView):
    queryset = Quote.objects.filter(isApproved=True, isHided=False).order_by('?')[:2]
    template_name = 'bor/quotes_random_list.html'


class QuotesNewListView(QuotesBaseListView):
    queryset = Quote.objects.filter(isApproved=True, isHided=False, date__range=(
        datetime.combine(datetime.today(), datetime.min.time()),
        datetime.combine(datetime.today(), datetime.max.time()))
                                   ).order_by('id')
    template_name = 'bor/quotes_new_list.html'


class QuotesByRatingListView(QuotesAllListView):
    queryset = Quote.objects.filter(isApproved=True, isHided=False).order_by('-rating')


class QuotesAbyssListView(QuotesBaseListView):
    queryset = Quote.objects.filter(isApproved=False, isHided=False).order_by('?')[:2]
    template_name = 'bor/quotes_abyss_list.html'


class QuotesAbyssTopListView(QuotesBaseListView):
    queryset = Quote.objects.filter(isApproved=False, isHided=False).order_by('rating')[:2]
    template_name = 'bor/quotes_abyss_top_list.html'


class QuotesSearchListView(QuotesAllListView):
    def get_queryset(self):
        text = self.request.GET.get('text', '')
        filter_set = Quote.objects.filter(isApproved=True, isHided=False).order_by('id')
        if text == '':
            return filter_set
        if text.isdigit():
            return filter_set.filter(Q(text__icontains = text) | Q(id = int(text)))
        else:
            return filter_set.filter(Q(text__icontains = text))


class CommentDetailView(generic.DetailView):
    model = Comment
    context_object_name = 'comment'
    template_name = 'bor/comment_detail.html'
