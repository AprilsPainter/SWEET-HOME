# 캐릭터 정의 ------------------------------------------------------------
define c = Character('김춘배')
define j = Character('윤지아')
define y = Character('연살')

<<<<<<< HEAD
default dead = False
default hp = 100
default key = False
default coin = False
default floor_2_cond = False
default floor_3_cond = False
default exit_cond = False
default ate_strawberry_cake = False
default ate_fish_cake = False
default assassin_event = False

label start:
    jump festival
default bathroom_event = False
default have_MP3 = False
default knife_event = False
default oven_event = False
=======
# 변수 정의 --------------------------------------------------------------
default Key = False
default MasterKey = False
default HaveMP3 = False
default Coin = False
default Floor2Cond1 = False
default Floor2Cond2 = False
default Floor2Cond3 = False
default Floor2Cond4 = False
default Floor2Cond5 = False
default QuizLife = 3
default Answer = None
default Quiz_Cleared_List = [False, False, False, False, False, False, False]
default HaveBottle = False
default HaveHoney = False
>>>>>>> dev

default ArtCleared = False
default KoreanCleared = False
default ScienceCleared = False
default SocietyCleared = False
default HistoryCleared = False
default EnglishCleared = False
default MathCleared = False
default TechCleared = False

default FirstCellar = True
default FirstCorrior = True
default FirstDiningRoom = True
default FirstStrawberryCake = True
default FirstFishCake = True
default FirstRestroom = True
default FirstKitchen = True
default FirstKnife = True
default FirstOven = True
default FirstStorage = True
default FirstQuizRoom = True
default FirstTerrace = True

# 이미지 정의 ------------------------------------------------------------


# 아이템/오브젝트 이미지 정의 -----------------------------------------------


# 배경 이미지 정의
image bg alley = "images/backgrounds/alley.png"
image bg bedroom = "images/backgrounds/bedroom.png"
image bg cellar = "images/backgrounds/cellar.png"
image bg corridor = "images/backgrounds/corridor.png"
image bg darkroom = "images/backgrounds/darkroom.png"
image bg dining_room = "images/backgrounds/dining_room.png"
image bg exit = "images/backgrounds/exit.png"
image bg festival = "images/backgrounds/festival.png"
image bg kitchen = "images/backgrounds/kitchen.png"
image bg quiz_room = "images/backgrounds/quiz_room.png"
image bg restroom = "images/backgrounds/restroom.png"
image bg rooftop = "images/backgrounds/rooftop.png"
image bg storage = "images/backgrounds/storage.png"
image bg terrace = "images/backgrounds/terrace.png"

# 스크린 정의 ------------------------------------------------------------


# 스크립트 시작 -----------------------------------------------------------
label start:
    jump Festival

label Festival:
    scene bg festival
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
    if FirstCellar:
        $ FirstCellar = False
        c "으윽, 머리야… 피 나는 건 아니겠지?"
        c "그런데 여기가 어디지?"
        c "설마 나… 납치 당한 거야?!"
        c "감히 나를 능멸하다니…!"
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

            jump Corridor

        "더 둘러본다.":
            c "손으로 문을 부수는 건 미친 짓이지."

            jump Cellar

label DoorWithKey:
    c "제발 이 열쇠가 맞기를…"
    c "열렸다!"
    c "드디어 이 지긋지긋한 공간에서 나갈 수 있어!"

    jump Corridor

label Corridor:
    if FirstCorrior:
        $ FirstCorrior = False
        c "드디어 나왔다! 그런데 밖이 아니네?"
        c "여기서 나가자마자 범인에게 곤장 100대를 치겠어…"
        c "이제 어디로 가야하지?"

    jump CorridorMenu

label CorridorMenu:
    menu:
        "탈출구":
            if MasterKey:
                jump Exit

            else:
                "탈출구 문을 열려면 열쇠가 필요하다."

                jump Corridor

        "2층 계단":
            if Floor2Cond1 and Floor2Cond2 and Floor2Cond3 and Floor2Cond4 and Floor2Cond5:
                jump QuizRoom

            else:
                "2층으로 올라가는 계단이다."
                "다른 곳을 먼저 둘러보고 올라가는 게 좋을 것 같다."

                jump Corridor

        "창고":
            if Coin:
                "동전을 사용해서 잠금을 풀 수 있다."
                "문을 열어볼까?"
                menu:
                    "문을 연다.":
                        jump Storage

                    "문을 열지 않는다.":
                        jump Corridor

            else:
                "특이한 모양의 잠금 장치가 있다."
                "지금 가진 걸론 열 수 없다."
                jump Corridor

        "식당":
            "식당으로 향하는 문이다."
            "식당에 들어갈까?"

            menu:
                "문을 연다.":
                    jump DiningRoom

                "더 둘러본다.":
                    jump Corridor

label DiningRoom:
    if FirstDiningRoom:
        $ FirstDiningRoom = False
        c "여기가 식당인가? 엄청 크네."
        c "잠깐만, 그럼 먹을 것도 많으려나?!"
        c "조금만 구경해 봐야지!"

        jump DiningRoomMenu

label DiningRoomMenu:
    menu:
        "문":
            "식당에서 나갈까?"
            menu:
                "식당에서 나간다.":
                    jump Corridor

                "더 둘러본다.":
                    jump DiningRoom

        "딸기 케이크":
            jump StrawberryCake

        "생선 대가리 케이크":
            jump FishCake

        "화장실":
            "화장실에 들어갈까?"
            menu:
                "들어간다.":
                    jump Restroom

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
    if not FirstStrawberryCake:
        $ FirstStrawberryCake = False
        c "참 맛있었지... 좀 찝찝하긴 하지만."

        jump DiningRoom

    else:
        "맛있어 보이는 딸기 케이크다."
        "위험해 보이지는 않는데, 먹어볼까?"

        $ Floor2Cond1 = True

        menu:
            "먹는다.":
                c "…"
                c "오! 맛있다."
                "딸기 케이크의 힘으로 HP가 10 증가했습니다."

                jump DiningRoom

            "먹지 않는다.":

                c "(아무래도 이런 곳에 있는 음식을 먹는 건 좀 그래.)"

                jump DiningRoom

label FishCake:
    if not FirstFishCake:
        $ FirstFishCake = False
        c "......"
        c "아무거나 주워 먹으면 안된다는 교훈을 얻었지."

        jump DiningRoom

    else:
        "절대 먹고 싶지 않게 생긴 생선 대가리 케이크다."
        "누가 이딴 재료로 케이크를 만들 생각을 했을까?"
        "…먹어볼까?"

        $ Floor2Cond2 = True

        menu:
            "먹는다.":
                c "…"
                "까득!"
                c "아악!!"
                "케이크에서 동전 한 개가 나왔다."
                "이빨이 나가 HP가 20 감소했다."
<<<<<<< HEAD

                $ ate_fish_cake = True
                $ coin = True
=======
>>>>>>> dev

                jump DiningRoom

            "먹지 않는다.":
                c "내가 잠깐 미쳤었나 보네, 이걸 먹을 생각을 하다니."

<<<<<<< HEAD
                jump dining_room_menu

label bathroom:
    if assassin_event == False:
        k "오, 안은 생각보다 깔끔하네."
        k "근데 여긴 왜 뭐가 나올 것 같이 생겼냐...?"
        k "아무 일도 안 일어나겠지?"
        "문 밖에서 누군가의 발걸음 소리가 들린다."
        "그것은 점점 가까워지고 있었다."
        k "아니 이런 망할, 호랑이도 제 말하면 온다더니...!!"
        "어느 칸에 숨어야 하지?"
=======
                jump DiningRoom

label Restroom:
    if FirstRestroom:
        $ FirstRestroom = False
        c "오, 안은 생각보다 깔끔하네."
        c "근데 여긴 왜 뭐가 나올 것 같이 생겼냐…?"
        c "아무 일도 안 일어나겠지?"
        "문 밖에서 누군가의 발걸음 소리가 들린다."
        c "아니 이런 망할, 호랑이도 제 말하면 온다더니…!!"
        "어느 칸에 숨을까?"
>>>>>>> dev

        $ Floor2Cond3 = True

        menu:
            "1번 칸":
<<<<<<< HEAD
                "당신은 1번 칸으로 잽싸게 들어갔다."
                "..."
                "발걸음 소리가 가까워졌다가, 다시 멀어진다..."
                k "(죽을 뻔했네. 앞으로는 플래그를 세우는 대사 따위 뱉지 않겠어.)"

                $ assassin_event = True
                jump bathroom
=======
                "발걸음 소리가 가까워졌다가 다시 멀어진다…"
                c "죽을 뻔 했네."
                jump Restroom
>>>>>>> dev

            "2번 칸":
                "당신은 2번 칸으로 잽싸게 들어갔다."
                "..."
                "발걸음 소리가 가까워진다..."
                c "아?"

<<<<<<< HEAD
                $ dead = True
                $ renpy.full_restart()
=======
                # 사망
>>>>>>> dev

            "3번 칸":
                "당신은 3번 칸으로 잽싸게 들어갔다."
                "..."
                "발걸음 소리가 가까워진다..."
                c "아?"

<<<<<<< HEAD
                $ dead = True
                $ renpy.full_restart()


    else:
        k "다시는 하고 싶지 않은 경험이었다."

label kitchen:
=======
                # 사망

    else:
        menu:
            "문":
                "화장실에서 나가시겠습니까?"
                menu:
                    "화장실에서 나간다.":
                        jump DiningRoom

                    "더 둘러본다.":
                        jump Restroom

            "오브젝트":
                "~~을 조사했습니다."
                jump Restroom

            "오브젝트":
                "~~을 조사했습니다."
                jump Restroom

            "오브젝트":
                "~~을 조사했습니다."
                jump Restroom

label Kitchen:
    if FirstKitchen:
        $ FirstKitchen = False
        c "으, 추워... 엄청 서늘하다."
        c "무슨 엘사가 다녀갔나…"
        c "여기도 빨리 보고 나가야지."

        jump KitchenMenu

label KitchenMenu:

    $ Floor2Cond4 = True

    menu:
        "문":
            "부엌에서 나갈까?"
            menu:
                "부엌에서 나간다.":
                    jump DiningRoom

                "더 둘러본다.":
                    jump Kitchen

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
    if FirstKnife:
        $ FirstKnife = False
        c "악!"
        "칼에 손이 베여 HP가 20 감소했습니다."

    else:
        c "두 번은 안 당한다."

        jump KitchenMenu

label Oven:
    if FirstOven:
        $ FirstOven = False
        "오븐을 열었다."
        c "으악 이게 뭐야!!"
        c "아니 이 집 주방장은 생선 못 먹어 죽은 귀신이 들렸나 왜 자꾸 생선으로 거지같은 요리를 하는 거야!!"

    else:
        c "썩은 정어리 파이 따위는 다시 보고 싶지 않아."

label Storage:
    if FirstStorage:
        $ FirstStorage = False
        c "이게 대체 다 뭐야?!"
        c "어떻게 이 정도 양의 돈이 이곳에 존재하는 거지?"
        c "내가 평생 벌어도 못 벌 돈이야..."
        c "..."
        c "조금만... 슬쩍 해볼까?"

        menu:
            "돈을 챙긴다.":
                c "조금은 괜찮잖아?"
                "당신은 돈더미를 향해 다가간다."
                "...깡!"
                c "윽!"

                # 사망

            "돈을 챙기지 않는다.":
                c "아니지, 이 거지 같은 장소에 있는 돈 따위 가지고 싶지 않아."

    else:
        jump StorageMenu

label StorageMenu:

    $ Floor2Cond5 = True

    menu:
        "문":
            "창고에서 나가시겠습니까?"
            menu:
                "창고에서 나간다.":
                    jump Corridor

                "더 둘러본다.":
                    jump StorageMenu

        "오브젝트":
            "~~을 조사했습니다."
            jump StorageMenu

        "오브젝트":
            "~~을 조사했습니다."
            jump StorageMenu

        "오브젝트":
            "~~을 조사했습니다."
            jump StorageMenu

# 퀴즈 ===============================================================================

label QuizRoom:
    if FirstQuizRoom:
        $ FirstQuizRoom = False
        c "이건 뭐 방탈출 게임도 아니고 퀴즈가 왜 이렇게 많아?"
        c "빨리 풀고 넘어가야겠어."

    if ArtCleared and KoreanCleared and ScienceCleared and SocietyCleared and HistoryCleared and EnglishCleared and MathCleared and TechCleared:
        "침실로 가는 문이 열렸다."
        jump Bedroom

    menu:
        "테라스 문":
            "테라스로 갈까?"
            menu:
                "테라스로 간다.":
                    jump Terrace
                "나가지 않는다.":
                    jump QuizRoom

        "미술" if not ArtCleared:
            jump ArtQuiz

        "국어" if not KoreanCleared:
            jump KoreanQuiz

        "과학" if not ScienceCleared:
            jump ScienceQuiz

        "사회" if not SocietyCleared:
            jump SocietyQuiz

        "역사" if not HistoryCleared:
            jump HistoryQuiz

        "영어" if not EnglishCleared:
            jump EnglishQuiz

        "수학" if not MathCleared:
            jump MathQuiz

        "기술가정" if not TechCleared:
            jump TechQuiz

label LifeCheck:
    if QuizLife <= 0:
        c "이... 이게 무슨 느낌이지?"
        "갑작스레 당신의 머리가 깨질듯이 아파옵니다."
        c "안돼...!"

        # 사망

    else:
        "남은 기회: [QuizLife]번"
        jump QuizRoom

label ArtQuiz:
    show text "{size=30}{b}[[미술]{/b}\n\n다음은 그림과 관련된 지식입니다. 옳지 않은 것은 무엇인지 1, 2, 3 중 하나를 쓰세요.\n\n1. 금속처럼 반짝거리는 재질을 그리려면 검은색이나 어두운 색을 적극적으로 활용해야 한다.\n2. 팝 아트는 대중(Popular)과 예술(Art)의 합성어로 추상적인 기하학적 이미지를 미술 영역으로 수용한 순수미술의 한 경향을 가리킨다.\n3. 이 게임의 디자이너는 세계 최고의 그림러다." at truecenter
    $ Answer = renpy.input("정답을 입력하세요.").strip()
    hide text
    if Answer == "2":
        show text "{size=30}{b}정답입니다!{/b}" at truecenter
        pause 1.0
        hide text
        $ ArtCleared = True
        jump QuizRoom
    else:
        show text "{size=30}{b}틀렸습니다.{/b}" at truecenter
        pause 1.0
        hide text
        $ QuizLife -= 1
        jump LifeCheck

label KoreanQuiz:
    show text "{size=30}{b}[[국어]{/b}\n\n아래 문장에서 둘 중 옳은 표현은 무엇인가요?\n\n1. 나는 [[곰곰히 / 곰곰이] 생각했다." at truecenter
    $ Answer = renpy.input("정답을 입력하세요.").strip()
    hide text
    if Answer == "곰곰이":
        show text "{size=30}{b}정답입니다!{/b}" at truecenter
        pause 1.0
        hide text
    else:
        show text "{size=30}{b}틀렸습니다.{/b}" at truecenter
        pause 1.0
        hide text
        $ QuizLife -= 1

        if QuizLife <= 0:
            jump LifeCheck
        else:
            "남은 기회: [QuizLife]번"

    show text "{size=30}{b}[[국어]{/b}\n\n아래 문장에서 둘 중 옳은 표현은 무엇인가요?\n\n2. [[재작년 / 제작년] 매출보다 높네." at truecenter
    $ Answer = renpy.input("정답을 입력하세요.").strip()
    hide text
    if Answer == "재작년":
        show text "{size=30}{b}정답입니다!{/b}" at truecenter
        pause 1.0
        hide text
    else:
        show text "{size=30}{b}틀렸습니다.{/b}" at truecenter
        pause 1.0
        hide text
        $ QuizLife -= 1
        if QuizLife <= 0:
            jump LifeCheck
        else:
            "남은 기회: [QuizLife]번"

    show text "{size=30}{b}[[국어]{/b}\n\n아래 문장에서 둘 중 옳은 표현은 무엇인가요?\n\n3. [[맞힐 / 맞출] 수 있으면 해봐." at truecenter
    $ Answer = renpy.input("정답을 입력하세요.").strip()
    hide text
    if Answer == "맞힐":
        show text "{size=30}{b}정답입니다!{/b}" at truecenter
        pause 1.0
        hide text
        $ KoreanCleared = True
        jump QuizRoom
    else:
        show text "{size=30}{b}틀렸습니다.{/b}." at truecenter
        pause 1.0
        hide text
        $ QuizLife -= 1
        jump LifeCheck

label ScienceQuiz:
    show text "{size=30}{b}[[과학]{/b}\n\n다음 화학 반응에서의 세 규칙 중 부피와 관련된 것은 무엇인지 1, 2, 3 중 하나를 쓰세요.\n\n1. 질량 보존 법칙\n2. 일정 성분비 법칙\n3. 기체 반응 법칙"
    $ Answer = renpy.input("정답을 입력하세요.").strip()
    hide text
    if Answer == "3":
        show text "{size=30}{b}정답입니다!{/b}" at truecenter
        pause 1.0
        hide text
        $ ScienceCleared = True
        jump QuizRoom
    else:
        show text "{size=30}{b}틀렸습니다.{/b}." at truecenter
        pause 1.0
        hide text
        $ QuizLife -= 1
        jump LifeCheck

label SocietyQuiz:
    show text "{size=30}{b}[[사회]{/b}\n\n기회비용의 의미로 알맞은 것은 무엇인지 1, 2, 3, 4 중 하나를 쓰세요.\n\n1. 어떤 주식을 매수했을 때 특정 기간 동안의 예상 이익에서 예상 손해액을 뺀 것\n2. 경제에서 여러 선택지 중 하나를 선택했을 때 그 선택으로 인해 포기해야 하는 대안 중 가장 가치가 큰 것\n3. 어떤 후보자가 특정 선거 전략을 펼쳤을 때 그로 인해 지지를 철회하는 지지자의 수와 선거 비용의 합\n4. 경제에서 이미 지출되어 어떤 선택을 하더라도 되돌릴 수 없는 비용" at truecenter
    $ Answer = renpy.input("정답을 입력하세요.").strip()
    hide text
    if Answer == "2":
        show text "{size=30}{b}정답입니다!{/b}" at truecenter
        pause 1.0
        hide text
        $ SocietyCleared = True
        jump QuizRoom
    else:
        show text "{size=30}{b}틀렸습니다.{/b}" at truecenter
        pause 1.0
        hide text
        $ QuizLife -= 1
        jump LifeCheck

label HistoryQuiz:
    show text "{size=30}{b}[[역사]{/b}\n\n사건과 설명이 옳지 않게 짝지어진 것은 무엇인지 1, 2, 3, 4, 5 중 하나를 쓰세요.\n\n1. 제주 4.3 사건: 경찰 발포 사건으로 시작된 제주 주민들의 무장 봉기에 대해 미군정과 예하의 국군, 경찰이 자행한 민간인 학살 사건\n2. 동학 농민 혁명: 전봉준을 중심으로 한 농민들이 탐관오리의 착취와 외세의 침략에 저항하며 개혁을 요구한 농민 봉기\n3. 3.1 운동: 한반도 전역과 세계 각지의 한인 밀집 지역에서 시민들이 독립을 선언하며 일제의 강점에 저항권을 행사한 시민 불복종 운동이자 독립운동\n4.  6.25 전쟁: 북한 공산 정권이 한반도 적화 통일을 목적으로 선전포고 없이 38선을 넘어 남침하여 시작된 전쟁\n5. 6월 항쟁: 전두환 정권의 장기집권 의도에 시민들이 ’호헌철폐 독재타도 민주쟁취‘ 등을 외치며 일어났으나, 대통령 직선제를 쟁취하는 데는 실패한 민주화 운동" at truecenter
    $ Answer = renpy.input("정답을 입력하세요.").strip()
    hide text
    if Answer == "5":
        show text "{size=30}{b}정답입니다!{/b}" at truecenter
        pause 1.0
        hide text
        $ HistoryCleared = True
        jump QuizRoom
    else:
        show text "{size=30}{b}틀렸습니다.{/b}" at truecenter
        pause 1.0
        hide text
        $ QuizLife -= 1
        jump LifeCheck

label EnglishQuiz:
    show text "{size=30}{b}[[영어]{/b}\n\n다음 중 어법적으로 옳은 문장은 무엇인지 1, 2, 3 중 하나를 쓰세요.\n\n1. Never have I have been to Korea.\n2. What you said yesterday were so terrible that I almost threw up.\n3. Do you know what he told to me?" at truecenter
    $ Answer = renpy.input("정답을 입력하세요.").strip()
    hide text
    if Answer == "1":
        show text "{size=30}{b}정답입니다!{/b}" at truecenter
        pause 1.0
        hide text
        $ EnglishCleared = True
        jump QuizRoom
    else:
        show text "{size=30}{b}틀렸습니다.{/b}" at truecenter
        pause 1.0
        hide text
        $ QuizLife -= 1
        jump LifeCheck

label MathQuiz:
    show text '{size=30}{b}[[수학]{/b}\n\n마토와 인터가 함께 급식을 먹으러 가고 있었습니다.\n인터가 학생 A와 B의 삼각형 모양 머리를 보고 이렇게 말했습니다.\n"학생 A의 머리의 한 각이 학생 B의 머리의 한 각과 같고, 그 각들의 대변의 길이가 각각 같으므로 학생 A의 머리와 학생 B의 머리는 합동이야."\n\n그러자 마토가 이렇게 말했습니다.\n"네 삼각형 모양 머리를 수직으로 가르는 직선을 그리면 그 직선의 그래프는 a가 0이 아닌 y=ax의 그래프로 나타나는데,\n이때 이 그래프는 a의 값과 관계 없이 반드시 (0, 1)의 점을 지나. 그러니까 네 두개골을 수직으로 가르는 직선을 그어 버리기 전에 조용히 하면 안 될까?"\n\n그때 지나가던 근초고왕이 이렇게 말했습니다.\n"이차방정식을 푸는 방법 중 하나인 인수분해는 각각 수 또는 식인 A와 B의 곱이 0일 때, A와 B 중 하나는 무조건 0이라는 원리를 이용해.\n나와 함께 백제의 전성기를 이끌지 않을래?"\n\n마지막으로 그들을 발견한 유 교수가 말했습니다.\n"어떤 소수를 기약분수로 바꾸어 나타낼 때, 분모의 소인수가 2, 3, 5뿐이면 그것은 유한소수이고 그렇지 않다면 그것은 순환소수야."\n\n\n위 글에서 옳은 말을 한 사람은 누구인지 [[인터, 마토, 근초고왕, 유 교수] 중 맞는 것을 모두 쓰시오.' at truecenter
    $ Answer = renpy.input("정답을 입력하세요.").strip()
    hide text
    if Answer == "근초고왕":
        show text "{size=30}{b}정답입니다!{/b}" at truecenter
        pause 1.0
        hide text
        $ MathCleared = True
        jump QuizRoom
    else:
        show text "{size=30}{b}틀렸습니다.{/b}" at truecenter
        pause 1.0
        hide text
        $ QuizLife -= 1
        jump LifeCheck

label TechQuiz:
    show text "{size=30}{b}[[기술]{/b}\n\n벌꿀을 채취해 오세요." at truecenter
    menu:
        "뒤로 가기":
            hide text
            jump QuizRoom

# ====================================================================================

label Terrace:
    if FirstTerrace:
        $ FirstTerrace = False
        c "여기에는 지하실도 있고, 테라스도 있고 별의별 게 다 있냐…"
        c "김춘배: 저건 뭐지?"
        c "김춘배: 벌집이잖아! 이게 뭔 거지 같은 경우지?"

label Bedroom:
    "침실."
>>>>>>> dev
