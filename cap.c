#include <stdio.h>
#define MAXMODS 50

typedef struct {
    char mod[8];
    char grade[3];
    int mc;
} result_t;

typedef struct {
    char name[31];
    result_t results[MAXMODS];
} student_t;

void convertGrade(result_t [], float [], int);
float computeCAP(result_t [], float[], int);

int main(void) {
    student_t student;
    int numOfMods, i;
    float CAP, gradePoint[MAXMODS] = {0};

    printf("Enter student's name: ");
    scanf("%s", &student.name);

    printf("Enter number of modules taken: ");
    scanf("%d", &numOfMods);

    printf("Enter results of %d mods\n", numOfMods);

    for(i=0;i<numOfMods;i++) {
        scanf("%s %s %d", &student.results[i].mod, &student.results[i].grade, &student.results[i].mc);
    }

    convertGrade(student.results, gradePoint, numOfMods);

    printf("Result: %f", computeCAP(student.results, gradePoint, numOfMods));
}

void convertGrade(result_t results[], float gradePoint[], int numOfMods){
    float gradePtArr[] = {5, 3.5, 2, 1, 0};
    int i;
    char grade, halfGrade;

    for(i = 0; i < numOfMods; i++){
        grade = results[i].grade[0] - 'A';
        halfGrade = results[i].grade[1];
        gradePoint[i] = gradePtArr[grade];

        //if + or - in the grade increase or decrease appropriately
        // except when grade is A+
        if (halfGrade == '+' && grade != 0)
            gradePoint[i] += 0.5;
        else if (halfGrade == '-')
            gradePoint[i] -= 0.5;
    }
}

float computeCAP(result_t results[], float gradePoint[], int numOfMods){
    int i, mcSum = 0, mc;
    float gradeSum = 0;

    for (i = 0; i < numOfMods; i++){
        mc = results[i].mc;
        gradeSum += gradePoint[i]*(float)mc;
        mcSum += mc;
    }
    return gradeSum / (float)mcSum;
}
