#include<stdio.h>
#include<stdbool.h>
bool max(int a,int b)
{
	if(a<b)
	{
		return true;
	}
	else
	{
		return false;
	}
}
int main()
{
	int a=11 ,b=21;
	bool bret;
	
	bret=max(a,b);
	if(bret == true)
	{
		printf("b motha ahe ");
	}
	else
	{
		printf("a motha ahe");
	}
	
	return 0;
}