#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

int isCorrect(int cats[], int cat, int n);
void printArray(const char *message, int arr[], int n);

int main()
{	
	int n;
	
	cout << "input n:" ;
	cin >> n;
	
	set<int> setCats;
	int cats[n], newCats[n], status[n], flag = 0;
	
	for (int i = 0; i < n; i++)
	{	
		cin >> cats[i];
		setCats.insert(cats[i]);
		status[i] = newCats[i] = 0;
	}
	printArray("cat", cats, n);
	cout << endl;
	
	int result = isCorrect(cats, 1, n);
	if (result)
	{
		cout << "box size : " << 0 << endl;
		return 0;
	}
	for (set<int>::iterator c = setCats.begin(); c != setCats.end(); c++)
	{
		int count = 0, cat = *c;
		for (int j = 0; j < n; j++)
			status[j] = newCats[j] = 0;
		for (int j = 0; j < n - 1; j++)
		{
			if (cats[j] <= cat && status[j] == 0)
			{
				status[j] = 1;
				newCats[count++] = cats[j];
				for (int k = j + 1; k < n; k++)
				{
					if (cats[j] == cats[k])
					{
						status[k] = 1;
						newCats[count++] = cats[k];	
					}
				}
			}
		}
		for (int j = 0; j < n; j++)
			if (status[j] == 0)
				newCats[count++] = cats[j];
		
		cout << "size : " << cat << " ";
		printArray("status", status, n);
		printArray("newCats", newCats, n);
		cout << endl;
		
		if(flag == 0 && (result = isCorrect(newCats, cat, n)))
			flag = 1;
	}
	cout << "box size : " << result << endl;
	return (0);
}

int isCorrect(int cats[], int cat, int n)
{
	for (int i = 0; i < n; i+=2)
		if (cats[i] != cats[i + 1])
			return 0;
	return cat;
}

void printArray(const char *message, int arr[], int n)
{
	cout << message << " : ";
	for (int i = 0; i < n; i++)
		cout << arr[i] << " ";
}
