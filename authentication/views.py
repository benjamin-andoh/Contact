import jwt
from django.contrib import auth
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from authentication.serializers import UserSerializer, LoginSerializer


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        creating_user = UserSerializer(data=request.data)
        if creating_user.is_valid():
            creating_user.save()
            return Response(creating_user.data, status=status.HTTP_201_CREATED)
        return Response(creating_user.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')

        user = auth.authenticate(username=username, password=password)
        if user:
            auth_token = jwt.encode(
                {'username': user.username}, 'dst364qw7j27ik2w47q46q')

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}
            return Response(data, status=status.HTTP_201_CREATED)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
