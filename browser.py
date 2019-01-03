import webbrowser

# 모모랜드 모든 멤버들의 검색 페이지를 한번에 여는 코드
#keyword = input("검색어를 입력해 주세요: ")

momo = ["혜빈", "연우", "제인", "태하", "나윤", "데이지", "아인", "주이", "낸시"]
url = "https://search.daum.net/search?q="

for mem in momo:
    webbrowser.open(url+mem)
