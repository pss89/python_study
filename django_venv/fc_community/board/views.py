from django.shortcuts import render
from .models import Board
# Create your views here.

def board_list(request):
    # board 모델에서 정렬해서 모든 목록을 가져오는 코드
    boards = Board.objects.all().order_by('-id')
    return render(request,'board_list.html',{'boards':boards})