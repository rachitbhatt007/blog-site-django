from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ("post",)

        labels = {
            "username": "Your Name",
            "email": "Your Email",
            "text": "Comment"
        }
