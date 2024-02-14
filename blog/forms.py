from django.forms import ModelForm,forms
from .models import *
# from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from bootstrap_datepicker_plus.widgets import DateTimePickerInput,TimePickerInput


class AddBlogForm(ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title','body','picture',]

class AddCommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']