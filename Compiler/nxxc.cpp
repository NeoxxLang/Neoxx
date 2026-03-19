#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    std::string cmd = "python nxxc.py ";
    if (argc > 1) cmd += argv[1];
    system(cmd.c_str());
}
