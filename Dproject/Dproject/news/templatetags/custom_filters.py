#!/usr/bin/python3
# -*- coding:utf-8 -*-
#auth:zhiyi
from django.template import Library
register = Library()

@register.filter
def fix_img_url(img):
    return 'static/images/' + str(img)


if __name__ == '__main__':
    pass