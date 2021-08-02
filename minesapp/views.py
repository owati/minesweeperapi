from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SavedGames, PlayedGames
from .serialisers import PlayedGamesSerializer, SavedGamesSerializer


USER = get_user_model()

# the api endpoint view for the saving and retrieving saved games
class SavedGamesApi(generics.CreateAPIView):
    queryset = SavedGames.objects.all()
    serializer_class = SavedGamesSerializer


@api_view(['GET', 'DELETE'])
def retrieveView(request, id, gid = None):
    if request.method == 'GET':
        if gid:
            game = SavedGames.objects.get(id = gid)
            if game.user.id != id:
                return Response({}, status=403)
            else:
                return Response(
                    {
                        'id': game.id,
                        'name': game.name,
                        'level': game.level,
                        'mines_array': game.mines_array,
                        'opened_array': game.opened_array,
                        'time': game.time,
                        'time_saved': game.time_saved

                    }, status= 202
                )
        else:
            try:
                qs = SavedGames.objects.all().filter(user = id)
                qs_dict = [
                    {
                        'id': i.id,
                        'name': i.name,
                        'level': i.level,
                        'mines_array': i.mines_array,
                        'opened_array': i.opened_array,
                        'time': i.time,
                        'time_saved': i.time_saved
                    } for i in qs
                ]
                return Response(qs_dict, status=200)
            except:
                return Response({}, status=404)
    
    elif request.method == 'DELETE':
        game = SavedGames.objects.get(id = gid)
        game.delete()

        return Response({}, status=200)




class PlayedGamesApi(generics.ListCreateAPIView):
    queryset = PlayedGames.objects.all()
    serializer_class = PlayedGamesSerializer


@api_view(['POST'])
def loginView(request):
    if request.method == 'POST':
        name = request.data['name']
        password = request.data['pass']

        user = authenticate(nick_name=name, password=password)

        if user is not None:
            data = {
                'id': user.id,
                'nick_name': user.nick_name,
                'name': user.name,
                'sex': True,
                'profile': user.profile,
            }

            return Response(data, status=202)
        else:
            return Response({}, status=203)

@api_view(['GET','POST'])
def signupView(request):
    if request.method == 'POST':
        login_data = request.data
        user = USER.object.create_user(
            nickname=login_data['nickname'],
            password=login_data['pass1'],
            name='mineuser',
            sex=True,
            profile=1
        )
        if user is not None:
            return Response({}, status=200)
        else:
            return Response({}, status=400)

    if request.method == 'GET':
        qs=[ i.nick_name for i in USER.object.all()]
        return Response(data=qs, status=200)
