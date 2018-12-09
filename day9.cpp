#include <stdio.h>
#include <list>
#include <vector>

#define PLAYERS     466
#define MARBLES     7143600

int main() {
    std::list<long> l;
    l.push_back(0);
    std::vector<long> scores(PLAYERS, 0);
    auto it = l.begin();
    int player = 1;

    for (long i = 1; i <= MARBLES; i++) {

        if (i % 23) {
            // go one step to the right, then insert
            // which means go 2 steps to the right and then insert
            for (int k = 0; k < 2; k++) {
                if (it == l.end()) {
                    it = l.begin();
                }
                it++;

            }

            l.insert(it, i);
            it--;
            // are we at new marble?
        } else {
                scores[player] += i;
            // go 7 steps back and remove
            for (int k  = 0; k < 7; k++) {
                if (it == l.begin()) {
                    it = l.end();
                }
                it--;
            }
            scores[player] += *it;
            l.erase(it);
            it++;
        }

        player  = (player + 1) % PLAYERS;
    }

    auto max_it = max_element(std::begin(scores), std::end(scores)); // c++11
    printf("Max score: %ld\n", *max_it);

    return 0;
}
