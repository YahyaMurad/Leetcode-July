#include <bits/stdc++.h>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        int idx=1;
        int fstIdx=-1;
        int sndIdx=-1;
        ListNode*a=head;
        ListNode*b=head->next;
        ListNode*c=head->next->next;
        if(c==NULL) return {-1,-1};
        int minDistance =INT_MAX;
        int _1stIdx=-1;
        int _2ndIdx=-1;
        while(c){
            if((b->val < a->val && b->val < c->val)||(b->val > a->val && b->val > c->val)){
                // for maximum distance
                if(fstIdx==-1) fstIdx=idx;
                else sndIdx=idx;
                // for minimum distance
                _1stIdx=_2ndIdx;
                _2ndIdx=idx;
                if(_1stIdx!=-1){
                    int distance=_2ndIdx-_1stIdx;
                    minDistance=min(minDistance,distance);
                }
            }
            a=a->next;
            b=b->next;
            c=c->next;
            idx++;
        }
        // if  there is only one critical point or zero critical point
        if(sndIdx==-1) return {-1,-1};
        int maxDistance = sndIdx-fstIdx;
        return {minDistance,maxDistance};
    }
};