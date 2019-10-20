#include <stdio.h>
#include <math.h>
#define MAX_STATION 5
#define MAX_TICKETS 100

float sample_count(int, int, int, int);
void message(float, float);

int main(void) {
	float sampleCountA=0.0, sampleCountB=0.0;
	int numVoterDivision, numStation, numVoterStation, numVoteA, numVoteB;
	int i;

	// Use the following printf statements to print the appropriate messages.
	printf("Enter number of voters in the division: ");
	scanf("%d", &numVoterDivision);

	printf("Enter number of stations: ");
	scanf("%d", &numStation);

	for(i = 1; i < numStation+1; i++) {
		printf("Enter number of voters in station %d: ", i);
		scanf("%d", &numVoterStation);
		printf("Enter number of votes for Team A: ");
		scanf("%d", &numVoteA);
		printf("Enter number of votes for Team B: ");
		scanf("%d", &numVoteB);
		sampleCountA += sample_count(numVoteA, numVoteB, numVoterStation, numVoterDivision);
	}

	sampleCountA *= 100;
	sampleCountB = 100-sampleCountA;


	printf("Sample count for Team A = %.2f%%\n",sampleCountA);
	printf("Sample count for Team B = %.2f%%\n",sampleCountB);

	message(sampleCountA, sampleCountB);

    return 0;
}

float sample_count(int numVoteA, int numVoteB, int numVoterStation, int numVoterDivision) {
	int numInvalidVote;
	float sampleCount=0.0;

	numInvalidVote = 100 - numVoteA - numVoteB;

	sampleCount += (((float)numVoteA/(100-(float)numInvalidVote))*((float)numVoterStation/(float)numVoterDivision));

	return sampleCount;
}

void message(float sampleCountA, float sampleCountB) {
    float diff = sampleCountA - sampleCountB;

    if (diff > 0)
        printf("Team A ");
    else if (diff < 0)
        printf("Team B ");
    else {
        printf("There is no winner in this election.");
        return;
    }

    diff = fabs(diff);

    if (diff < 5)
        printf("narrowly wins the election.");
    else if (diff <= 30)
        printf("wins by a significant margin.");
    else
        printf("wins by a landslide.");

    /*
	if((sampleCountA - sampleCountB) == 0) {
		printf("There is no winner in this election.");
	} else if((sampleCountA - sampleCountB) < 5) {
		printf("Team A narrowly wins the election.");
	} else if((sampleCountB - sampleCountA) < 5) {
		printf("Team B narrowly wins the election.");
	} else if((sampleCountA - sampleCountB) > 6 && (sampleCountA - sampleCountB) < 31) {
		printf("Team A wins by a significant margin");
	} else if((sampleCountB - sampleCountA) > 6 && (sampleCountB - sampleCountA) < 31) {
		printf("Team B wins by a significant margin.");
	} else if((sampleCountA - sampleCountB) > 30) {
		printf("Team A wins by a landslide.");
	} else if(sampleCountB - sampleCountA > 30) {
		printf("Team B wins by a landslide.");
	}
	*/
}
