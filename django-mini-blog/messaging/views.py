from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Message
from .forms import MessageForm


@login_required
def inbox(request):
    messages_received = Message.objects.filter(receiver=request.user).order_by('-created_at')
    return render(request, 'messaging/inbox.html', {'messages_received': messages_received})


@login_required
def sent_messages(request):
    messages_sent = Message.objects.filter(sender=request.user).order_by('-created_at')
    return render(request, 'messaging/sent_messages.html', {'messages_sent': messages_sent})


@login_required
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)

    if message.receiver != request.user and message.sender != request.user:
        return redirect('inbox')

    return render(request, 'messaging/message_detail.html', {'message': message})


@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        form.fields['receiver'].queryset = User.objects.exclude(id=request.user.id)

        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
        form.fields['receiver'].queryset = User.objects.exclude(id=request.user.id)

    return render(request, 'messaging/send_message.html', {'form': form})