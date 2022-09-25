'Practice04-01(도전! 프로그래밍04-01)'
''' 다음을 참고해 월(month)을 표준 입력으로 입력받아
계절을 출력하는 프로그램을 작성하시오.
봄: 4, 5월, 여름: 6, 7, 8월, 가을: 9, 10월, 겨울: 11, 12, 1, 2, 3월 '''

month = int(input('월 입력 ? '))

if month==4 or month==5:
    season = '봄'
    print('%d월 %s' % (month, season))  
    
if month==6 or month==7 or month==8:
    season = '여름'
    print('%d월 %s' % (month, season)) 
 
if month==9 or month==10:
    season = '가을'
    print('%d월 %s' % (month, season)) 

if month==11 or month==12 or month==1 or month==2 or month==3:
    season = '겨울'
    print('%d월 %s' % (month, season)) 


