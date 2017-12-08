#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "elina_interval.h"

elina_interval_t * interval1=NULL, *interval2=NULL;

void test_set_int(){
	long int inf = rand()%100;
	long int sup = rand()%100;
	elina_interval_set_int(interval1,inf,sup);
	printf("set int inf: %ld sup: %ld interval: ",inf,sup);
	elina_interval_print(interval1);
	printf(" is bottom: %d is top: %d\n", elina_interval_is_bottom(interval1),elina_interval_is_top(interval1));
}


void test_set_mpq(){
	mpq_t inf1,sup1;
	mpq_init(inf1);
	mpq_init(sup1);
	long int p = rand()%1000;
	unsigned long int q= rand()%20;
	mpq_set_si(inf1,p,q);
	p = p + rand()%1000;
	mpq_set_si(sup1,p,q);
	elina_interval_set_mpq(interval1,inf1,sup1);
	printf("set mpq inf: ");
	mpq_out_str(stdout,10,inf1);
	printf(" sup: ");
	mpq_out_str(stdout,10,sup1);
	printf(" interval: ");
	elina_interval_print(interval1);
	printf(" is bottom: %d is top: %d\n", elina_interval_is_bottom(interval1),elina_interval_is_top(interval1));
	mpq_clear(inf1);
	mpq_clear(sup1);
}

void test_set_frac(){
	long int p1 = rand()%100;
	unsigned long int q1 = rand()%20;
	long int p2 = rand()%100;
	unsigned long int q2 = rand()%20;
	elina_interval_set_frac(interval1,p1,q1,p2,q2);
	printf("set frac p1: %ld q1: %ld p2: %ld q2: %ld interval: ",p1,q1,p2,q2);
	elina_interval_print(interval1);
	printf(" is bottom: %d is top: %d\n", elina_interval_is_bottom(interval1),elina_interval_is_top(interval1));
}


void test_set_double(){
	double inf = (double)rand()/RAND_MAX*2.0-1.0;
	double sup = (double)rand()/RAND_MAX*2.0-1.0;
	elina_interval_set_double(interval1,inf,sup);
	printf("set double inf: %g sup: %g interval: ",inf,sup);
	elina_interval_print(interval1);
	printf(" is bottom: %d is top: %d\n", elina_interval_is_bottom(interval1),elina_interval_is_top(interval1));
}


void test_set_mpfr(){
	mpfr_t inf,sup;
	mpfr_init(inf);
	mpfr_init(sup);
	double d = (double)rand()/RAND_MAX*2.0-1.0;
	mpfr_set_d(inf,d,GMP_RNDU);
	
	d = (double)rand()/RAND_MAX*2.0-1.0;
	mpfr_set_d(sup,d,GMP_RNDU);

	elina_interval_set_mpfr(interval1,inf,sup);
	printf("set mpfr: ");
	mpfr_out_str(stdout,10,elina_scalar_print_prec,inf,GMP_RNDU);
	printf(" ");
	mpfr_out_str(stdout,10,elina_scalar_print_prec,sup,GMP_RNDU);
	printf(" interval: ");
	elina_interval_print(interval1);
	printf(" is bottom: %d is top: %d\n", elina_interval_is_bottom(interval1),elina_interval_is_top(interval1));
	mpfr_clear(inf);
	mpfr_clear(sup);
}	



void test_cmp(){
	long int inf2 = rand()%100;
	long int sup2 = inf2+ rand()%100; 
	elina_interval_set_int(interval2,inf2,sup2);
	printf("cmp interval: ");
	elina_interval_print(interval1);
	printf(" ");
	elina_interval_print(interval2);
	printf("interval1<=interval2: %d interval1==interval2: %d \n",elina_interval_cmp(interval1,interval2), elina_interval_equal(interval1,interval2));
}


void test_set_interval(){
	elina_interval_set(interval2,interval1);
	printf("set interval1: ");
	elina_interval_print(interval1);
	printf(" interval2: ");
	elina_interval_print(interval2);
	printf(" interval1==interval2: %d\n",elina_interval_equal(interval1,interval2));
}



void test_equality(){
	elina_interval_set_bottom(interval1);
	printf("equality interval1: ");
	elina_interval_print(interval1);
	elina_interval_set_top(interval2);
	printf(" interval2: ");
	elina_interval_print(interval2);
	printf(" interval1==interval2: %d\n", elina_interval_equal(interval1,interval2));
}



void test_swap(){
	elina_interval_swap(interval1,interval2);
	printf("swap interval1: ");
	elina_interval_print(interval1);
	printf("interval2: ");
	elina_interval_print(interval2);
	printf("interval1 is bottom: %d is top: %d\n", elina_interval_is_bottom(interval1),elina_interval_is_top(interval1));
	printf("interval2 is bottom: %d is top: %d\n", elina_interval_is_bottom(interval2),elina_interval_is_top(interval2));
}

void test_neg(){
	elina_interval_neg(interval1,interval2);
	printf("neg interval1: ");
	elina_interval_print(interval1);
	printf("interval2: ");
	elina_interval_print(interval2);
	printf("interval1 is bottom: %d is top: %d\n", elina_interval_is_bottom(interval1),elina_interval_is_top(interval1));
	printf("interval2 is bottom: %d is top: %d\n", elina_interval_is_bottom(interval2),elina_interval_is_top(interval2));
}

int main(){
	time(NULL);

	interval1 = elina_interval_alloc();

	interval2 = elina_interval_alloc();

	// interval is set to int
	test_set_int();
	
	

	//interval is set to mpq
	test_set_mpq();
	
	
	
	//interval is set to fractions
	test_set_frac();
	
	//interval is set to double
	test_set_double();
	

	//interval is set to mpfr
	test_set_mpfr();	
	

	//set to interval
	test_set_interval();	
	
	//test for comparison and equality 
	test_cmp();
	test_equality();
	
	
	//test for swapping and negation
	test_swap();
	test_neg();
	

	elina_interval_free(interval2);
	elina_interval_free(interval1);
}