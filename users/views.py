from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import CustomUserSerializer
from .models import CustomUser


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.AllowAny]
        elif self.action == 'list':
            self.permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
        return super(CustomUserViewSet, self).get_permissions()


class CustomAuthToken(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.pk,
            'email': user.email
        })


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
