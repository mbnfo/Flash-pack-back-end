from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from base.serializers import FlashPackSerializer, FlashSerializer
from base.models import FlashCard, FlashPacks
from rest_framework_simplejwt.tokens import RefreshToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        return token
        

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

        
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh'
        
    ]
    return Response(routes)


@api_view(['POST'])  
def signin(request):
    useremail = str(request.data['username'] + '@gmail.com')
    user = User.objects.create_user(username = request.data['username'], password = request.data['password'])
    user.save()
    
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    return Response({
    'access_token': access_token,
    'refresh_token': str(refresh),
    'user': user.username
        })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createFlash(request):
    user = request.user
    pack = FlashPacks.objects.create(author = request.user, name = request.data['name'], category = 'to be replaced')
    pack.save()
    serializer = FlashPackSerializer(pack, many = False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createCard(request):
    card = FlashCard.objects.create(answer = request.data['answer'], question = request.data['question'])
    card.save
    flash = FlashPacks.objects.get(id = request.data['packId'])
    flash.cards.add(card)
    serializer = FlashSerializer(card, many = False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getFlash(request, pk):
    if pk == 'false':
        user = request.user
        pack = user.flashpacks_set.all()
    elif pk  == 'true':
        pack = FlashPacks.objects.all()
    serializer = FlashPackSerializer(pack, many = True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def flashCards(request, pk):
    flashpack = FlashPacks.objects.get(id = pk)
    pack = flashpack.cards.all()
    serializer = FlashSerializer(pack, many = True)
    return Response(serializer.data)
    
def flashpack(request):
    pass


