// #include <bits/stdc++.h>
// using namespace std;
// int main()
// {
//     int a, b, L;
//     cin >> a >> b >> L;
//     int x[a][b];
//     double g[a][b];
//     int nm[L];
//     for (int i = 0; i < L; i++)
//     {
//         nm[i] = 0;
//     }
//     for (int i = 0; i < a; i++)
//     {
//         for (int j = 0; j < b; j++)
//         {
//             cin >> x[i][j];
//             // for(int k = 0;k<L;k++){
//             // if(nm[k]==x[i][j]){
//             nm[x[i][j]] += 1;
//             // }
//             // }
//         }
//     }
//     double G[L];
//     for (int i = 0; i < L; i++)
//     {
//         G[i] = 0;
//     }

//     for (int i = 0; i < L; i++)
//     {
//         for (int j = 0; j <= i; j++)
//         {
//             G[i] += ((double)nm[j] / (a * b));
//         }
//         G[i] *= (L - 1);
//     }

//     for (int i = 0; i < a; i++)
//     {
//         for (int j = 0; j < b; j++)
//         {
//             g[i][j] = G[x[i][j]];
//         }
//     }
//     for (int i = 0; i < a; i++)
//     {
//         for (int j = 0; j < b; j++)
//         {
//             cout << round(g[i][j]) << " ";
//         }
//         cout << endl;
//     }
// }
#include<bits/stdc++.h>
using namespace std;
int main(){
    int a,b,L;
    cin>>a>>b>>L;
    int x[a][b];
    double g[a][b];
    int nm[L];
    for(int i=0;i<L;i++) nm[i]=0;
    for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            cin>>x[i][j];
            nm[x[i][j]]+=1;
        }
    }
    double G[L];
    for(int i=0;i<L;i++) G[i] = 0;
    for(int i=0;i<L;i++){
        for(int j= 0;j<=i;j++){
            G[i] += ((double)nm[j]/(a*b));
        }
        G[i] *=(L-1);
    }
    for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            cout<<round(G[x[i][j]])<<" ";
        }
        cout<<endl;
    }
}