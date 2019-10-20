// CS1010 AY2015/6 Semester 1
// PE2 Ex1: panel.c
// Name:
// Matriculation number:
// plab-id:
// Discussion group:
// Description:

#include <stdio.h>
#define GRID_SIZE 5
#define MAX_LENGTH 30

void readGrid(int grid[][GRID_SIZE]);
void printGrid(int grid[][GRID_SIZE]);
int readSequence(int sequence[]);
void press(int grid[][GRID_SIZE], int seq_len, int seq[]);
void press_1(int grid[][GRID_SIZE], int button);
int in_grid(int button);
void to_flip(int button, int arr[]);
void flip(int grid[][GRID_SIZE], int button);
int allOff(int grid[][GRID_SIZE], int *n);

int main(void) {
	int grid[GRID_SIZE][GRID_SIZE], sequence[MAX_LENGTH], length;
	int n_panels;

	readGrid(grid);

	length = readSequence(sequence);

	press(grid, length, sequence);

	if (allOff(grid, &n_panels))
        printf("All panels are off.\n");
	else {
        printf("Number of lighted panels: %d\n", n_panels);
        printGrid(grid);
	}

	return 0;
}

// Read the initial state of a grid
void readGrid(int grid[][GRID_SIZE]) {
	int i,j;

	printf("Enter grid:\n");

	for (i=0; i<GRID_SIZE; i++)
		for (j=0; j<GRID_SIZE; j++)
			scanf("%d", &grid[i][j]);
}

// Print the current grid
void printGrid(int grid[][GRID_SIZE]) {
	int i,j;

	for (i=0; i<GRID_SIZE; i++){
		for (j=0; j<GRID_SIZE; j++)
			printf("%d ", grid[i][j]);
		printf("\n");
	}
}

// Read the sequence of panels to be pressed
int readSequence(int sequence[]) {
	int i,length;

	printf("Enter length of sequence: ");
	scanf("%d", &length);

	printf("Enter sequence of panels: ");

	for (i=0; i<length; i++)
		scanf("%d", &sequence[i]);

	return length;
}

// Updates grid with each press in sequence
void press(int grid[][GRID_SIZE], int seq_len, int seq[]){
    int i = 0;

    // presses each button in the sequence
    for (i; i < seq_len; i++){
        press_1(grid, seq[i]);
    }
}

// Checks whether button is valid - inside the grid
int in_grid(int button){
    return button >=0 && button < GRID_SIZE * GRID_SIZE;
}

// Updates grid from a single press
void press_1(int grid[][GRID_SIZE], int button){
    // if out of grid, do nothing
    if (!in_grid(button)) return;

    // initialize an array to keep track of buttons to be flipped
    // button pressed will also be flipped
    int buttons_to_flip[5] = {button};
    int i = 0;

    // inserts buttons to be flipped into an array
    to_flip(button, buttons_to_flip);

    // flips all the buttons to be flipped using the buttons_to_flip array
    for (i; i < 5; i++){
        flip(grid, buttons_to_flip[i]);
    }
}

// Inserts button no. to be flipped into input array
void to_flip(int button, int arr[]){
    arr[1] = button - GRID_SIZE; //above
    arr[2] = button + GRID_SIZE; // below
    arr[3] = button - 1; //left
    arr[4] = button + 1; //right
}

// Flips a single button and updates grid
void flip(int grid[][GRID_SIZE], int button){
    // if out of grid, do nothing
    if (!in_grid(button)) return;

    int row = button / GRID_SIZE;
    int col = button % GRID_SIZE;
    // flip the grid element by equating it to its opposite
    grid[row][col] = !(grid[row][col]);
}

// Checks if all buttons are off and returns 1 if yes 0 if no. Also updates an input number of panels tracker.
int allOff(int grid[][GRID_SIZE], int *n_panels){
    int i, j;
    // takes the input no. of panel to track how many are on and set it to 0
    *n_panels = 0;

    // counts how many panels are on
    for (i = 0; i < GRID_SIZE; i++){
        for (j = 0; j < GRID_SIZE; j++){
            if (grid[i][j])
                (*n_panels)++;
        }
    }

    return *n_panels == 0;
}
