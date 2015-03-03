from django import forms

class ContactForm(forms.Form):
  """
  define a contact form class
  """
  # this will be rendered like
  # <input class="form-control" id="id_subject" name="subject" size="48" type="text">
  # valid if not empty
  subject = forms.CharField(widget=forms.TextInput(attrs={'size':'48', 'class':'form-control'}))
  # A CharField that checks that the value is a valid email address.
  email = forms.EmailField(widget=forms.TextInput(attrs={'size':'48', 'class':'form-control'}))
  message = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows': 5 , 'class':'form-control'}))


#该代码片段来自于: http://www.sharejs.com/codes/python/8848
