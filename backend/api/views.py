from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Bookserializer, Memberserializer, Circulationserializer
from .models import Books, Members, Circulation
from django.http import HttpResponse
import json
import datetime
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint':'/addbook/',
            'method':'POST',
            'body':None,
            'description':'Returns an array of books'
        },
        {
            'Endpoint':'/books/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of books'
        },
        {
            'Endpoint':'/addmember/',
            'method':'POST',
            'body':None,
            'description':'Returns an array of books'
        },
        {
            'Endpoint':'/members/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of members'
        },
         {
            'Endpoint':'/checkoutbook/',
            'method':'POST',
            'body':None,
            'description':'Creates a checkout event'
        },
         {
            'Endpoint':'/overduebook/',
            'method':'GET',
            'body':None,
            'description':'Calculates overdue amount'
        },
         {
            'Endpoint':'/returnbook/',
            'method':'POST',
            'body':None,
            'description':'Creates a return event'
        },

    ]
    return Response(routes)

@api_view(['GET'])
def getbooks(request):
    booksdata = Books.objects.all()
    serializer = Bookserializer(booksdata, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def addbook(request, book_name):
    booksdata = Books.objects.all()
    serializer = Bookserializer(booksdata, many=True)
    print(booksdata)
    try:
        print(book_name)
        bookdata = Books.objects.get(book_name= book_name)
        print(bookdata)
        bookdata.copies = bookdata.copies + 1
        print('successfully added book copy')
        bookdata.save()
        return Response(serializer.data)
    except:
        book_id = 1000 + booksdata.count()
        book = Books.objects.create(book_name= book_name, book_id= book_id)
        book.save()
        print('successfully added book')
        booksdata = Books.objects.all()
        return Response(serializer.data)

@api_view(['GET','POST'])
def addmember(request, member_name):
    membersdata = Members.objects.all()
    member_id = 2000 + membersdata.count()
    print(member_id)
    serializer = Memberserializer(membersdata, many=True)
    member = Members.objects.create(member_name= member_name, member_id= member_id)
    member.save()
    print('successfully added member')
    return Response(serializer.data)

@api_view(['GET'])
def getmembers(request):
    membersdata = Members.objects.all()
    serializer = Memberserializer(membersdata, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def checkoutbook(request, book_id, member_id):
    bokksdata = Books.objects.all()
    membersdata = Members.objects.all()
    circulationdata = Circulation.objects.all()
    bookSerializer = Bookserializer(bokksdata, many=True)
    memberSerializer = Memberserializer(membersdata, many=True)
    circulationSerializer = Circulationserializer(circulationdata, many=True)
    bookdata = Books.objects.get(book_id= book_id)
    circulationhoarding = Circulation.objects.filter(returnevent= False)

    for i in circulationhoarding:
        if int(i.member_id) == int(member_id):
            print('member already has a book checked out')
            return Response('member already has a book checked out')

    if bookdata.copies > 0:
        bookdata.copies = bookdata.copies - 1
        bookdata.save()
        circulation = Circulation.objects.create(book_id= book_id, member_id= member_id)
        circulation.save()
        print('successfully checked out book')
        return Response('successfully checked out book')
    else:
        print('book not available')
        return Response('book not available')

@api_view(['GET'])
def overduebook(request, book_id, member_id):
    try:
        circulation = Circulation.objects.get(book_id= book_id, member_id= member_id, returnevent= False)
        circulationdate = circulation.date
        currentdate = datetime.datetime.now()
        finedays = (currentdate - circulationdate).days
        fine = 0
        if(finedays > 7):
            fine = (finedays%7) * 50
        return Response(fine)
    except:
        return Response('No book found')
    
@api_view(['GET','POST'])
def returnbook(request, member_id):
    try:
        circulation = Circulation.objects.get(member_id= member_id, returnevent= False)
        circulation.returnevent = True
        book_id = circulation.book_id
        circulation.returndate = datetime.datetime.now()
        finedays = (circulation.date - circulation.returndate).days
        fine = 0
        if(finedays > 7):
            fine = (finedays%7) * 50
        circulation.save()
        bookdata = Books.objects.get(book_id= book_id)
        bookdata.copies = bookdata.copies + 1
        bookdata.save()
        print('successfully returned book with fine of ' + str(fine) + ' rupees')
        return Response('successfully returned book with fine of ' + str(fine) + ' rupees')
    except:
        return Response('No book found')