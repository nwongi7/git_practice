import webbrowser

# 1. 사용자의 입력을 받아 검색하기 
# keyword = input("검색어를 입력해 주세요: ")

# 모모랜드 모든 멤버들의 검색 페이지를 한 번에 여는 코드
url = "https://search.daum.net/search?q="

momo = ["나윤", "혜빈", "아인", "낸시", "주이", "연우", "제인", "데이지", "태하"]

# momo라고 하는 리스트를 한 번 씩 돌면서, 웹 브라우저를 연다.
for myGirl in momo:
    webbrowser.open(url + myGirl)

"https://search.daum.net/search?w=tot&q=%EC%97%B0%EC%9A%B0"