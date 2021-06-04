#include <Windows.h> 

int main() { 
  // Uncomment next line if you don't need output at all
  //FreeConsole();
  WinExec("main\\main.exe", SW_HIDE);
  return 0; 
}