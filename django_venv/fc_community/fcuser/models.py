from django.db import models

# Create your models here.

# 장고에서 import 한 model을 상속받아야 한다
class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')
    useremail = models.EmailField(max_length=128,
                                verbose_name='사용자이메일')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, # 등록 시 자동으로 시간이 저장되는 부분
                                            verbose_name='등록시간')

    # 문자열 변환 내장 함수
    def __str__(self):
        return self.username

    class Meta: # 테이블 명을 지정하는 부분
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자' # 별칭
        verbose_name_plural = '패스트캠퍼스 사용자' # 복수형 명칭