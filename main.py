import sys

print("어서오세요(✿ ^~^)❤")
골라=input("[커피 / 쥬스 / 에이드] 중에 메뉴를 선택해 주세요")

#가격
bean_menu = {"브라질":200, "케냐":800, "콜롬비아":500, "에티오피아":1000,"하우스블렌드":0}
coffee_menu = {"아메리카노":4100, "라떼":4600, "돌체라떼":5600, "바닐라라떼":5100,"화이트 초코모카":5800}
juice = {"딸기":1500,"바나나":1000,"망고":2000,"키위":1200,"블루베리":800,"오렌지":500}
ade_menu = {"레몬에이드":5100, "청포도에이드":5500, "자몽에이드":5800}

#메뉴선택
while True : 
 if 골라 =='커피' :
    print("아래 커피메뉴 중 선택해주세요")
    coffee = input("[아메리카노 / 라떼 / 돌체라떼 / 바닐라라떼 / 화이트 초코모카] : ")
    while True :
      if coffee == '아메리카노' :
       break
      if coffee == '라떼' :
       break
      if coffee == '돌체라떼' :
       break
      if coffee == '바닐라라떼' :
       break
      if coffee == '화이트 초코모카' :
       break
      else :
       coffee = input("다시 골라주세요")
    print("원두를 고르세요")
    bean = input("[브라질 / 케냐 / 콜롬비아 / 에티오피아 / 하우스블렌드] : ")
    while True :
      if bean == '브라질' :
       break
      if bean == '케냐' :
       break
      if bean == '콜롬비아' :
       break
      if bean == '에티오피아' :
       break
      if bean == '하우스블렌드' :
       break
      else :
        bean = input("다시 골라주세요")
    print("가격 :", coffee_menu[coffee] + bean_menu[bean])
    break

 elif 골라 =='쥬스' :
  print("아래 과일 중 고르세요")
  fruit = input("[딸기 / 바나나 / 망고 / 키위 / 블루베리 / 오렌지] : ")
  while True :
      if fruit == '딸기' :
       break
      if fruit == '바나나' :
       break
      if fruit == '망고' :
       break
      if fruit == '키위' :
       break
      if fruit == '블루베리' :
       break
      if fruit == '오렌지' :
       break
      else :
        fruit = input("다시 골라주세요")
  print("한가지 더 고르세요")
  fruit2 = input("[딸기 / 바나나 / 망고 / 키위 / 블루베리 / 오렌지] : ")
  while True :
      if fruit2 == '딸기' :
       break
      if fruit2 == '바나나' :
       break
      if fruit2 == '망고' :
       break
      if fruit2 == '키위' :
       break
      if fruit2 == '블루베리' :
       break
      if fruit2 == '오렌지' :
       break
      else :
       fruit2 = input("다시 골라주세요")
  print("가격 : ", juice[fruit] + juice[fruit2])
  break

 elif 골라 =='에이드' :
  print("아래 중 고르세요")
  ade = input("[레몬에이드 / 청포도에이드 / 자몽에이드] : ")
  while True :
      if ade == '레몬에이드' :
       break
      if ade == '청포도에이드' :
       break
      if ade == '자몽에이드' :
       break
      else :
         ade = input("다시 골라주세요")
  print("가격 : ", ade_menu[ade])
  break

 else :
  골라 = input("다시 고르세요")
    
#결제
결제=input("결제하시겠습니까? (Y/N)").upper()
while True : 
 if 결제=="Y" :
  print("감사합니다 또 오세요")
  break
 elif 결제=="N" :
  print("안녕히가세요")
  break
 else :
  결제=input("(Y/N)로만 입력하세요").upper()