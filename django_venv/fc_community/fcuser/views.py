from django.http import HttpResponse # 백엔드에서 데이터 예외처리 시 사용하는 라이브러리
from django.shortcuts import render, redirect # view페이지 리터을 위한 라이브러리
from django.contrib.auth.hashers import make_password, check_password # 평문으로 넘어오는 password를 암호화하여 처리하기 위함
from .models import Fcuser
from .forms import LoginForm
# Create your views here.

# home 추가
def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)

    return HttpResponse('HOME!')

# login 함수 추가
def login(request):

    # forms.py 사용 안할 때
    # if request.method == 'GET':
    #     return render(request,'login.html')
    # elif request.method == 'POST':
    #     username = request.POST.get('username',None)
    #     password = request.POST.get('password',None)

    #     res_data = {}
    #     if not (username and password):
    #         res_data['error'] = '모든 값을 입력해야합니다.'
    #     else:
    #         # 필드명의 값을 체크하여 가져오기
    #         fcuser = Fcuser.objects.get(username=username)
    #         if check_password(password,fcuser.password):
    #             # 로그인 처리
    #             # pass
    #             # 세션 & 리다이렉트 처리
    #             request.session['user'] = fcuser.id
    #             return redirect('/')
    #         else:
    #             # 로그인 실패
    #             res_data['error'] = '비밀번호를 틀렸습니다.'


    # form = LoginForm()

    # return render(request,'login.html',res_data)
    # return render(request, 'login.html', {'form':form})

    # forms.py 사용할 떄 
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): # 이미 검증 한 상태
            # session
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form':form})

# logout 함수 추가
def logout(request):
    if request.session.get('user'):
        # 있으면 삭제
        del(request.session['user'])

    return redirect('/')

# register 함수 추가
def register(request):
    # return render(request, 'folder1/folder2/register.html')
    # request를 받아서 register.html 파일을 랜더링 하겠다는 의미
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        # 값이 있으면 true, 없으면 공백으로 처리
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail',None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        # 응답값을 view페이지에 넘겨주기 위함
        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다'
        elif password != re_password:
            # return HttpResponse('비밀번호가 다릅니다')
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )

            fcuser.save()

        return render(request, 'register.html', res_data)