from django import template
from django.core.paginator import Paginator
# from django.template.loader import render_to_string
from pagination.settings import PAGINATION_PAGE_SIZE

register = template.Library()


# @register.simple_tag(name='pagination', takes_context=True)
@register.inclusion_tag('pagination/pagination.html', name='pagination', takes_context=True)
def render_pagination(context, value):
    if PAGINATION_PAGE_SIZE:
        request = context.get('request')
        page = request.GET.get('page')

        paginator = Paginator(value, PAGINATION_PAGE_SIZE)
    
        # return render_to_string(
        #     'pagination/pagination.html',
        #     {
        #         'page_obj': paginator.get_page(page),
        #         'paginator': paginator
        #     }
        # )

        return {
            'page_obj': paginator.get_page(page),
            'paginator': paginator
        }

@register.filter(name='paginate')
def paginate_value(value, page):
    if PAGINATION_PAGE_SIZE:
        paginator = Paginator(value, PAGINATION_PAGE_SIZE)

        return paginator.get_page(page)
    
    return value
