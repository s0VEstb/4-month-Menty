from django import forms
from cars.models import Post, Review


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'brand', 'model', 'price', 'year_of_issue', 'img']
        
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']