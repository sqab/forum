from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

from .models import Post
from .models import CommentPost


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
        }


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "registration/signup.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
