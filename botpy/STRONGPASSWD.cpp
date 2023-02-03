#include <bits/stdc++.h>
using namespace std;

bool checkKey(string str)
{
    if (str.size() < 8)
        return false;
    int checkNum = 0, checkChar = 0, checkChar2 = 0;
    for (int i = 0; i < str.size(); i++)
    {
        if (str[i] >= 'A' && str[i] <= 'Z')
        {
            checkChar = 1;
        }
        if (str[i] >= '0' && str[i] <= '9')
        {
            checkNum = 1;
        }
        if (str[i] >= 'a' && str[i] <= 'z')
        {
            checkChar2 = 1;
        }
    }
    if (checkNum && checkChar && checkChar2)
        return true;
    return false;
}

bool checkCharSpecical(string str)
{
    if (str.size() < 8)
        return false;
    string check = "!@#$%^&*()-+";
    for (int i = 0; i < str.size(); i++)
    {
        for (int j = 0; j < check.size(); j++)
        {
            if (str[i] == check[j])
            {
                return true;
            }
        }
    }
    return false;
}
bool checkLoop(string str)
{
    for (int i = 0; i < str.size() - 1; i++)
    {
        if (str[i] == str[i + 1])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    string str;
    cin >> str;
    if (checkCharSpecical(str) && checkKey(str) && checkLoop(str))
    {
        cout << "YES";
    }
    else
        cout << "NO";
}