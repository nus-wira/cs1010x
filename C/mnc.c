#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAXDAYS 10000

typedef struct{
    char *projectName;
    char *clientName;
    int startDay;
    int endDay;
    int manpower;
    double profit;
} project;

double cal_profit(project [], int, char*);
int busiestDay(project [], int);
int countProjects(project [], int, int);


int main(void){
    project p[]={{"p1","c1",1, 7, 1, 4},{"p2","c1",5, 9, 1, 2}, {"p3","c1",3, 5, 1, 3}};
    printf("%f\n", cal_profit(p, 3, "c1"));
    printf("%d\n", busiestDay(p, 3));
    return 0;

}

double cal_profit(project p[], int n, char* c){
    int i;
    double sum = 0;
    for (i = 0; i < n; i++){
        if (!strcmp(p[i].clientName, c))
            sum += p[i].profit;
    }
    return sum;
}

int busiestDay(project p[], int n){
    int i, most = 0, curr_count, day = 0;
    for (i = 0; i <= MAXDAYS; i++){
        curr_count = countProjects(p, n, i);
        if (curr_count > most){
            day = i;
            most = curr_count;
        }
    }
    return day;
}

int countProjects(project p[], int n, int day){
    int i, count = 0;
    for (i = 0; i < n; i++){
        if (p[i].startDay <= day && p[i].endDay >= day)
            count++;
    }
    return count;
}
