#include <cstring>
#include <cstdlib>
#include <ctime>
#include "console.h"

#define BOARD_SIZE 20
#define MOVE_DELAY 15
#define WALL_VERTICAL_STRING "┃"
#define WALL_HORIZONTAL_STRING "━"
#define WALL_RIGHT_TOP_STRING "┓"
#define WALL_LEFT_TOP_STRING "┏"
#define WALL_RIGHT_BOTTOM_STRING "┛"
#define WALL_LEFT_BOTTOM_STRING "┗"
#define SNAKE_STRING "■"
#define SNAKE_BODY_STRING "■"
#define APPLE_STRING "●"

#define LOST_COMMENT1 "YOU LOST!"
#define LOST_COMMENT2 "Try again? (Enter)"

struct PositionInfo {
    int x;
    int y;

    bool operator==(const PositionInfo &other) {
        return this->x == other.x && this->y == other.y;
    }
};

enum GameState {
    PLAYING,
    OVER
};

PositionInfo snakePosition;
PositionInfo applePosition;

console::Key recentHandleInput = console::K_NONE; // -1: pending
int score = 0;

PositionInfo recentSnakePosition[BOARD_SIZE * BOARD_SIZE] = {};

PositionInfo randomAppleList[BOARD_SIZE * BOARD_SIZE] = {};

console::Key handleInput(GameState state) {
    // 키 입력 상태를 받는다.
    switch (state) {
        case PLAYING:
            if (console::key(console::K_LEFT) && (recentHandleInput != console::K_RIGHT || score == 0)) {
                recentHandleInput = console::K_LEFT;
            }
            if (console::key(console::K_RIGHT) && (recentHandleInput != console::K_LEFT || score == 0)) {
                recentHandleInput = console::K_RIGHT;
            }
            if (console::key(console::K_UP) && (recentHandleInput != console::K_DOWN || score == 0)) {
                recentHandleInput = console::K_UP;
            }
            if (console::key(console::K_DOWN) && (recentHandleInput != console::K_UP || score == 0)) {
                recentHandleInput = console::K_DOWN;
            }
            break;
        case OVER:
            if (console::key(console::K_ENTER)) {
                recentHandleInput = console::K_ENTER;
            }
            break;
    }
    if (console::key(console::K_ESC)) {
        recentHandleInput = console::K_ESC;
    }
    return recentHandleInput;
}

void restrictInScreen() {
    // x, y 위치를 화면의 최대 크기에서 벗어나지 않게 한다.
    if (snakePosition.x < 0)
        snakePosition.x = 0;
    if (snakePosition.x >= console::SCREEN_WIDTH)
        snakePosition.x = console::SCREEN_WIDTH - 1;
    if (snakePosition.y < 0)
        snakePosition.y = 0;
    if (snakePosition.y >= console::SCREEN_HEIGHT)
        snakePosition.y = console::SCREEN_HEIGHT - 1;
}

void followSnakePosition() {
    // 뱀의 이전 위치 정보를 저장한다.
    for (int i = 0; i < score; i++) {
        recentSnakePosition[score - i].x = recentSnakePosition[score - 1 - i].x;
        recentSnakePosition[score - i].y = recentSnakePosition[score - 1 - i].y;
    }

    recentSnakePosition[0] = snakePosition;
}

// change apple postion
void placeApple() {
    int index = 0;
    int data[BOARD_SIZE][BOARD_SIZE] = {0};
    
    for (int i = 0; i < score; i++) {
        data[recentSnakePosition[i].x][recentSnakePosition[i].y] = 1;
    }
    for (int i = 1; i < BOARD_SIZE; i++) {
        for (int j = 1; j < BOARD_SIZE; j++) {
            if (data[i][j] != 1) {
                randomAppleList[index].x = i;
                randomAppleList[index].y = j;
                index++;
            }
        }
    }
    applePosition = {
        randomAppleList[rand() % (index - 1)].x,
        randomAppleList[rand() % (index - 1)].y
    };
}

/* 출력 함수 모음 */
void printApple() {
    // 사과를 배치한다.
    console::draw(applePosition.x, applePosition.y, APPLE_STRING);
}

void printSnake() {
    // 뱀을 배치한다.
    for (int i = 0; i < score + 1; i++) {
        console::draw(recentSnakePosition[i].x, recentSnakePosition[i].y, SNAKE_BODY_STRING);
    }
}

void clearScreen(int x_1 = 1, int x_2 = BOARD_SIZE, int y_1 = 1, int y_2 = BOARD_SIZE) {
    for (int i = x_1; i < x_2; i++) {
        for (int j = y_1; j < y_2; j++) {
            console::draw(i, j, " ");
        }
    }
}

// 화면의 프레임을 출력한다.
void printFrame() {
    for (int i = 0; i < BOARD_SIZE; i++) {
        console::draw(i, 0, WALL_HORIZONTAL_STRING);
        console::draw(i, BOARD_SIZE, WALL_HORIZONTAL_STRING);
    }
    for (int i = 0; i < BOARD_SIZE; i++) {
        console::draw(0, i, WALL_VERTICAL_STRING);
        console::draw(BOARD_SIZE, i, WALL_VERTICAL_STRING);
    }
    console::draw(0, 0, WALL_LEFT_TOP_STRING);
    console::draw(BOARD_SIZE, BOARD_SIZE, WALL_RIGHT_BOTTOM_STRING);
    console::draw(0, BOARD_SIZE, WALL_LEFT_BOTTOM_STRING);
    console::draw(BOARD_SIZE, 0, WALL_RIGHT_TOP_STRING);
}


void printText() {

    // 정보
    // console::draw(0, BOARD_SIZE + 1, "x: " + std::to_string(x));
    // console::draw(0, BOARD_SIZE + 2, "y: " + std::to_string(y));
    console::draw(
            (BOARD_SIZE / 2) - ("score: " + std::to_string(score*10)).length() / 2,
            BOARD_SIZE + 1,
            "score: " + std::to_string(score*10)
    );
    // for (int i = 0; i < score; i ++) {
    //     console::draw(0, BOARD_SIZE + i + 5, "snake position (X): " + std::to_string(snakePosition[i][0]));
    // }
}

/* 게임 종료 조건 함수 모음 */
bool isRestrict() {
    // 뱀이 게임 밖으로 탈출했는가?
    return snakePosition.x == 0 ||
           snakePosition.y == 0 ||
           snakePosition.x >= BOARD_SIZE ||
           snakePosition.y >= BOARD_SIZE;
}

bool isCrash() {
    // 뱀이 충돌했는가?
    for (int i = 1; i < score + 1; i++) {
        if (snakePosition == recentSnakePosition[i])
            return true;
    }
    return false;
}

void initialization() {
    // 게임 초기 설정
    console::clear();
    snakePosition.x = BOARD_SIZE / 2;
    snakePosition.y = BOARD_SIZE / 2;
    score = 0;
    recentHandleInput = console::K_RIGHT;

    placeApple();
    followSnakePosition();

    printFrame();

}    

void game() {
    int tickRate = 0;
    console::Key inputKey;

    GameState state = PLAYING;
    srand(time(NULL));

    // 콘솔 라이브러리를 초기화한다.
    console::init();

    initialization();

    while (true) {
        clearScreen();
        inputKey = handleInput(state);

        if (state == PLAYING) {
            if (tickRate >= MOVE_DELAY) {
                tickRate = 0;

                if (inputKey == console::K_LEFT) {
                    snakePosition.x--;
                } else if (inputKey == console::K_RIGHT) {
                    snakePosition.x++;
                } else if (inputKey == console::K_UP) {
                    snakePosition.y--;
                } else if (inputKey == console::K_DOWN) {
                    snakePosition.y++;
                }
                restrictInScreen();
                followSnakePosition();

                // 점수 or 게임 오버 부분
                if (applePosition == snakePosition) {
                    score++;
                    placeApple();
                }

                if (isCrash() || isRestrict()) {
                    state = OVER;
                }
            }
            tickRate++;
        } else if (state == OVER) {
            console::draw(
                    BOARD_SIZE / 2 - strlen(LOST_COMMENT1) / 2,
                    BOARD_SIZE / 2,
                    LOST_COMMENT1
            );
            console::draw(
                    BOARD_SIZE / 2 - strlen(LOST_COMMENT2) / 2,
                    BOARD_SIZE / 2 + 1,
                    LOST_COMMENT2
            );

            if (inputKey == console::K_ENTER) {
                initialization();
                state = PLAYING;
            }
        }

        // Exit game
        if (inputKey == console::K_ESC) {
            break;
        }

        // 출력 부분
        printApple();
        printSnake();
        printText();
        
        // 화면을 갱신하고 다음 프레임까지 대기한다.
        console::wait();
    }
}
