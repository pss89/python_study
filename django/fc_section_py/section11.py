# section11
# 파이썬 외부파일 처리
# 파이썬 엑셀, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv (콤마로 구분 된 파일-무조건 콤마는 아님)

import csv

# 예제1
with open('../resource/sample1.csv','r') as f:
    reader = csv.reader(f)
    #next(reader) #컬럼명 제외(Header 스킵)

    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)

print()

# 예제2
with open('../resource/sample2.csv','r') as f:
    reader = csv.reader(f, delimiter='|') #구분자를 기준으로 list형태로 변환해준다
    #next(reader) #컬럼명 제외(Header 스킵)

    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)

print()

#예제3 (Dict 변환)
with open('../resource/sample1.csv','r') as f:
    #딕셔너리 형태로 읽어온다
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            # if k == '나이':
            #     print(k,v)
            # else:
            #     print(k,v,end=' / ')
            print(k, v)
        print('---------------')
        # print()

#예제4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('../resource/sample3.csv','w',newline='') as f: #newline = 새줄은 어떻게 처리 할것이냐
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

#예제5 (한번에 쓰기)
with open('../resource/sample4.csv','w',newline='') as f: #newline = 새줄은 어떻게 처리 할것이냐
    wt = csv.writer(f)
    wt.writerows(w)

#XSL, XLSX
#openpyxl, xlsxwriter, xlrd, xlwt, xlutils
#pandas 를 주로 사용(openpyxl, xlrd 내부적으로 사용)
#pip install xlrd
#pip install openpyxl
#pip install pandas

#예제6
import pandas as pd

#옵션 : sheetname='시트명' 또는 숫자, header=3, skiprows=숫자
xlsx = pd.read_excel('../resource/sample.xlsx')

print(xlsx)
print(type(xlsx))

for k,v in xlsx.items():
    print(k,v)

#상위 데이터 확인
print(xlsx.head()) #0~5까지
print()

#데이터 확인
print(xlsx.tail()) #끝부분
print()

#데이터 확인
print(xlsx.shape) #행, 열

#엑셀 or csv 다시 쓰기
# xlsx.to_excel('./resource/result.xlsx',index=False)
# xlsx.to_csv('./resource/result.csv',index=False)