from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import views, status
from rest_framework.response import Response

class PasswordResetConfirmView(views.APIView):
    def get(self, request, uidb64, token):
        try:
            # Decode uidb64 to get user ID
            user_id = force_text(urlsafe_base64_decode(uidb64))

            # Retrieve user based on user ID
            user = get_user_model().objects.get(pk=user_id)

            # Check if the token is valid
            if PasswordResetTokenGenerator().check_token(user, token):
                # Token is valid, you can implement your password reset logic here
                # For example, you might return a success message
                return Response({'detail': 'Password reset successful'}, status=status.HTTP_200_OK)
            else:
                # Token is invalid
                return Response({'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            # Handle exceptions such as invalid uidb64 or user not found
            return Response({'detail': 'Invalid user or token'}, status=status.HTTP_400_BAD_REQUEST)
