#include <stdio.h>

int determineType(int, int, int, int, int, int, int, int);
float computeK(int, int, int, int);
void printMessage(int);

int main(void) {

	int Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, type;

	printf("Enter the coordinates of A: ");
	scanf("%d %d", &Ax, &Ay);
	printf("Enter the coordinates of B: ");
	scanf("%d %d", &Bx, &By);
	printf("Enter the coordinates of C: ");
	scanf("%d %d", &Cx, &Cy);
	printf("Enter the coordinates of D: ");
	scanf("%d %d", &Dx, &Dy);

	type = determineType(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy);
	printMessage(type);

	return 0;
}

int determineType(int Ax, int Ay, int Bx, int By, int Cx, int Cy, int Dx, int Dy) {
	int AB, AC, CD;

	AB = computeK(Ax, Ay, Bx, By);
	AC = computeK(Ax, Ay, Cx, Cy);
	CD = computeK(Cx, Cy, Dx, Dy);

	// if AB and CD have different slopes, must intersect
	if (AB != CD)
        return 2;
    // over here, AB must be parallel to CD
    // if AB == AC then must be overlapping
    else if (AB == AC)
        return 3;
    // otherwise parallel
    else
        return 1;

	/*
	if(AB == CD && ((AB || CD) != AC)) {
		return 1;
	} else if (AB != CD) {
		return 2;
	} else if (AB == CD && AB == AC && CD == AC) {
		return 3;
	}
	*/

	return 0;
}

float computeK(int Ax, int Ay, int Bx, int By) {
	float k;

	k = (Ay - By)/(Ax - Bx);

	return k;
}

void printMessage(int type) {
	if(type == 1) {
		printf("The two lines are parallel.\n");
	} else if(type == 2) {
		printf("The two lines are intersecting.\n");
	} else if(type == 3) {
		printf("The two lines are overlapping.\n");
	}
}
