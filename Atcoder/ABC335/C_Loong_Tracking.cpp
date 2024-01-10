#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,q;
    cin >> n >> q;
    deque<pair<int,int> > que;
    for (int i = n;i>0;i--){
        que.push_back(make_pair(i,0));
    }
    for (int m = 0;m<q;m++){
        int type;
        cin >> type;
        if (type==1){
            // Move the dragon head
            char movement;
            cin >> movement;
            if (movement =='U'){
                que.push_back(make_pair(que.back().first, que.back().second + 1));
            }
            else if (movement == 'D'){
                que.push_back(make_pair(que.back().first, que.back().second - 1));
            }
            else if (movement == 'L'){
                que.push_back(make_pair(que.back().first-1, que.back().second));
            }
            else if (movement == 'R'){
                que.push_back(make_pair(que.back().first+1, que.back().second));
            }
            que.pop_front();
        }
        else {
            //track point
            int pos;
            cin >> pos;
            pair<int, int> coords = que.at(que.size()-pos);
            cout << coords.first << " " << coords.second << endl;
        }
    }
}