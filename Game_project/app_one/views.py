from django.shortcuts import render
from random import randint
secret_number = randint(0, 100)
success = False
count =0
def index(request):
    global secret_number, success, count
    Message = ''
    guessNumber = None
    if request.method == 'POST' and request.POST.get('guessNumber'):
        guessNumber = int(request.POST['guessNumber'])
        count+=1
        if guessNumber == secret_number:
            success = True
        else:
            if(guessNumber > secret_number):
                Message = 'lower'
            else:
                Message = 'higher'
        
    else:
        secret_number = randint(0,100)
        success = False
        Message = ''
        guessNumber = None
        count=0
    context = {
    'success': success,
    'Message' : Message,
    'guessNumber': guessNumber,
    'secret_number': secret_number,
    'count': count
    }
    return render(request, 'index.html', context)