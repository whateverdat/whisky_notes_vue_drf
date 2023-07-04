from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist

from whisky.models import TastingNote, Comment
from whisky.serializers import TastingNoteSerializer, CommentsSerializer

import random
# from itertools import chain


@api_view(['GET'])
def load_homepage(request):

    notes = TastingNote.objects.order_by('-date')[:10]
    serializer = TastingNoteSerializer(notes, many=True)
    return Response(serializer.data) 


@api_view(['GET'])
def load_note(request, slug):

    note = TastingNote.objects.all().filter(slug=slug)
    try:
        serializer = TastingNoteSerializer(note[0])
    except IndexError:
         return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)


@api_view(['GET'])
def load_comments(request, slug):

    comments = Comment.objects.all().filter(note__slug=slug).order_by('-date')
    serializer = CommentsSerializer(comments, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def make_comment(request):
    name = request.data['name']
    comment = request.data['comment']
    slug = request.data['slug']

    if not name or not comment:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    note = TastingNote.objects.filter(slug=slug)[0]
    newComment = Comment(note=note, name=name, comment=comment)
    newComment.save()
    serializer = CommentsSerializer(newComment)
    return Response(serializer.data)


@api_view(['GET'])
def load_all(request):

    notes = TastingNote.objects.order_by('name')
    serializer = TastingNoteSerializer(notes, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def double_database(request):
#     notes = TastingNote.objects.all()
#     for note in notes:
#         note.pk = None
#         note.save()
#     # comments = Comment.objects.all()
#     # for comment in comments:
#     #     comment.pk = None
#     #     comment.save()
#     return Response(200)


@api_view(['GET'])
def load_random(request):

    random_note = None
    if TastingNote.objects.filter(name__icontains=""):
        max_id = TastingNote.objects.all().aggregate(max_id=Max("id"))['max_id']
 
        while not random_note:
            try:
                pk = random.randint(1, max_id)
                random_note = TastingNote.objects.get(pk=pk)
            except TypeError:
                pass
            # Raised when random primary key hits a deleted object
            except ObjectDoesNotExist:
                pass

        serializer = TastingNoteSerializer(random_note)
        return Response(serializer.data)


@api_view(['GET'])
def load_category(request, category):
    
    schema = {
        'daily': 'tag',
        'value': 'tag',
        'gift': 'tag',
        'occasion': 'tag',
        'scotch': 'wtype',
        'irish': 'region',
        'american': 'region',
        'other': 'region'
    }
    # https://stackoverflow.com/questions/4720079/django-query-filter-with-variable-column
    variable_column = schema[category]
    filter = variable_column + '__' + 'contains'  
    notes = TastingNote.objects.filter(**{filter: category})
    
    serializer = TastingNoteSerializer(notes, many=True)
    return Response(serializer.data)
