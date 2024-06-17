from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from api.serializers.account_serializer import AccountSerializer

@api_view(['POST'])
def sign_in(request):
  if request.method == 'POST':
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
      instance = serializer.save()
      return Response(serializer.to_representation(instance), status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  else:
    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def login(request):
  if request.method == 'POST':
    serializer = AccountSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      account = serializer.authenticate(serializer.validated_data)
      token = AccessToken.for_user(account)
      return Response({'token': str(token)}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  else:
    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def refresh_token(request):
  if request.method == 'POST':
    token = RefreshToken.for_user(request.user)
    return Response({'token': str(token)}, status=status.HTTP_200_OK)