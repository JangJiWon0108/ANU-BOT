# emoji_moving.py
# 이모지 이동시키는 UI 파일
# HTML/CSS/JavaScript를 이용한 이모지 애니메이션

# ==================================== 이모지를 입력받아 에니메이션 생성(고래) =======================
def f_emoji_moving_whale():
    character_js = """
    <div id="character" style="font-size: 35px; position: absolute; top: 0px;">🐳</div>

    <script>
    let position = 0;
    const character = document.getElementById('character');
    const containerWidth = window.innerWidth;

    function move() {
        position += 1;
        if (position > containerWidth) {
            position = -50;  // 이모지가 컨테이너 밖으로 나가면 왼쪽으로 재설정
        }
        character.style.left = position + 'px';
        requestAnimationFrame(move);
    }
    move();
    </script>
    """

    return character_js

# ==================================== 이모지를 입력받아 에니메이션 생성(튤립) =======================
def f_emoji_moving_tulip():
    character_js = """
    <div id="character" style="font-size: 35px; position: absolute; top: 0px;">🌷</div>

    <script>
    let position = 0;
    const character = document.getElementById('character');
    const containerWidth = window.innerWidth;

    function move() {
        position += 1;
        if (position > containerWidth) {
            position = -50;  // 이모지가 컨테이너 밖으로 나가면 왼쪽으로 재설정
        }
        character.style.left = position + 'px';
        requestAnimationFrame(move);
    }
    move();
    </script>
    """

    return character_js

# ==================================== 이모지를 입력받아 에니메이션 생성(단풍) =======================
def f_emoji_moving_maple():
    character_js = """
    <div id="character" style="font-size: 35px; position: absolute; top: 0px;">🍁</div>

    <script>
    let position = 0;
    const character = document.getElementById('character');
    const containerWidth = window.innerWidth;

    function move() {
        position += 1;
        if (position > containerWidth) {
            position = -50;  // 이모지가 컨테이너 밖으로 나가면 왼쪽으로 재설정
        }
        character.style.left = position + 'px';
        requestAnimationFrame(move);
    }
    move();
    </script>
    """

    return character_js

# ==================================== 이모지를 입력받아 에니메이션 생성(병아리) =======================
def f_emoji_moving_chicken():
    character_js = """
    <div id="character" style="font-size: 35px; position: absolute; top: 0px;">🐤</div>

    <script>
    let position = 0;
    const character = document.getElementById('character');
    const containerWidth = window.innerWidth;

    function move() {
        position += 1;
        if (position > containerWidth) {
            position = -50;  // 이모지가 컨테이너 밖으로 나가면 왼쪽으로 재설정
        }
        character.style.left = position + 'px';
        requestAnimationFrame(move);
    }
    move();
    </script>
    """

    return character_js

# ==================================== 이모지를 입력받아 에니메이션 생성(벌) =======================
def f_emoji_moving_bee():
    character_js = """
    <div id="character" style="font-size: 35px; position: absolute; top: 0px;">🐝</div>

    <script>
    let position = 0;
    const character = document.getElementById('character');
    const containerWidth = window.innerWidth;

    function move() {
        position += 1;
        if (position > containerWidth) {
            position = -50;  // 이모지가 컨테이너 밖으로 나가면 왼쪽으로 재설정
        }
        character.style.left = position + 'px';
        requestAnimationFrame(move);
    }
    move();
    </script>
    """

    return character_js


# ==================================== 이모지를 입력받아 에니메이션 생성(강아지) =======================
def f_emoji_moving_dog():
    character_js = """
    <div id="character" style="font-size: 35px; position: absolute; top: 0px;">🐶</div>

    <script>
    let position = 0;
    const character = document.getElementById('character');
    const containerWidth = window.innerWidth;

    function move() {
        position += 1;
        if (position > containerWidth) {
            position = -50;  // 이모지가 컨테이너 밖으로 나가면 왼쪽으로 재설정
        }
        character.style.left = position + 'px';
        requestAnimationFrame(move);
    }
    move();
    </script>
    """
    
    return character_js