#include <stdio.h>

// 최대공약수 계산 함수
int try1(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    int a, b, z;
    scanf("%d %d", &a, &b);
    scanf("%d", &z);

    while (z--) {
        int c, d, e;
        scanf("%d %d %d", &c, &d, &e);

        if (c == 1) {
            if (d == e) {
                printf("%d\n", a + (d - 1) * b);
            } else if ((e - d) % 2 == 1) {
                int ans = ((a + (d - 1) * b) + (a + (e - 1) * b)) * ((e - d + 1) / 2);
                printf("%d\n", ans);
            } else {
                int ans = ((a + (d - 1) * b) + (a + (e - 1) * b)) * ((e - d) / 2) + ((a + (d - 1) * b) + (a + (e - 1) * b)) / 2;
                printf("%d\n", ans);
            }
        } else {
            if (b != 0) {
                if (d == e) {
                    printf("%d\n", a + (d - 1) * b);
                } else {
                    int f = try1(a + (d - 1) * b, a + (d - 1) * b + b);
                    for (int i = a + (d - 1) * b + b; i <= a + (e - 1) * b; i += b) {
                        if (f % i == 0) {
                            f = i;
                        } else if (i % f != 0) {
                            f = try1(i, f);
                            if (f == 1) {
                                break;
                            }
                        }
                    }
                    printf("%d\n", f);
                }
            } else {
                printf("%d\n", a);
            }
        }
    }

    return 0;
}
