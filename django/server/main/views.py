from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string


def index(request):
    """template = Template("Hello {{ name }}")
    context = Context({
        "name" : "User_Name"
    })"""
    template = get_template("main/index.html")
    context = {"name" : "User_Name"}
    return HttpResponse(
        template.render(context)
    )
    #return render(request, "main/index.html")

def contacts(request):
    #return render(request, "main/contacts.html")
    rendered_page = render_to_string("main/contacts.html", {
        "contacts" : ["Phone number - 8-800-999-700-33-40",
        "E-mail - APPS@mail.ru",
        "Address - Russia, Smolensk region, Safonovo, Microdistrict - 2, House - 32"]
    })
    return HttpResponse(rendered_page)
   