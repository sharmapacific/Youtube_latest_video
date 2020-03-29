from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def paginate_objects(request, objs_list):
    paginator = Paginator(objs_list, 5)
    page = request.GET.get('page')
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)
    return objs
