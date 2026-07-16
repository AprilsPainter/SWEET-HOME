define k = Character('김춘배')
define j = Character('윤지아')
define y = Character('연살')

default hp = 100
default key = False
default coin = False
default floor_2_cond = False
default floor_3_cond = False
default exit_cond = False
default ate_strawberry_cake = False
default ate_fish_cake = False
default bathroom_event = False
default have_MP3 = False
default knife_event = False
default oven_event = False

label start:
    jump festival

label game_over(cause: str):
    "[게임 오버] {cause}"

    menu:
        "처음부터":
            renpy.utter_restart()

        "메인 화면":
            renpy.full_restart()

label hp(amount: int, cause: str = ""):
    $ hp += amount
    if amount > 0:
        "{cause} HP가 {amount} 증가했습니다."

    elif amount < 0:
        "{cause} HP가 {amount} 감소했습니다."

    if hp <= 0:
        jump game_over("HP가 0이 되어 사망하였습니다.")

label festival:
    k "(내는 김춘배, 평범한 회사원이다.)"
    k "(오늘은 회사 동료인 윤지아 씨와 함께 벚꽃 축제를 즐겼다.)"
    j "춘배 씨! 이렇게 헤어지기 아쉬운데, 오늘 저희 집에서 영화라도 보고 가실래요?"
    k "그래 좋다."
    j "아하핫! 역시 춘배 씨는 재밌는 분이시네요!"
    k "(지아 씨와 단둘이 영화라니… 정말 기대돼.)"
    j "저는 할 게 있어서 먼저 가 있을게요."
    j "주소 보내드릴 테니까 이따 만나요!"

    jump way_home

label way_home:
    k "(내가 지아 씨 집에 가는 날이 오게 될 줄이야.)"
    k "(근데 집 가는 길이 왜 이렇게 외진 곳이지?)"
    k "(이러다 괴한한테 머리 한 대 맞고 납치당하는 거 아냐?)"
    k "(나도 참 별 생각을 다 하네…)"
    "깡!" # 효과음
    k "윽…!"

    jump cellar

label cellar:
    k "으윽, 머리야… 피 나는 건 아니겠지?"
    k "그런데 여기가 어디지…?"
    k "설마 나… 납치 당한 거야?!"
    k "감히 나를 능멸하다니… 나가기만 하면 용서치 않겠어."
    k "하아... 일단 이 곳에서 나갈 방법을 찾아 보자."

    # 오브젝트 클릭 시 각각의 라벨로 이동, 일단 메뉴로 대체

    jump cellar_menu

label cellar_menu:
    menu:
        "상자":
            jump chest

        "구멍":
            jump hole

        "캐리어":
            jump suitcase

        "나무 문":
            if key:
                jump door_with_key

            else:
                jump door_no_key

label chest:
    k "으, 이게 뭐야... 물컹거리는데…?"
    k "?"
    k "으악!!! 쥐잖아!!!!!!!!!!!!"

    jump cellar_menu

label hole:
    k "뭔가 단단한게 집히는데.."
    k "이게 뭐지?"
    k "으악!!! 해골?!"
    k "설마 여기서 죽은 거야?!?!?!?!"

    jump cellar_menu

label suitcase:
    k "이상한 거 나오진 않겠지…?"
    k "어?"
    k "열쇠다!"
    k "이거라면 문을 열 수 있지 않을까?"

    $ key = True

    jump cellar_menu

label door_no_key:
    "열쇠가 필요한 것 같다."
    k "그냥 겁나 세게 치면 열릴 것 같긴 한데… 어쩌지?"

    menu:
        "손으로 부순다.":
            k "윽! 겁나 아프네…"
            k "그래도 문이 박살났으니 이 공간에서 나갈 수 있겠어!"

            jump corridor_1

        "더 둘러본다.":
            k "손으로 문을 부수는 건 미친 짓이지."

            jump cellar_menu

label door_with_key:
    k "제발 이 열쇠가 맞기를…"
    k "열렸다!"
    k "드디어 이 지긋지긋한 공간에서 나갈 수 있어!"

    jump corridor_1

label corridor_1:
    k "드디어 나왔다! 그런데 밖이 아니네…?"
    k "여기서 나가자마자 범인에게 곤장 100대를 맞게 하겠어…"
    k "이제 어디로 가야하지?"

    # 이미지 오브젝트 선택, 일단 메뉴로 대체

    jump corridor_1_menu

label corridor_1_menu:
    menu:
        "탈출구":
            if exit_cond:
                jump exit

            else:
                "탈출구 문을 열려면 열쇠가 필요한 것 같다."

                jump corridor_1_menu

        "2층 계단":
            if floor_2_cond:
                jump corridor_2

            else:
                "2층으로 올라가는 계단이다."
                "다른 곳을 더 둘러보고 올라가는 게 좋을 것 같다."

                jump corridor_1_menu

        "암실":
            if coin:
                    "동전을 사용해서 잠금을 풀 수 있는 것 같다."
                    "문을 열어볼까?"

                    menu:
                        "문을 연다.":

                            jump dark_room_1

                        "문을 열지 않는다.":

                            jump corridor_1_menu

            else:
                "특이한 모양의 잠금 장치가 있다."
                "지금 가진 걸론 열 수 없는 것 같다."

                jump corridor_1_menu

        "식당":
            "식당으로 향하는 문이다."
            "식당으로 가볼까?"

            menu:
                "문을 연다.":
                    jump dining_room

                "더 둘러본다.":
                    jump corridor_1_menu

label dining_room:
    k "여기가 식당인가? 엄청 크네."
    k "잠깐만, 그럼 먹을 것도 많으려나?!"
    k "조금만 구경해 봐야지!"

    # 이미지 오브젝트 클릭, 일단 메뉴로 대체

    jump dining_room_menu

label dining_room_menu:
    menu:
        "딸기 케이크":
            jump strawberry_cake

        "생선 대가리 케이크":
            jump fish_cake

        "화장실(미완)":
            "화장실에 들어갈까?"
            menu:
                "들어간다.":
                    jump bathroom

                "다른 곳을 둘러본다.":
                    jump dining_room_menu

        "부엌(미완)":
            "부엌에 들어갈까?"
            menu:
                "들어간다.":
                    jump kitchen

                "다른 곳을 둘러본다.":
                    jump dining_room_menu

label strawberry_cake:
    if ate_strawberry_cake:
        k "참 맛있었지... 좀 찝찝하긴 하지만."

        jump dining_room_menu

    else:
        "맛있어 보이는 딸기 케이크다."
        "위험해 보이지는 않는데, 먹어볼까?"

        menu:
            "먹는다.":
                k "…"
                k "오! 맛있다."
                "딸기 케이크의 힘으로 HP가 10 증가했습니다."

                $ ate_strawberry_cake = True

                jump dining_room_menu

            "먹지 않는다.":

                k "(아무래도 이런 곳에 있는 음식을 먹는 건 좀 그래.)"

                jump dining_room_menu

label fish_cake:
    if ate_fish_cake:
        k "......"
        k "아무거나 주워 먹으면 안된다는 교훈을 얻었지."

        jump dining_room_menu

    else:
        "절대 먹고 싶지 않게 생긴 생선 대가리 케이크다."
        "누가 이딴 재료로 케이크를 만들 생각을 했을까?"
        "…먹어볼까?"

        menu:
            "먹는다.":
                k "…"
                "까득!"
                k "아악!!"
                "케이크에서 동전 한 개가 나왔다."
                "이빨이 나가 HP가 20 감소했다."
                $ ate_fish_cake = True

                jump dining_room_menu

            "먹지 않는다.":
                k "내가 잠깐 미쳤었나 보네, 이걸 먹을 생각을 하다니."

                jump dining_room_menu

label bathroom:
    if bathroom_event == False:
        k "오, 안은 생각보다 깔끔하네."

        k "근데 여긴 왜 뭐가 나올 것 같이 생겼냐…?"

        k "아무 일도 안 일어나겠지?"

        "문 밖에서 누군가의 발걸음 소리가 들린다."

        k "아니 이런 망할, 호랑이도 제 말하면 온다더니…!!"

        "어느 칸에 숨을까?"

        menu:
            "1번 칸":
                "발걸음 소리가 가까워졌다가 다시 멀어진다…"
                k "Sh*t, 죽을 뻔 했네."

                $ bathroom_event = True

            "2번 칸":
                "발걸음 소리가 가까워진다..."
                k "아?"

                jump game_over("자객에 의해 사망하였습니다.")

            "3번 칸":
                "발걸음 소리가 가까워진다..."
                k "아?"

                jump game_over("자객에 의해 사망하였습니다.")

    else:
        "화장실에서 나갈까?"
        menu:
            "나간다.":
                jump dining_room_menu
            
            "화장실에 있는다.":
                k "무언가 쓸 만한 게 있을지도 몰라."
                # 조사 상태

label kitchen:
    k "으, 추워... 엄청 서늘하다."

    k " 무슨 엘사가 다녀갔나…"

    k " 여기도 빨리 보고 나가야지."

    jump kitchen_menu

label kitchen_menu:
    menu:
        "수납장":
            "수납장을 열었다."
            if have_MP3 == False:
                k "...? 왜 여기에 MP3 플레이어가 있지?"
                k "일단 챙겨둬야겠다."

                $ have_MP3 = True

                $ have_MP3 = True
                jump kitchen_menu

            else:
                k "그렇지, 상식적으로 텅 빈 수납장을 또 열어봤자 뭐가 생기진 않겠지."

                jump kitchen_menu

        "냉장고":
            "냉장고를 열었다."
            k "뭐라 감상평을 말하기도 민망할 정도로 아무 것도 안 들어 있네."
            
            jump kitchen_menu

        "식칼":
            if knife_event == False:
                k "악!"
                call hp(-10, "식칼에 손이 베여")

                $ knife_event = True

            else:
                k "두 번은 안 당한다."

                jump kitchen_menu

        "오븐":
            "오븐을 열었다."
            if oven_event == False:
                k "으악 이게 뭐야!!"
                k "아니 이 집 주방장은 생선 못 먹어 죽은 귀신이 들렸나 왜 자꾸 생선으로 거지같은 요리를 하는 거야!!"

                $ oven_event = True

            else:
                k "썩은 정어리 파이 따위는 다시 보고 싶지 않아."