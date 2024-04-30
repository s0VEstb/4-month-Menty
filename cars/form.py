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

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['text']

#     user = None  # Добавляем атрибут user

#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         instance.user = self.user  # Устанавливаем пользователя для отзыва
#         if commit:
#             instance.save()
#         return instance