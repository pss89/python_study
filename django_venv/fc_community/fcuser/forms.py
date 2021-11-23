from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required':'아이디를 입력해주세요.'
        },
        max_length=32,label='사용자 이름')
    password = forms.CharField(
        error_messages={
            'required':'비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput,label='비밀번호')

    def clean(self):
        cleaned_data = super().clean() #form 안에있는 clean 함수 실행

        # 값이 있으면 변수에 저장
        username = cleaned_data.get('username') 
        password = cleaned_data.get('password')

        # 두개의 변수 체크
        if username and password:
            # 검증처리
            fcuser = Fcuser.objects.get(username=username)
            if not check_password(password, fcuser.password):
                # forms 안에 기본적인 에러 함수
                self.add_error('password','비밀번호를 틀렸습니다')
            else:
                self.user_id = fcuser.id