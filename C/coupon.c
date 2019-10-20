#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    int quantity; // Number of items purchasable with this coupon
    int price;    // Total price to be paid for using this coupon
} coupon_t;

int minimumCost(coupon_t [], int, int);
void withoutFirst(coupon_t [], coupon_t [], int);

int main(void){
   coupon_t coupons[] = {{3,10},{2,4},{2,4},{1,3}};
   int units = 5;

   printf("%d\n", minimumCost(coupons, 4, 8));
   return 0;

}

int minimumCost(coupon_t coupons[], int numCoupons, int units){
    if (units == 0)
        return 0;
    else if (numCoupons == 0 || units < 0)
        return -1;

    int qty = coupons[0].quantity, price = coupons[0].price, cost1, cost2;
    coupon_t restOfCoupons[numCoupons];

    withoutFirst(coupons, restOfCoupons, numCoupons);


    //using first coupon
    cost1 = minimumCost(restOfCoupons, numCoupons - 1, units - qty);
    //not using first coupon
    cost2 = minimumCost(restOfCoupons, numCoupons - 1, units);


    //if both invalid return invalid
    if (cost1 < 0 && cost2 < 0)
        return -1;
    // if one invalid return the other
    else if (cost1 < 0)
        return cost2;
    else if (cost2 < 0)
        return price + cost1;
    // return the lesser of the two costs
    else if (cost1 + price <= cost2)
        return price + cost1;
    else
        return cost2;

}

//function for coupons without first coupon
void withoutFirst(coupon_t coupons[], coupon_t restOfCoupons[], int numCoupons){
    int i;

    for (i = 0; i < numCoupons -1; i++){
        restOfCoupons[i] = coupons[i+1];
    }
}
