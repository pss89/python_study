from django.db import models

# Create your models here.

# 장고에서 import 한 model을 상속받아야 한다
class Board(models.Model):
    title = models.CharField(max_length=128,
                                verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    # fcuser db의 fcuser와 연결 시키겠다
    # cascade fcuser 정보가 삭제되면 해당 모델에서도 삭제를 하겠다
    writer = models.ForeignKey('fcuser.fcuser',on_delete=models.CASCADE,
                                verbose_name='작성자')
    registered_dttm = models.DateTimeField(auto_now_add=True, # 등록 시 자동으로 시간이 저장되는 부분
                                            verbose_name='등록시간')

    # 문자열 변환 내장 함수
    def __str__(self):
        return self.title

    class Meta: # 테이블 명을 지정하는 부분
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글' # 별칭
        verbose_name_plural = '패스트캠퍼스 게시글' # 복수형 명칭