# 공공 API 데이터 분석
---

### 특징

- 서울시 생필품 농수축산물 가격 정보


- 서울시 물가모니터가 주1회 자치구별 전통시장과 대형마트에 나가 농수축산물 16개 품목을 조사하고 그 가격을 공개하는 정보입니다.


- 관련 태그

    물가 ,  농업 ,  수산업 ,  축산업 ,  전통시장 ,  대형마트 ,  갈치 ,  고등어 ,  달걀 ,  닭고기 ,  동태 ,  돼지고기 ,  명태 ,  무 ,  배 ,  배추 ,  사과 ,  삼겹살 ,  상추 ,  쇠고기 ,  애호박 ,  양파 ,  오이 ,  오징어 ,  조기 ,  호박
    
- 업데이트 주기: 1주일, 토요일 오전


- 한번에 최대 1,000건 호출 가능


- 전체 데이터 수는 오픈 API의 `list_total_count` 항목을 확인
    - (2022.05.12 기준) - 370,899건

## 가격 조사 전통시장 및 대형마트 목록 (2022.06.09 기준)

---
종로구: 광장시장, 통인시장, 롯데백화점 명동본점, 신세계백화점 본점


중구: 서울중앙시장, 남대문시장, 이마트 청계천점, 롯데마트 서울역점


용산구: 후암시장, 용문시장, 농협하나로마트 용산점, 이마트 용산점


성동구: 금남시장, 뚝도시장, 이마트 성수점, 이마트 왕십리점


광진구: 노룬산골목시장, 자양골목시장, 롯데마트 강변점, 이마트 자양점


동대문구: 경동시장, 청량리종합시장, 롯데백화점 청량리점, 홈플러스 동대문점


중랑구: 동원시장, 우림시장, 홈플러스 면목점, 이마트 상봉점


성북구: 장위전통시장, 돈암제일시장, 현대백화점 미아점, 이마트 미아점


강북구: 숭인시장, 수유재래시장, 농협하나로마트 미아점, 롯데백화점 미아점


도봉구: 신창시장, 방학동 도깨비시장, 이마트 창동점, 홈플러스 방학점


노원구: 상계중앙시장, 공릉동 도깨비시장, 홈플러스 중계점, 롯데백화점 노원점


은평구: 대조시장, 대림시장, 이마트 은평점, NC백화점 불광점


서대문구: 독립문영천시장, 인왕시장, 롯데슈퍼 유진점, 현대백화점 신촌점


마포구: 망원시장, 마포농수산물시장, 농협하나로마트 신촌점, 홈플러스 월드컵점


양천구: 신영시장, 목3동시장, 홈플러스 목동점, 이마트 목동점


강서구: 화곡본동시장, 송화시장, 이마트 가양점, 홈플러스 익스프레스 등촌점


구로구: 남구로시장, 고척근린시장, 이마트 신도림점, NC백화점 신구로점


금천구: 별빛남문시장, 현대시장, 홈플러스 독산점, 홈플러스 시흥점


영등포구: 영등포 전통시장, 대림중앙시장, 이마트 여의도점, 홈플러스 영등포점


동작구: 남성시장, 관악신사시장, 이마트 이수점, 롯데백화점 영등포점


관악구: 신원시장, 원당종합시장, 롯데백화점 관악점, 세이브마트 신림본점


서초구: 방배종합시장, 신세계백화점 강남점, 뉴코아아울렛 강남점, 농협하나로마트 양재점


강남구: 청담삼익시장, 도곡시장, 롯데백화점 강남점, 이마트 역삼점


송파구: 방이시장, 마천중앙시장, 홈플러스 잠실점, 롯데백화점 잠실점


강동구: 둔촌역전통시장, 암사종합시장, 홈플러스 강동점, 이마트 명일점


```python
import os

os.listdir('../')
```




    ['.gitignore',
     'app.py',
     'config.py',
     'crawler.py',
     'data',
     'models.py',
     'notebook',
     'papi',
     'requirements.txt',
     'run_server.sh',
     'util',
     '__pycache__']



## 샘플 데이터


```python
json_data_path = "../data/sample.json"
```


```python
import json

with open(json_data_path, 'rb') as f:
    data = json.load(f)
```


```python
import pandas as pd

json_data = data['ListNecessariesPricesService']['row']

df = pd.DataFrame(json_data)
```


```python
df[:10]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ADD_COL</th>
      <th>A_NAME</th>
      <th>A_PRICE</th>
      <th>A_SEQ</th>
      <th>A_UNIT</th>
      <th>M_GU_CODE</th>
      <th>M_GU_NAME</th>
      <th>M_NAME</th>
      <th>M_SEQ</th>
      <th>M_TYPE_CODE</th>
      <th>M_TYPE_NAME</th>
      <th>P_DATE</th>
      <th>P_SEQ</th>
      <th>P_YEAR_MONTH</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>국내산</td>
      <td>사과(부사, 300g)</td>
      <td>1000</td>
      <td>305.0</td>
      <td>1개(300g)</td>
      <td>560000</td>
      <td>영등포구</td>
      <td>대림중앙시장</td>
      <td>19.0</td>
      <td>001</td>
      <td>전통시장</td>
      <td>2022-06-16</td>
      <td>1759389.0</td>
      <td>2022-06</td>
    </tr>
    <tr>
      <th>1</th>
      <td>국내산</td>
      <td>배(신고, 600g)</td>
      <td>2000</td>
      <td>306.0</td>
      <td>1개(600g)</td>
      <td>560000</td>
      <td>영등포구</td>
      <td>대림중앙시장</td>
      <td>19.0</td>
      <td>001</td>
      <td>전통시장</td>
      <td>2022-06-16</td>
      <td>1759390.0</td>
      <td>2022-06</td>
    </tr>
    <tr>
      <th>2</th>
      <td>국내산</td>
      <td>배추</td>
      <td>3500</td>
      <td>26.0</td>
      <td>1포기(2.5kg)</td>
      <td>560000</td>
      <td>영등포구</td>
      <td>대림중앙시장</td>
      <td>19.0</td>
      <td>001</td>
      <td>전통시장</td>
      <td>2022-06-16</td>
      <td>1759391.0</td>
      <td>2022-06</td>
    </tr>
    <tr>
      <th>3</th>
      <td>국내산</td>
      <td>무(1kg)</td>
      <td>1500</td>
      <td>308.0</td>
      <td>1개(1kg)</td>
      <td>560000</td>
      <td>영등포구</td>
      <td>대림중앙시장</td>
      <td>19.0</td>
      <td>001</td>
      <td>전통시장</td>
      <td>2022-06-16</td>
      <td>1759392.0</td>
      <td>2022-06</td>
    </tr>
    <tr>
      <th>4</th>
      <td>국내산 /1망(1.8kg) 3,500원</td>
      <td>양파</td>
      <td>2917</td>
      <td>24.0</td>
      <td>1.5kg</td>
      <td>560000</td>
      <td>영등포구</td>
      <td>대림중앙시장</td>
      <td>19.0</td>
      <td>001</td>
      <td>전통시장</td>
      <td>2022-06-16</td>
      <td>1759393.0</td>
      <td>2022-06</td>
    </tr>
    <tr>
      <th>5</th>
      <td>국내산</td>
      <td>상추(100g)</td>
      <td>750</td>
      <td>310.0</td>
      <td>100g</td>
      <td>560000</td>
      <td>영등포구</td>
      <td>대림중앙시장</td>
      <td>19.0</td>
      <td>001</td>
      <td>전통시장</td>
      <td>2022-06-16</td>
      <td>1759394.0</td>
      <td>2022-06</td>
    </tr>
    <tr>
      <th>6</th>
      <td>국내산</td>
      <td>오이</td>
      <td>666</td>
      <td>22.0</td>
      <td>1개(100g)</td>
      <td>560000</td>
      <td>영등포구</td>
      <td>대림중앙시장</td>
      <td>19.0</td>
      <td>001</td>
      <td>전통시장</td>
      <td>2022-06-16</td>
      <td>1759395.0</td>
      <td>2022-06</td>
    </tr>
    <tr>
      <th>7</th>
      <td>국내산</td>
      <td>애호박</td>
      <td>1500</td>
      <td>312.0</td>
      <td>1개(200g)</td>
      <td>560000</td>
      <td>영등포구</td>
      <td>대림중앙시장</td>
      <td>19.0</td>
      <td>001</td>
      <td>전통시장</td>
      <td>2022-06-16</td>
      <td>1759396.0</td>
      <td>2022-06</td>
    </tr>
    <tr>
      <th>8</th>
      <td>한우 설도 1+</td>
      <td>쇠고기(한우,불고기)</td>
      <td>6280</td>
      <td>58.0</td>
      <td>100g</td>
      <td>560000</td>
      <td>영등포구</td>
      <td>대림중앙시장</td>
      <td>19.0</td>
      <td>001</td>
      <td>전통시장</td>
      <td>2022-06-16</td>
      <td>1759397.0</td>
      <td>2022-06</td>
    </tr>
    <tr>
      <th>9</th>
      <td>국내산 삼겹살</td>
      <td>돼지고기(생삼겹살)</td>
      <td>2880</td>
      <td>99.0</td>
      <td>100g</td>
      <td>560000</td>
      <td>영등포구</td>
      <td>대림중앙시장</td>
      <td>19.0</td>
      <td>001</td>
      <td>전통시장</td>
      <td>2022-06-16</td>
      <td>1759398.0</td>
      <td>2022-06</td>
    </tr>
  </tbody>
</table>
</div>



# 피쳐 목록

```
공통	list_total_count	총 데이터 건수 (정상조회 시 출력됨)
공통	RESULT.CODE	요청결과 코드 (하단 메세지설명 참고)
공통	RESULT.MESSAGE	요청결과 메시지 (하단 메세지설명 참고)

1	P_SEQ	일련번호
2	M_SEQ	시장/마트 번호
3	M_NAME	시장/마트 이름
5	A_SEQ	품목 번호
6	A_NAME	품목 이름
7	A_UNIT	실판매규격
8	A_PRICE	가격(원)
9	P_YEAR_MONTH	년도-월
10	ADD_COL	비고
11	P_DATE	점검일자
12	M_TYPE_CODE	시장유형 구분 코드
13	M_TYPE_NAME	시장유형 구분 이름
14	M_GU_CODE	자치구 코드
15	M_GU_NAME	자치구 이름
```

## 총 데이터 건수

- list_total_count
- type : int


```python
# 총 데이터 건수
data['ListNecessariesPricesService']['list_total_count']
```




    379194




```python
# 모든 row 데이터 정보

total_info = data['ListNecessariesPricesService']['row']
```


```python
# 데이터는 1000개씩 호출할 수 있다
len(total_info)
```




    1000



## 일련번호

- P-SEQ
- 일련번호 순서가 불규칙하다.
- type: float


```python
for i in range(10):
    print(f"{i+1}번째 데이터의 일련번호 : {int(total_info[i]['P_SEQ'])}")
        
print("---------------------------------------------------------")

for i in range(len(total_info) - 10, len(total_info)):
    print(f"{i+1}번째 데이터의 일련번호 : {int(total_info[i]['P_SEQ'])}")
    
print(type(total_info[i]['ADD_COL']))
```

    1번째 데이터의 일련번호 : 1759389
    2번째 데이터의 일련번호 : 1759390
    3번째 데이터의 일련번호 : 1759391
    4번째 데이터의 일련번호 : 1759392
    5번째 데이터의 일련번호 : 1759393
    6번째 데이터의 일련번호 : 1759394
    7번째 데이터의 일련번호 : 1759395
    8번째 데이터의 일련번호 : 1759396
    9번째 데이터의 일련번호 : 1759397
    10번째 데이터의 일련번호 : 1759398
    ---------------------------------------------------------
    991번째 데이터의 일련번호 : 1758411
    992번째 데이터의 일련번호 : 1758738
    993번째 데이터의 일련번호 : 1758139
    994번째 데이터의 일련번호 : 1758178
    995번째 데이터의 일련번호 : 1758739
    996번째 데이터의 일련번호 : 1758110
    997번째 데이터의 일련번호 : 1758412
    998번째 데이터의 일련번호 : 1758740
    999번째 데이터의 일련번호 : 1758103
    1000번째 데이터의 일련번호 : 1758105
    

## 시장/마트 번호

- M-SEQ
- 시장/마트 번호를 분류하는 키
- type: float


```python
# 시장/마트 번호

for i in range(10):
    print(total_info[i]['M_SEQ'])
    
print(type(total_info[i]['M_SEQ']))
```

    19.0
    19.0
    19.0
    19.0
    19.0
    19.0
    19.0
    19.0
    19.0
    19.0
    <class 'float'>
    

# 품목 번호

- A-SEQ
- 품목별로 고유 값
- type : float


```python
for i in range(10):
    print(f"품목번호: {total_info[i]['A_SEQ']}")
    
print(type(total_info[i]['A_SEQ']))
```

    품목번호: 305.0
    품목번호: 306.0
    품목번호: 26.0
    품목번호: 308.0
    품목번호: 24.0
    품목번호: 310.0
    품목번호: 22.0
    품목번호: 312.0
    품목번호: 58.0
    품목번호: 99.0
    <class 'float'>
    

## 품목 이름

- A_NAME
- type: str


```python
for i in range(10):
    print(f"품목이름: {total_info[i]['A_NAME']}")
    
print(type(total_info[i]['A_NAME']))
```

    품목이름: 사과(부사, 300g)
    품목이름: 배(신고, 600g)
    품목이름: 배추
    품목이름: 무(1kg)
    품목이름: 양파
    품목이름: 상추(100g)
    품목이름: 오이
    품목이름: 애호박
    품목이름: 쇠고기(한우,불고기)
    품목이름: 돼지고기(생삼겹살)
    <class 'str'>
    

# 실판매규격

- A_UNIT
- type: str


```python
for i in range(10):
    print(f"실판매규격: {total_info[i]['A_UNIT']}")
    
print(type(total_info[i]['A_UNIT']))
```

    실판매규격: 1개(300g)
    실판매규격: 1개(600g)
    실판매규격: 1포기(2.5kg)
    실판매규격: 1개(1kg)
    실판매규격: 1.5kg
    실판매규격: 100g
    실판매규격: 1개(100g)
    실판매규격: 1개(200g)
    실판매규격: 100g
    실판매규격: 100g
    <class 'str'>
    

# 가격(원)

- A_PRICE
- type: str


```python
for i in range(10):
    print(f"가격(원): {total_info[i]['A_PRICE']}")
    
print(type(total_info[i]['A_PRICE']))
```

    가격(원): 1000
    가격(원): 2000
    가격(원): 3500
    가격(원): 1500
    가격(원): 2917
    가격(원): 750
    가격(원): 666
    가격(원): 1500
    가격(원): 6280
    가격(원): 2880
    <class 'str'>
    

# 년도-월

- P_YEAR_MONTH
- type: str


```python
for i in range(10):
    print(f"년도-월: {total_info[i]['P_YEAR_MONTH']}")
    
print(type(total_info[i]['P_YEAR_MONTH']))
```

    년도-월: 2022-06
    년도-월: 2022-06
    년도-월: 2022-06
    년도-월: 2022-06
    년도-월: 2022-06
    년도-월: 2022-06
    년도-월: 2022-06
    년도-월: 2022-06
    년도-월: 2022-06
    년도-월: 2022-06
    <class 'str'>
    

# 비고

- 무슨 용도로 사용되는지 아직 잘 모르겠음
- ADD_COL
- type: str


```python
for i in range(10):
    print(f"비고: {total_info[i]['ADD_COL']}")
    
print(type(total_info[i]['ADD_COL']))
```

    비고: 국내산 
    비고: 국내산 
    비고: 국내산 
    비고: 국내산 
    비고: 국내산 /1망(1.8kg) 3,500원
    비고: 국내산 
    비고: 국내산 
    비고: 국내산 
    비고: 한우 설도 1+
    비고: 국내산 삼겹살 
    <class 'str'>
    

# 점검일자

- 물가조사 날짜
- P_DATE
- type : str


```python
for i in range(10):
    print(f"점검일자: {total_info[i]['P_DATE']}")

print(type(total_info[i]['P_DATE']))
```

    점검일자: 2022-06-16
    점검일자: 2022-06-16
    점검일자: 2022-06-16
    점검일자: 2022-06-16
    점검일자: 2022-06-16
    점검일자: 2022-06-16
    점검일자: 2022-06-16
    점검일자: 2022-06-16
    점검일자: 2022-06-16
    점검일자: 2022-06-16
    <class 'str'>
    

# 시장유형 구분 코드


```python
for i in range(10):
    print(f"시장유형 구분 코드: {total_info[i]['M_TYPE_CODE']}")
    
print(type(total_info[i]['M_TYPE_CODE']))
```

    시장유형 구분 코드: 001
    시장유형 구분 코드: 001
    시장유형 구분 코드: 001
    시장유형 구분 코드: 001
    시장유형 구분 코드: 001
    시장유형 구분 코드: 001
    시장유형 구분 코드: 001
    시장유형 구분 코드: 001
    시장유형 구분 코드: 001
    시장유형 구분 코드: 001
    <class 'str'>
    

# 시장유형 구분 이름


```python
for i in range(10):
    print(f"시장유형 구분 이름: {total_info[i]['A_NAME']}")
    
print(type(total_info[i]['A_NAME']))
```

    시장유형 구분 이름: 사과(부사, 300g)
    시장유형 구분 이름: 배(신고, 600g)
    시장유형 구분 이름: 배추
    시장유형 구분 이름: 무(1kg)
    시장유형 구분 이름: 양파
    시장유형 구분 이름: 상추(100g)
    시장유형 구분 이름: 오이
    시장유형 구분 이름: 애호박
    시장유형 구분 이름: 쇠고기(한우,불고기)
    시장유형 구분 이름: 돼지고기(생삼겹살)
    <class 'str'>
    

# 자치구 코드


```python
for i in range(10):
    print(f"자치구 코드: {total_info[i]['M_GU_CODE']}")
    
print(type(total_info[i]['M_GU_CODE']))
```

    자치구 코드: 560000
    자치구 코드: 560000
    자치구 코드: 560000
    자치구 코드: 560000
    자치구 코드: 560000
    자치구 코드: 560000
    자치구 코드: 560000
    자치구 코드: 560000
    자치구 코드: 560000
    자치구 코드: 560000
    <class 'str'>
    

# 자치구 이름


```python
for i in range(10):
    print(f"자치구 이름: {total_info[i]['M_GU_NAME']}")
    
print(type(total_info[i]['M_GU_NAME']))
```

    자치구 이름: 영등포구
    자치구 이름: 영등포구
    자치구 이름: 영등포구
    자치구 이름: 영등포구
    자치구 이름: 영등포구
    자치구 이름: 영등포구
    자치구 이름: 영등포구
    자치구 이름: 영등포구
    자치구 이름: 영등포구
    자치구 이름: 영등포구
    <class 'str'>
    


```python

```
