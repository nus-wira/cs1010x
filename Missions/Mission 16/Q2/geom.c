/*****************************************
 * CS1010X --- Programming Methodology  *
 *                                       *
 *   Mission 16, Question 2 Template     *
 *****************************************/

#include <stdio.h>
#define PI 3.14159265358979323846

typedef struct {
    int x;
    int y;
} Point;

typedef struct {
    Point corner;        // coordinates of top-left corner
    unsigned int width;  // units to right edge from corner
    unsigned int height; // units to bottom edge from corner
} Rectangle;

void print_rect(Rectangle rect) {
    printf("x = %d, y = %d, w = %u, l = %u\n",
           rect.corner.x, rect.corner.y, rect.width, rect.height);
}

void print_circle_in(Rectangle rect, const char *name);


Rectangle bounds(Rectangle rect[], int total) {
    /************
     *  Task 1  *
     ************

     Compute and return the smallest rectangle enclosing all the rectangles
     in the array up to "total", i.e. from rect[0] to rect[total - 1].

     If the total is zero, return a rectangle with zero width and height
     positioned at the origin.

     Note that the positive x-axis extends to the right of the origin, while
     the positive y-axis extends downwards from the origin.

    */
    Point pt = {0,0};
    Rectangle result = {pt, 0, 0};
    if (total == 0) return result;

    int i = 1;
    int xf, yf; //furthest x and y coordinates
    pt.x = rect[0].corner.x;
    pt.y = rect[0].corner.y;
    result.width = rect[0].width;
    result.height = rect[0].height;

    for(i; i < total; i++){
        Point curr_pt = rect[i].corner;
        int curr_x = curr_pt.x, curr_y = curr_pt.y;
        //unsigned int needs to be converted to int to handle comparison of negative values
        int res_w = result.width, res_h = result.height;
        int curr_w = rect[i].width, curr_h = rect[i].height;

        //checking for furthest x and y coordinate
        if (curr_x + curr_w > pt.x + res_w)
            xf =  curr_x + curr_w;
        else
            xf = pt.x + res_w;

        if (curr_y + curr_h > pt.y + res_h)
            yf =  curr_y + curr_h;
        else
            yf = pt.y + res_h;

        //checking for corner being left-most and top-most
        if (curr_x < pt.x)
            pt.x = curr_x;
        if (curr_pt.y < pt.y)
            pt.y = curr_y;

        //setting appropriate width and height
        result.width = xf - pt.x;
        result.height = yf - pt.y;

    }
    result.corner = pt;

    return result;
}

/************
 *  Task 2  *
 ************

 Write the function make_circle to compute the largest circle that can fit in
 the given box. If the circle is only touching two sides of the box, it should
 be centered between the other two sides.

 This function should return a structure that contains multiple values pertaining
 to the computed circle. You will need to decide on how to define and populate
 the structure from the way the "print_circle_in" function uses it.

*/

// Define the required structure here.
typedef struct {
    float area;
    float perimeter;
} Stat;

typedef struct {
    float x;
    float y;
    float radius;
    Stat stats;
} Circle;

Circle make_circle(Rectangle box){
    float radius, x, y, area, peri, w =box.width, h=box.height;
    Point pt = box.corner;
    if (w < h)
        radius = w/2;
    else
        radius = h/2;

    x = pt.x + (w/2);
    y = pt.y + (h/2);

    area = PI*radius*radius;
    peri = 2*PI*radius;

    Stat stats = {area, peri};
    Circle circ = {x, y, radius, stats};
    return circ;
}


int main(void) {
    Rectangle rect[] = {
        { {-1, 2}, 30, 60 },
        { {10, 1}, 20, 1 },
        { {0, -10}, 3, 2 },
        { {0, 0}, 55, 77 },
    };

    // Task 1 output
    print_rect(bounds(rect, 0));
    print_rect(bounds(rect, 1));
    print_rect(bounds(rect, 2));
    print_rect(bounds(rect, 3));
    print_rect(bounds(rect, 4));
    printf("\n");

    Rectangle a = { {3, 4}, 32, 32 };
    Rectangle b = { {-9, -10}, 65, 37 };
    Rectangle c = { {-12, -80}, 87, 99 };

    // Task 2 output
    print_circle_in(a, "a");
    print_circle_in(b, "b");
    print_circle_in(c, "c");

    return 0;
}

void print_circle_in(Rectangle box, const char *name) {
    // Uncomment the following lines to test your make_circle function
    // for Task 2. DO NOT MODIFY THEM.

    Circle circ = make_circle(box);
    printf("%s.center: %f %f\n", name, circ.x, circ.y);
    printf("%s.radius: %f\n", name, circ.radius);
    printf("%s.area: %f\n", name, circ.stats.area);
    printf("%s.perimeter: %f\n\n", name, circ.stats.perimeter);
}

/*
 EXPECTED OUTPUT:

    x = 0, y = 0, w = 0, l = 0
    x = -1, y = 2, w = 30, l = 60
    x = -1, y = 1, w = 31, l = 61
    x = -1, y = -10, w = 31, l = 72
    x = -1, y = -10, w = 56, l = 87

    a.center: 19.000000 20.000000
    a.radius: 16.000000
    a.area: 804.247742
    a.perimeter: 100.530968

    b.center: 23.500000 8.500000
    b.radius: 18.500000
    b.area: 1075.210083
    b.perimeter: 116.238930

    c.center: 31.500000 -30.500000
    c.radius: 43.500000
    c.area: 5944.678711
    c.perimeter: 273.318573
*/
