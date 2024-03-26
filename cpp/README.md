# CPP Practice Folder
This folder where learning contents about cpp are saved.
If you find filename file, go to `./cpp/filename`. you can fine filename cpp file.

## Run cpp file

window powershell, g++ compiler
```powershell
cd ./cpp/filename
g++ -Werror -c ./*.cpp
g++ ./*.o -o filename.exe
./filename.exe
```

e.g ) I want run snake game

Window powershell, g++ compiler
```powershell
git checkout snake
cd ./cpp/snake
g++ -Werror -c ./*.cpp
g++ ./*.o -o snake.exe
./snake.exe
```
