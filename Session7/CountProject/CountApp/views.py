from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text=request.POST['text']
    total_len=len(text)
    len_without_space=len(text.replace(' ', ''))
    count_words=len(text.split(' '))
    return render(request, 'result.html', {'text':text, 
                                           'total_len':total_len, 
                                           'len_without_space':len_without_space, 
                                           'count_words':count_words, })