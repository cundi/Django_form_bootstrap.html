from django.shortcuts import render
from .forms import ContactForm

def contact(request):
  if request.method == 'POST':
    # get data from POST request to contactform
    # http://www.sharejs.com
    form = ContactForm(request.POST)
  else:
    form = ContactForm()
  
  data = {
    'form': form,
  }
  return render(request, 'contact_form.html', data)
