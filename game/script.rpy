# 캐릭터 정의 ------------------------------------------------------------
define c = Character('김춘배')
define j = Character('윤지아')
define y = Character('연살')

# 변수 정의 --------------------------------------------------------------
default Key = False
default MasterKey = False
default HaveMP3 = False
default Coin = False

# 이미지 정의 ------------------------------------------------------------



# 시작 -------------------------------------------------------------------

label start:
    jump Festival

label Festival:
    c "(내는 김춘배, 평범한 회사원이다.)"
    c "(오늘 회사 동료인 지아 씨와 벚꽃 축제에 다녀왔다.)"
    j "춘배 씨!"
    c "예?"
    j "이렇게 헤어지기 아쉬운데, 저희 집에서 영화라도 보고 갈래요?"
    c "그거 좋구나."
    j "아하핫! 역시 춘배 씨는 재밌는 분이시네요!"
    c "(지아 씨와 단둘이 영화라니… 정말 기대돼.)"
    j "저는 할 게 있어서 먼저 가 있을게요."
    j "주소 보낼 테니 이따 만나요!"

    jump Alley

label Alley:
    c "(내가 지아 씨 집에 가는 날이 오게 될 줄이야.)"
    c "(근데 집 가는 길이 왜 이렇게 외진 곳이지?)"
    c "(이러다 괴한한테 머리 한 대 맞고 납치당하는 거 아냐?)"
    c "(나도 참 별 생각을 다 하네…)"
    "깡!"
    c "윽…!"

    jump Cellar

label Cellar:
    if not renpy.seen_label():
        c "으윽, 머리야… 피 나는 건 아니겠지?"
        c "그런데 여기가 어디지?"
        c "설마 나… 납치 당한 거야?!"
        c "감히 나를 능멸하다니…!"
        c "어떤 자식인지는 몰라도, 나가기만 하면 용서치 않겠어."
        c "하아... 일단 이 곳에서 나갈 방법을 찾아 보자."

    jump CellarMenu

label CellarMenu:
    menu:
        "상자":
            jump Chest

        "구멍":
            jump Hole

        "캐리어":
            jump Suitcase

        "나무 문":
            if Key:
                jump DoorWithKey

            else:
                jump DoorWithoutKey

label Chest:
    c "으, 이게 뭐야... 물컹거리는데…?"
    c "?"
    c "으악!!! 쥐잖아!!!!!!!!!!!!"

    jump Cellar

label Hole:
    c "뭔가 단단한게 집히는데.."
    c "이게 뭐지?"
    c "으악!!! 해골?!"
    c "설마... 여기서 죽은 사람?!?!?!?!"

    jump Cellar

label Suitcase:
    c "이상한 거 나오진 않겠지…?"
    c "어?"
    c "열쇠다!"
    c "이거라면 문을 열 수 있지 않을까?"

    $ Key = True

    jump Cellar

label DoorWithoutKey:
    "열쇠가 필요하다."
    c "그냥 풀파워로 치면 열릴 것 같긴 한데… 어쩌지?"

    menu:
        "손으로 부순다.":
            c "윽! 겁나 아프네…"
            c "그래도 문이 박살났으니 이 공간에서 나갈 수 있겠어!"

            jump Corridor1

        "더 둘러본다.":
            c "손으로 문을 부수는 건 미친 짓이지."

            jump Cellar

label DoorWithKey:
    c "제발 이 열쇠가 맞기를…"
    c "열렸다!"
    c "드디어 이 지긋지긋한 공간에서 나갈 수 있어!"

    jump Corridor1

label Corridor1:
    if not renpy.seen_label():
        c "드디어 나왔다! 그런데 밖이 아니네?"
        c "여기서 나가자마자 범인에게 곤장 100대를 치겠어…"
        c "이제 어디로 가야하지?"

    jump Corridor1Menu

label Corridor1Menu:
    menu:
        "탈출구":
            if MasterKey:
                jump Exit

            else:
                "탈출구 문을 열려면 열쇠가 필요하다."

                jump Corridor1

        "2층 계단":
            if Floor2Cond:
                jump Corridor2

            else:
                "2층으로 올라가는 계단이다."
                "다른 곳을 먼저 둘러보고 올라가는 게 좋을 것 같다."

                jump Corridor1

        "암실":
            if Coin:
                "동전을 사용해서 잠금을 풀 수 있다."
                "문을 열어볼까?"
                    menu:
                        "문을 연다.":
                            jump DarkRoom1

                        "문을 열지 않는다.":
                            jump Corridor1

            else:
                "특이한 모양의 잠금 장치가 있다."
                "지금 가진 걸론 열 수 없다."
                    jump Corridor1

        "식당":
            "식당으로 향하는 문이다."
            "식당에 들어갈까?"

            menu:
                "문을 연다.":
                    jump DiningRoom

                "더 둘러본다.":
                    jump Corridor1

label DiningRoom:
    if not renpy.seen_label():
        c "여기가 식당인가? 엄청 크네."
        c "잠깐만, 그럼 먹을 것도 많으려나?!"
        c "조금만 구경해 봐야지!"

        jump DiningRoomMenu

label DiningRoomMenu:
    menu:
        "딸기 케이크":
            jump StrawberryCake

        "생선 대가리 케이크":
            jump FishCake

        "화장실":
            "화장실에 들어갈까?"
            menu:
                "들어간다.":
                    jump Bathroom

                "다른 곳을 둘러본다.":
                    jump DiningRoomMenu

        "부엌":
            "부엌에 들어갈까?"
            menu:
                "들어간다.":
                    jump Kitchen

                "다른 곳을 둘러본다.":
                    jump DiningRoomMenu

label StrawberryCake:
    if renpy.seen_label():
        c "참 맛있었지... 좀 찝찝하긴 하지만."

        jump DiningRoomMenu

    else:
        "맛있어 보이는 딸기 케이크다."
        "위험해 보이지는 않는데, 먹어볼까?"

        menu:
            "먹는다.":
                c "…"
                c "오! 맛있다."
                "딸기 케이크의 힘으로 HP가 10 증가했습니다."

                jump DiningRoomMenu

            "먹지 않는다.":

                c "(아무래도 이런 곳에 있는 음식을 먹는 건 좀 그래.)"

                jump DiningRoomMenu

label FishCake:
    if renpy.seen_label():
        c "......"
        c "아무거나 주워 먹으면 안된다는 교훈을 얻었지."

        jump DiningRoomMenu

    else:
        "절대 먹고 싶지 않게 생긴 생선 대가리 케이크다."
        "누가 이딴 재료로 케이크를 만들 생각을 했을까?"
        "…먹어볼까?"

        menu:
            "먹는다.":
                c "…"
                "까득!"
                c "아악!!"
                "케이크에서 동전 한 개가 나왔다."
                "이빨이 나가 HP가 20 감소했다."

                jump DiningRoomMenu

            "먹지 않는다.":
                c "내가 잠깐 미쳤었나 보네, 이걸 먹을 생각을 하다니."

                jump DiningRoomMenu

label Restroom:
    if not renpy.seen_label():
        c "오, 안은 생각보다 깔끔하네."
        c "근데 여긴 왜 뭐가 나올 것 같이 생겼냐…?"
        c "아무 일도 안 일어나겠지?"
        "문 밖에서 누군가의 발걸음 소리가 들린다."
        c "아니 이런 망할, 호랑이도 제 말하면 온다더니…!!"
        "어느 칸에 숨을까?"

        menu:
            "1번 칸":
                "발걸음 소리가 가까워졌다가 다시 멀어진다…"
                c "죽을 뻔 했네."

            "2번 칸":
                "발걸음 소리가 가까워진다..."
                c "아?"

                # 사망

            "3번 칸":
                "발걸음 소리가 가까워진다..."
                c "아?"

                # 사망

    else:
        "화장실에서 나갈까?"
        menu:
            "나간다.":
                jump DiningRoomMenu
            
            "화장실에 있는다.":
                c "무언가 쓸 만한 게 있을지도 몰라."

label Kitchen:
    if not renpy.seen_label():
        c "으, 추워... 엄청 서늘하다."
        c "무슨 엘사가 다녀갔나…"
        c "여기도 빨리 보고 나가야지."

        jump KitchenMenu

label KitchenMenu:
    menu:
        "수납장":
            "수납장을 열었다."
            if HaveMP3 == False:
                c "...? 왜 여기에 MP3 플레이어가 있지?"
                c "일단 챙겨둬야겠다."

                $ HaveMP3 = True
                jump Kitchen

            else:
                c "그래, 상식적으로 텅 빈 수납장을 또 열어봤자 뭐가 생기진 않겠지."

                jump Kitchen

        "냉장고":
            "냉장고를 열었다."
            c "뭐라 감상평을 말하기에 민망할 정도로 텅 비어 있네."
            
            jump Kitchen

        "식칼":
            jump Knife

        "오븐":
            jump Oven


label Knife:
    if not renpy.seen_label():
        c "악!"
        "칼에 손이 베여 HP가 20 감소했습니다."

    else:
        c "두 번은 안 당한다."

        jump KitchenMenu

label Oven:
    if not renpy.seen_label():
        "오븐을 열었다."
        c "으악 이게 뭐야!!"
        c "아니 이 집 주방장은 생선 못 먹어 죽은 귀신이 들렸나 왜 자꾸 생선으로 거지같은 요리를 하는 거야!!"

    else:
        c "썩은 정어리 파이 따위는 다시 보고 싶지 않아."

label DarkRoom1:
    if not renpy.seen_label():
        c "이게 대체 다 뭐야?!"
        c "어떻게 이 정도 양의 돈이 이곳에 존재하는 거지?"
        c "내가 평생 벌어도 못 벌 돈이야..."
        c "..."
        c "조금만... 슬쩍 해볼까?"
