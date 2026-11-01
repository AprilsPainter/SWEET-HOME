# 캐릭터 정의 ------------------------------------------------------------
define c = Character('김춘배')
define j = Character('윤지아')
define y = Character('연살')

# 변수 정의 --------------------------------------------------------------

default HP = 100
default EndingType = None

# 퀴즈
default QuizLife = 3
default Answer = None
default Cleared_KoreanQuiz = False
default Cleared_EnglishQuiz = False
default Cleared_MathQuiz = False
default Cleared_ScienceQuiz = False
default Cleared_HistoryQuiz = False
default Cleared_SocietyQuiz = False
default Cleared_ArtQuiz = False
default Cleared_TechQuiz = False

# 아이템
default CellarKey = False
default MasterKey = False
default GoldenCoin = False
default GlassBottle = False
default Honey_GlassBottle = False
default MP3 = False

# 첫 방문
default FirstCellar = True
default FirstCorridor = True
default FirstDiningRoom = True
default FirstRestroom = True
default FirstKitchen = True
default FirstKnife = True
default FirstOven = True
default FirstStorage = True
default FirstQuizRoom = True
default FirstTerrace = True

# 진행 조건
default Checked_StrawberryCake = False
default Checked_FishCake = False
default Checked_RestroomEvent = False
default Checked_Kitchen = False
default Ate_StrawberryCake = False
default Ate_FishCake = False

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
image bg game_over = "images/backgrounds/game_over.png"
image bg game_clear = "images/backgrounds/game_clear.png"

# 스크린 정의 ------------------------------------------------------------


# 스크립트 시작 -----------------------------------------------------------
label start:
    jump Festival

label GameClear:
    scene bg game_clear
    show text "{size=60}{b}탈출에 성공하였습니다!{/b}" at truecenter
    pause 2.0
    hide text

    menu:
        "처음부터 다시":
            $ renpy.full_restart()

        "게임 종료":
            return

label GameOver:
    scene bg game_over

    if EndingType == "NoHP":
        show text "{size=60}{b}HP가 0이 되어 사망했습니다.{/b}" at truecenter

    elif EndingType == "NoQuizLife":
        show text "{size=60}{b}세 번의 기회 안에 퀴즈를 모두 풀지 못해 사망했습니다.{/b}" at truecenter
    
    elif EndingType == "RestroomAssassin":
        show text "{size=60}{b}화장실에서 자객에 의해 사망했습니다.{/b}" at truecenter

    elif EndingType == "StorageAssassin":
        show text "{size=60}{b}창고에서 자객에 의해 사망했습니다.{/b}" at truecenter

    elif EndingType == "DarkroomAssassin":
        show text "{size=60}{b}암실에서 자객에 의해 사망했습니다.{/b}" at truecenter

    elif EndingType == "Yeonsal":
        show text "{size=60}{b}연살에게 패배하였습니다.{/b}" at truecenter

    pause 2.0
    hide text
    menu:
        "처음부터 다시":
            $ renpy.full_restart()
            
        "게임 종료":
            return

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
    scene bg alley
    c "(내가 지아 씨 집에 가는 날이 오게 될 줄이야.)"
    c "(근데 집 가는 길이 왜 이렇게 외진 곳이지?)"
    c "(이러다 괴한한테 머리 한 대 맞고 납치당하는 거 아냐?)"
    c "(나도 참 별 생각을 다 하네…)"
    "깡!"
    c "윽…!"

    jump Cellar

label Cellar:
    scene bg cellar
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
            if CellarKey:
                jump DoorWithCellarKey

            else:
                jump DoorWithoutCellarKey

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
    "{b}{color=ffd400}지하실 열쇠{/color}{/b}를 획득했습니다."

    $ CellarKey = True

    jump Cellar

label DoorWithoutCellarKey:
    "이 문을 열려면 열쇠가 필요합니다."
    c "그냥 풀파워로 치면 열릴 것 같긴 한데… 어쩌지?"

    menu:
        "손으로 부순다.":
            $ HP = max(HP - 30, 0)
            "{color=66ff66}HP가 30 감소했습니다.{/color}"

            if  HP <= 0:
                $ EndingType = "NoHP"
                jump GameOver

            c "윽! 겁나 아프네…"
            c "그래도 문이 박살났으니 이 공간에서 나갈 수 있겠어!"

            jump Corridor

        "더 둘러본다.":
            c "손으로 문을 부수는 건 미친 짓이지."

            jump Cellar

label DoorWithCellarKey:
    c "제발 이 열쇠가 맞기를…"
    c "열렸다!"
    c "드디어 이 지긋지긋한 공간에서 나갈 수 있어!"

    jump Corridor

label Corridor:
    scene bg corridor
    if FirstCorridor:
        $ FirstCorridor = False
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
                "탈출구 문을 열려면 열쇠가 필요합니다."

                jump Corridor

        "2층 계단":
            if Checked_StrawberryCake and Checked_FishCake and Checked_RestroomEvent and Checked_Kitchen:
                jump QuizRoom

            else:
                "2층으로 올라가는 계단이다."
                "다른 곳을 먼저 둘러보고 올라가는 게 좋을 것 같다."

                jump Corridor

        "창고":
            if GoldenCoin:
                "{b}{color=ffd400}황금 동전{/color}{/b}을 사용해서 잠금을 풀 수 있다."
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
    scene bg dining_room
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
                    jump DiningRoomMenu

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
    if Ate_StrawberryCake:
        c "참 맛있었지... 좀 찝찝하긴 하지만."
        jump DiningRoomMenu

    else:
        "맛있어 보이는 딸기 케이크다."
        "위험해 보이지는 않는데, 먹어볼까?"

        menu:
            "먹는다.":
                $ Ate_StrawberryCake = True
                $ Checked_StrawberryCake = True
                c "…"
                c "오! 맛있다."
                $ HP = min(HP + 10, 100)
                "딸기 케이크의 힘으로 HP가 10 증가했습니다."
                jump DiningRoomMenu

            "먹지 않는다.":
                c "(아무래도 이런 곳에 있는 음식을 먹는 건 좀 그래.)"
                $ Checked_StrawberryCake = True
                jump DiningRoomMenu

label FishCake:
    if Ate_FishCake:
        c "......"
        c "아무거나 주워 먹으면 안된다는 교훈을 얻었지."
        jump DiningRoomMenu

    else:
        "절대 먹고 싶지 않게 생긴 생선 대가리 케이크다."
        "누가 이딴 재료로 케이크를 만들 생각을 했을까?"
        "…먹어볼까?"

        menu:
            "먹는다.":
                $ Ate_FishCake = True
                $ Checked_FishCake = True
                $ GoldenCoin = True
                c "…"
                "까득!"
                c "아악!!"
                "케이크에서 동전 한 개가 나왔다."
                "이빨이 나가 HP가 20 감소했다."
                $ HP = max(HP - 20, 0)

                if  HP <= 0:
                    $  EndingType = "NoHP"
                    jump GameOver

                jump DiningRoomMenu

            "먹지 않는다.":
                $ Checked_FishCake = True
                c "내가 잠깐 미쳤었나 보네, 이걸 먹을 생각을 하다니."
                jump DiningRoomMenu

label Restroom:
    scene bg restroom
    if FirstRestroom:
        $ FirstRestroom = False
        c "오, 안은 생각보다 깔끔하네."
        c "근데 여긴 왜 뭐가 나올 것 같이 생겼냐…?"
        c "아무 일도 안 일어나겠지?"
        "문 밖에서 누군가의 발걸음 소리가 들린다."
        c "아니 이런 망할, 호랑이도 제 말하면 온다더니…!!"
        "어느 칸에 숨을까?"

        menu:
            "1번 칸":
                "당신은 1번 칸으로 잽싸게 들어갔다."
                "..."
                "발걸음 소리가 가까워졌다가, 다시 멀어진다..."
                c "(죽을 뻔했네. 앞으로는 플래그를 세우는 대사 따위 뱉지 않겠어.)"

                $ Checked_RestroomEvent = True
                jump Restroom

            "2번 칸":
                "당신은 2번 칸으로 잽싸게 들어갔다."
                "..."
                "발걸음 소리가 가까워진다..."
                c "아?"

                $ EndingType = "RestroomAssassin"
                jump GameOver

            "3번 칸":
                "당신은 3번 칸으로 잽싸게 들어갔다."
                "..."
                "발걸음 소리가 가까워진다..."
                c "아?"

                $ EndingType = "RestroomAssassin"
                jump GameOver

    else:
        menu:
            "문":
                "화장실에서 나가시겠습니까?"
                menu:
                    "화장실에서 나간다.":
                        jump DiningRoomMenu

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
    scene bg kitchen
    if FirstKitchen:
        $ FirstKitchen = False
        c "으, 추워... 엄청 서늘하다."
        c "무슨 엘사가 다녀갔나…"
        c "여기도 빨리 보고 나가야지."

    jump KitchenMenu

label KitchenMenu:

    $ Checked_Kitchen = True

    menu:
        "문":
            "부엌에서 나갈까?"
            menu:
                "부엌에서 나간다.":
                    jump DiningRoomMenu

                "더 둘러본다.":
                    jump KitchenMenu

        "수납장":
            "수납장을 열었다."
            if MP3 == False:
                c "...? 왜 여기에 {b}{color=ffd400}MP3 플레이어{/color}{/b}가 있지?"
                c "일단 챙겨둬야겠다."

                $ MP3 = True
                jump KitchenMenu

            else:
                c "그래, 상식적으로 텅 빈 수납장을 또 열어봤자 뭐가 생기진 않겠지."

                jump KitchenMenu

        "냉장고":
            "냉장고를 열었다."
            c "뭐라 감상평을 말하기에 민망할 정도로 텅 비어 있네."

            jump KitchenMenu

        "식칼":
            jump Knife

        "오븐":
            jump Oven

label Knife:
    if FirstKnife:
        $ FirstKnife = False
        c "악!"
        $ HP = max(HP - 20, 0)
        c "칼에 손이 베여 HP가 20 감소했습니다."

        if  HP <= 0:
                $ EndingType = "NoHP"
                jump GameOver

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
    
    jump KitchenMenu

label Storage:
    scene bg storage
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

                $ EndingType = "StorageAssassin"
                jump GameOver
                
            "돈을 챙기지 않는다.":
                c "아니지, 이 거지 같은 장소에 있는 돈 따위 가지고 싶지 않아."

    jump StorageMenu

label StorageMenu:

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
    scene bg quiz_room
    if FirstQuizRoom:
        $ FirstQuizRoom = False
        c "이게 전부 풀어야 하는 문제들인가...?"
        c "빨리 풀고 넘어가야겠어."
    
    if Cleared_ArtQuiz and Cleared_KoreanQuiz and Cleared_ScienceQuiz and Cleared_SocietyQuiz and Cleared_HistoryQuiz and Cleared_EnglishQuiz and Cleared_MathQuiz and Cleared_TechQuiz:
        "침실로 가는 문이 열렸다."
        jump QuizRoomMenu

    menu:
        "테라스 문":
            "테라스로 갈까?"
            menu:
                "테라스로 간다.":
                    jump Terrace
                "나가지 않는다.":
                    jump QuizRoom

        "미술" if not Cleared_ArtQuiz:
            jump ArtQuiz

        "국어" if not Cleared_KoreanQuiz:
            jump KoreanQuiz

        "과학" if not Cleared_ScienceQuiz:
            jump ScienceQuiz

        "사회" if not Cleared_SocietyQuiz:
            jump SocietyQuiz

        "역사" if not Cleared_HistoryQuiz:
            jump HistoryQuiz

        "영어" if not Cleared_EnglishQuiz:
            jump EnglishQuiz

        "수학" if not Cleared_MathQuiz:
            jump MathQuiz

        "기술가정" if not Cleared_TechQuiz:
            jump TechQuiz

label QuizRoomMenu:
    menu:
        "침실 문":
            "침실로 갈까?"
            menu:
                "침실로 간다.":
                    jump Bedroom

                "더 둘러본다.":
                    jump QuizRoomMenu

        "테라스 문":
            "테라스로 갈까?"
            menu:
                "테라스로 간다.":
                    jump Terrace

                "나가지 않는다.":
                    jump QuizRoomMenu

        "미술" if not Cleared_ArtQuiz:
            jump ArtQuiz

        "국어" if not Cleared_KoreanQuiz:
            jump KoreanQuiz

        "과학" if not Cleared_ScienceQuiz:
            jump ScienceQuiz

        "사회" if not Cleared_SocietyQuiz:
            jump SocietyQuiz

        "역사" if not Cleared_HistoryQuiz:
            jump HistoryQuiz

        "영어" if not Cleared_EnglishQuiz:
            jump EnglishQuiz

        "수학" if not Cleared_MathQuiz:
            jump MathQuiz

        "기술가정" if not Cleared_TechQuiz:
            jump TechQuiz
        

label LifeCheck:
    if QuizLife <= 0:
        $ EndingType = "NoQuizLife"
        jump GameOver

    else:
        "남은 기회: [QuizLife]번"
        jump QuizRoom

label ArtQuiz:
    if not Cleared_ArtQuiz:
        show text "{size=30}{b}[[미술]{/b}\n\n다음은 그림과 관련된 지식입니다. 옳지 않은 것은 무엇인지 1, 2, 3 중 하나를 쓰세요.\n\n1. 금속처럼 반짝거리는 재질을 그리려면 검은색이나 어두운 색을 적극적으로 활용해야 한다.\n2. 팝 아트는 대중(Popular)과 예술(Art)의 합성어로 추상적인 기하학적 이미지를 미술 영역으로 수용한 순수미술의 한 경향을 가리킨다.\n3. 이 게임의 디자이너는 세계 최고의 그림러다." at truecenter
        $ Answer = renpy.input("정답을 입력하세요.").strip()
        hide text
        if Answer == "2":
            show text "{size=30}{b}정답입니다!{/b}" at truecenter
            pause 1.0
            hide text
            $ Cleared_ArtQuiz = True
            jump QuizRoom
        else:
            show text "{size=30}{b}틀렸습니다.{/b}" at truecenter
            pause 1.0
            hide text
            $ QuizLife -= 1
            jump LifeCheck
    
    else:
        "이미 미술 퀴즈를 통과했습니다."
        jump QuizRoom

label KoreanQuiz:
    if not Cleared_KoreanQuiz:

        # 1번 문제 ------------------------------------------------------------------
        show text "{size=30}{b}[[국어]{/b}\n\n아래 문장에서 둘 중 옳은 표현은 무엇인가요?\n\n1. 나는 [[곰곰히 / 곰곰이] 생각했다." at truecenter
        $ Answer = renpy.input("정답을 입력하세요.").strip()
        hide text

        if Answer == "곰곰이":
            show text "{size=30}{b}정답입니다!{/b}" at truecenter
            pause 1.0
            hide text
        else:
            jump KoreanWrongAnswer

        # 2번 문제 ------------------------------------------------------------------
        show text "{size=30}{b}[[국어]{/b}\n\n아래 문장에서 둘 중 옳은 표현은 무엇인가요?\n\n2. [[재작년 / 제작년] 매출보다 높네." at truecenter
        $ Answer = renpy.input("정답을 입력하세요.").strip()
        hide text

        if Answer == "재작년":
            show text "{size=30}{b}정답입니다!{/b}" at truecenter
            pause 1.0
            hide text
        else:
            jump KoreanWrongAnswer

        # 3번 문제 ------------------------------------------------------------------
        show text "{size=30}{b}[[국어]{/b}\n\n아래 문장에서 둘 중 옳은 표현은 무엇인가요?\n\n3. [[맞힐 / 맞출] 수 있으면 해봐." at truecenter
        $ Answer = renpy.input("정답을 입력하세요.").strip()
        hide text

        if Answer == "맞힐":
            show text "{size=30}{b}정답입니다!{/b}" at truecenter
            pause 1.0
            hide text
            $ Cleared_KoreanQuiz = True
            jump QuizRoom
        else:
            jump KoreanWrongAnswer
    
    else:
        "이미 국어 퀴즈를 통과했습니다."
        jump QuizRoom 

label KoreanWrongAnswer:

    $ QuizLife -= 1

    show text "{size=30}{b}틀렸습니다.{/b}" at truecenter
    pause 1.0
    hide text

    if QuizLife <= 0:
        jump LifeCheck

    "남은 기회: [QuizLife]번"

    jump KoreanQuiz

label ScienceQuiz:
    if not Cleared_ScienceQuiz:
        show text "{size=30}{b}[[과학]{/b}\n\n다음 화학 반응에서의 세 규칙 중 부피와 관련된 것은 무엇인지 1, 2, 3 중 하나를 쓰세요.\n\n1. 질량 보존 법칙\n2. 일정 성분비 법칙\n3. 기체 반응 법칙" at truecenter
        $ Answer = renpy.input("정답을 입력하세요.").strip()
        hide text
        if Answer == "3":
            show text "{size=30}{b}정답입니다!{/b}" at truecenter
            pause 1.0
            hide text
            $ Cleared_ScienceQuiz = True
            jump QuizRoom
        else:
            show text "{size=30}{b}틀렸습니다.{/b}." at truecenter
            pause 1.0
            hide text
            $ QuizLife -= 1
            jump LifeCheck
    
    else:
        "이미 과학 퀴즈를 통과했습니다."
        jump QuizRoom

label SocietyQuiz:
    if not Cleared_SocietyQuiz:
        show text "{size=30}{b}[[사회]{/b}\n\n기회비용의 의미로 알맞은 것은 무엇인지 1, 2, 3, 4 중 하나를 쓰세요.\n\n1. 어떤 주식을 매수했을 때 특정 기간 동안의 예상 이익에서 예상 손해액을 뺀 것\n2. 경제에서 여러 선택지 중 하나를 선택했을 때 그 선택으로 인해 포기해야 하는 대안 중 가장 가치가 큰 것\n3. 어떤 후보자가 특정 선거 전략을 펼쳤을 때 그로 인해 지지를 철회하는 지지자의 수와 선거 비용의 합\n4. 경제에서 이미 지출되어 어떤 선택을 하더라도 되돌릴 수 없는 비용" at truecenter
        $ Answer = renpy.input("정답을 입력하세요.").strip()
        hide text
        if Answer == "2":
            show text "{size=30}{b}정답입니다!{/b}" at truecenter
            pause 1.0
            hide text
            $ Cleared_SocietyQuiz = True
            jump QuizRoom
        else:
            show text "{size=30}{b}틀렸습니다.{/b}" at truecenter
            pause 1.0
            hide text
            $ QuizLife -= 1
            jump LifeCheck
        
    else:
        "이미 사회 퀴즈를 통과했습니다."
        jump QuizRoom

label HistoryQuiz:
    if not Cleared_HistoryQuiz:
        show text "{size=30}{b}[[역사]{/b}\n\n사건과 설명이 옳지 않게 짝지어진 것은 무엇인지 1, 2, 3, 4, 5 중 하나를 쓰세요.\n\n1. 제주 4.3 사건: 경찰 발포 사건으로 시작된 제주 주민들의 무장 봉기에 대해 미군정과 예하의 국군, 경찰이 자행한 민간인 학살 사건\n2. 동학 농민 혁명: 전봉준을 중심으로 한 농민들이 탐관오리의 착취와 외세의 침략에 저항하며 개혁을 요구한 농민 봉기\n3. 3.1 운동: 한반도 전역과 세계 각지의 한인 밀집 지역에서 시민들이 독립을 선언하며 일제의 강점에 저항권을 행사한 시민 불복종 운동이자 독립운동\n4.  6.25 전쟁: 북한 공산 정권이 한반도 적화 통일을 목적으로 선전포고 없이 38선을 넘어 남침하여 시작된 전쟁\n5. 6월 항쟁: 전두환 정권의 장기집권 의도에 시민들이 ’호헌철폐 독재타도 민주쟁취‘ 등을 외치며 일어났으나, 대통령 직선제를 쟁취하는 데는 실패한 민주화 운동" at truecenter
        $ Answer = renpy.input("정답을 입력하세요.").strip()
        hide text
        if Answer == "5":
            show text "{size=30}{b}정답입니다!{/b}" at truecenter
            pause 1.0
            hide text
            $ Cleared_HistoryQuiz = True
            jump QuizRoom
        else:
            show text "{size=30}{b}틀렸습니다.{/b}" at truecenter
            pause 1.0
            hide text
            $ QuizLife -= 1
            jump LifeCheck

    else:
        "이미 역사 퀴즈를 통과했습니다."
        jump QuizRoom

label EnglishQuiz:
    if not Cleared_EnglishQuiz:
        show text "{size=30}{b}[[영어]{/b}\n\n다음 중 어법적으로 옳은 문장은 무엇인지 1, 2, 3 중 하나를 쓰세요.\n\n1. Never have I been to Korea.\n2. What you said yesterday were so terrible that I almost threw up.\n3. Do you know what he told to me?" at truecenter
        $ Answer = renpy.input("정답을 입력하세요.").strip()
        hide text
        if Answer == "1":
            show text "{size=30}{b}정답입니다!{/b}" at truecenter
            pause 1.0
            hide text
            $ Cleared_EnglishQuiz = True
            jump QuizRoom
        else:
            show text "{size=30}{b}틀렸습니다.{/b}" at truecenter
            pause 1.0
            hide text
            $ QuizLife -= 1
            jump LifeCheck

    else:
        "이미 영어 퀴즈를 통과했습니다."
        jump QuizRoom

label MathQuiz:
    if not Cleared_MathQuiz:
        show text '{size=30}{b}[[수학]{/b}\n\n곽철이와 제임스가 함께 급식을 먹으러 가고 있었습니다.\n{b}{color=ffd400}제임스{/color}{/b}가 학생 A와 B의 삼각형 모양 머리를 보고 이렇게 말했습니다.\n"학생 A의 머리의 한 각이 학생 B의 머리의 한 각과 같고, 그 각들의 대변의 길이가 각각 같으므로 학생 A의 머리와 학생 B의 머리는 합동이야."\n\n그러자 {b}{color=ffd400}곽철이{/color}{/b}가 이렇게 말했습니다.\n"네 삼각형 모양 머리를 수직으로 가르는 직선을 그리면 그 직선의 그래프는 a가 0이 아닌 y=ax의 그래프로 나타나는데,\n이때 이 그래프는 a의 값과 관계 없이 반드시 (0, 1)의 점을 지나. 그러니까 네 두개골을 수직으로 가르는 직선을 그어 버리기 전에 조용히 하면 안 될까?"\n\n그때 지나가던 {b}{color=ffd400}{한권택}{/color}{/b}이 이렇게 말했습니다.\n"이차방정식을 푸는 방법 중 하나인 인수분해는 각각 수 또는 식인 A와 B의 곱이 0일 때, A와 B 중 하나는 무조건 0이라는 원리를 이용해."\n\n마지막으로 그들을 발견한 {b}{color=ffd400}오르테}{/color}{/b}가 말했습니다.\n"어떤 소수를 기약분수로 바꾸어 나타낼 때, 분모의 소인수가 2, 3, 5뿐이면 그것은 유한소수이고 그렇지 않다면 그것은 순환소수야."\n\n\n위 글에서 옳은 말을 한 사람은 누구인지 [[{b}{color=ffd400}제임스, 곽철이, 한권택, 오르테{/color}{/b}] 중 맞는 것을 모두 쓰시오.' at truecenter
        $ Answer = renpy.input("정답을 입력하세요.").strip()
        hide text
        if Answer == "한권택":
            show text "{size=30}{b}정답입니다!{/b}" at truecenter
            pause 1.0
            hide text
            $ Cleared_MathQuiz = True
            jump QuizRoom
        else:
            show text "{size=30}{b}틀렸습니다.{/b}" at truecenter
            pause 1.0
            hide text
            $ QuizLife -= 1
            jump LifeCheck
    
    else:
        "이미 수학 퀴즈를 통과했습니다."
        jump QuizRoom

label TechQuiz:
    if not Cleared_TechQuiz:
        show text "{size=30}{b}[[기술]{/b}\n\n벌꿀을 채취해 오세요." at truecenter
        pause 2.0
        hide text
        menu:
            "뒤로 가기":
                jump QuizRoom

            "{color=ffd400}유리병{/color} 가져가기":
                if GlassBottle or Honey_GlassBottle:
                    "{color=ffd400}유리병{/color}을 이미 보유하고 있습니다."
                    jump QuizRoom
            
                else:
                    "{color=ffd400}유리병{/color}을 얻었습니다."
                    $ GlassBottle = True
                    jump QuizRoom
            
            "{color=ffd400}꿀이 든 병{/color} 제출하기":
                if Honey_GlassBottle:
                    "기술 가정 퀴즈를 통과했습니다."
                    $ Cleared_TechQuiz = True
                    $ Honey_GlassBottle = False
                    jump QuizRoom
            
                else:
                    "{color=ffd400}꿀이 든 병{/color}을 보유하고 있지 않습니다."
                    jump QuizRoom
        
    else:
        "이미 기술가정 퀴즈를 통과했습니다."
        jump QuizRoom
        
# ====================================================================================

label Terrace:
    scene bg terrace
    if FirstTerrace:
        $ FirstTerrace = False
        c "여기에는 지하실도 있고, 테라스도 있고 별의별 게 다 있냐…"
        c "저건 뭐지?"
        c "벌집이잖아! 이게 뭔 거지 같은 경우지?"
    
    jump TerraceMenu

label TerraceMenu:
    menu:
        "문":
            "테라스에서 나가시겠습니까?"
            menu:
                "테라스에서 나간다.":
                    jump QuizRoom

                "더 둘러본다.":
                    jump TerraceMenu

        "벌집":
            if GlassBottle:
                menu:
                    "벌꿀을 채취한다.":
                        $ Honey_GlassBottle = True
                        $ GlassBottle = False
                        "{color=ffd400}꿀이 든 병{/color}을 얻었습니다."
                        jump  TerraceMenu

                    "채취하지 않는다.":
                        jump TerraceMenu
                
            elif Honey_GlassBottle:
                "이미 벌꿀을 채취했습니다."
                jump TerraceMenu
            
            else:
                "벌꿀을 채취하려면 {color=ffd400}유리병{/color}이 필요합니다."
                jump TerraceMenu

        "오브젝트":
            "~~을 조사했습니다."
            jump TerraceMenu
    

label Bedroom:
    scene bg bedroom
    "침실." # 임시
    jump GameClear
