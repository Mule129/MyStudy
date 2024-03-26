#include <string>
#include <random>
#include <time.h>

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

int randInt(int min, int max);

int x, y;
int werstInput;
int snakeArray[BOARD_SIZE*BOARD_SIZE][1] = {0};
int snakeNotArray[BOARD_SIZE*BOARD_SIZE][1] = {0};
int snakeLength;


int handleInput() {
    if (console::key(console::K_UP)) {
        werstInput = 1;
        return 1;
    } 
    if (console::key(console::K_DOWN)) {
        werstInput = -1;
        return -1;
    } 
    if (console::key(console::K_LEFT)) {
        werstInput = -2;
        return -2;
    } 
    if (console::key(console::K_RIGHT)) {
        werstInput = 2;
        return 2;
    }
    if (console::key(console::K_ESC)) {
        werstInput = 0;
        return 0;
    }
    if (console::key(console::K_ENTER)) {
        werstInput = 10;
        return 10;
    }

    return werstInput;
}

void initGameSetting() {
    x = BOARD_SIZE/2;
    y = BOARD_SIZE/2;
    
    snakeLength = 1;
    snakeArray[0][0] = x;
    snakeArray[0][1] = y;

    int snakeArray[BOARD_SIZE*BOARD_SIZE][1] = {0};

    werstInput = 2;

    console::draw(0, 0, WALL_LEFT_TOP_STRING);
    console::draw(BOARD_SIZE, BOARD_SIZE, WALL_RIGHT_BOTTOM_STRING);
    console::draw(0, BOARD_SIZE, WALL_LEFT_BOTTOM_STRING);
    console::draw(BOARD_SIZE, 0, WALL_RIGHT_TOP_STRING);

    console::draw(x, y, SNAKE_STRING);
}

void screenCleaer() {
    console::clear(1, console::SCREEN_WIDTH-1, 1, console::SCREEN_HEIGHT-1);
}

void snakePositionSave(int x, int y) {
    for (int i = snakeLength - 1; i > 0; i--) {
        snakeArray[snakeLength+1][0] = snakeArray[snakeLength][0];
        snakeArray[snakeLength+1][1] = snakeArray[snakeLength][1];
    }

    snakeArray[0][0] = x;
    snakeArray[0][1] = y;
    
}

bool eatApple(int x, int y) {
    if (1){
        console::draw(x, y, SNAKE_BODY_STRING);
        x = randInt(0, BOARD_SIZE);
        y = randInt(0, BOARD_SIZE);
        for (int i = 0; i < snakeLength; i++) {
            
        }
        console::draw(x, y, APPLE_STRING);
        return true;
    } else {

    }

}

bool snakeHeadCheck() {
    if (x >= BOARD_SIZE || y >= BOARD_SIZE || x <= 0 || y <= 0) {
        console::draw(
            BOARD_SIZE/2 - 4, BOARD_SIZE/2, "YOU LOST!"
        );
        console::draw(
            BOARD_SIZE/2 - 9, BOARD_SIZE/2+1, "Try again? (Enter)"
        );
        return true;
    } else if (eatApple(x, y)) {
        snakeLength++;
    }
    
    return false;
}



void controll() {

}


int game() {
    int delayCnt = 0;
    int score = 0;
    bool lossGame = false;
    std::string scoreText = "score: ";

    console::init();
    console::clear(1, 1, BOARD_SIZE-1, BOARD_SIZE-1);

    initGameSetting();

    while (true) {
        // console::clear(x, y);
        console::draw(x, y, SNAKE_BODY_STRING);

        int status = handleInput();

        if (status == 0) {
            break;
        } else if (status == 10 && lossGame) {
            console::clear();
            initGameSetting();
            lossGame = false;
            score = 0;
        }

        if (lossGame) {
            ;
        } else if (delayCnt < MOVE_DELAY) {
            delayCnt++;
        } else if (status == 2) {
            delayCnt = 0;
            x++;
        } else if (status == -2) {
            delayCnt = 0;
            x--;
        } else if (status == 1) {
            delayCnt = 0;
            y--;
        } else if (status == -1) {
            delayCnt = 0;
            y++;
        }
        
        
        console::draw(0, BOARD_SIZE + 1, "x: " + std::to_string(x));
        console::draw(0, BOARD_SIZE + 2, "y: " + std::to_string(y));
        console::draw(0, BOARD_SIZE + 4, "input: " + std::to_string(werstInput));
        console::draw(
            (BOARD_SIZE / 2) - (scoreText + std::to_string(score)).length()/2, 
            BOARD_SIZE + 1, 
            "score: " + std::to_string(score)
        );

        lossGame = snakeHeadCheck();
        
        console::wait();
    }   

    return 0;
}