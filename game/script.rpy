# 캐릭터 정의
define c = Character("김춘배")
define j = Character("윤지아")
define s = Character("연살")


# 변수 정의



# 아이템/오브젝트 이미지 정의



# 배경 이미지 정의
image bg festival = "images/backgrounds/festival"
image bg alley = "images/backgrounds/alley"
image bg cellar = "images/backgrounds/cellar"
image bg corridor_1 = "images/backgrounds/corridor_1"
image bg dining_room = "images/backgrounds/dining_room"
image bg kitchen = "images/backgrounds/kitchen"
image bg restroom = "images/backgrounds/restroom"
image bg dark_room_1 = "images/backgrounds/dark_room_1"
image bg corridor_2 = "images/backgrounds/corridor_2"
image bg terrace = "images/backgrounds/terrace"
image bg bedroom = "images/backgrounds/bedroom"
image bg dark_room_2 = "images/backgrounds/dark_room_2"
image rooftop = "images/backgrounds/rooftop"
image exit = "images/backgrounds/exit"


# 스크린 정의



# 스크립트 시작 ----------------------------------------------
label start:
    jump Festival

label Festival:
    scene bg festival

    c "(내는 김춘배, 평범한 회사원이다.)"
    c "(오늘은 회사 동료인 지아 씨와 함께 벚꽃 축제에 다녀왔다.)"
    j "춘배 씨!"
    c "예, 예...?"
    j "이렇게 헤어지기 아쉬운데, 저희 집에서 영화라도 보고 가실래요?"
    c "그거 좋구나."
    j "아하핫! 역시 춘배 씨는 재밌는 분이씨네요!"
    c "(지아 씨와 단둘이 영화라니... 정말 기대돼.)"
    j "저는 할 게 있어서 먼저 가 있을게요."
    j "주소 보내드릴 테니까 이따 만나요!"

    jump Alley

label Alley:

