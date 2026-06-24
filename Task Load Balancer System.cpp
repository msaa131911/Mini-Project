#include<iostream>
#include<vector>
using namespace std;

bool isPossible(vector<int>& tasks,int n,int workers,int maxload){
    int workercount=1,currentload=0;
    for(int i=0;i<n;i++){
        if(tasks[i]>maxload){
            return false;
        }
        if(currentload+tasks[i]<=maxload){
            currentload+=tasks[i];
        }
        else{
            workercount++;
            currentload=tasks[i];
            if(workercount>workers){
                return false;
            }
        }
    }
    return true;
}

int taskBalancer(vector<int>& tasks,int n,int workers){
    int st=0,end=0,ans=-1;
    for(int x:tasks){
        st=max(st,x);
        end+=x;
    }
    while(st<=end){
        int mid=st+(end-st)/2;
        if(isPossible(tasks,n,workers,mid)){
            ans=mid;
            end=mid-1;
        }
        else{
            st=mid+1;
        }
    }
    return ans;
}

void printDistribution(vector<int>& tasks, int workers, int maxLoad)
{
    int currentLoad = 0;
    int worker = 1;

    cout << "\nTask Distribution:\n";
    cout << "Worker " << worker << " -> ";

    for(int task : tasks)
    {
        if(currentLoad + task <= maxLoad)
        {
            cout << task << " ";
            currentLoad += task;
        }
        else
        {
            worker++;
            cout << "\nWorker " << worker << " -> ";
            cout << task << " ";
            currentLoad = task;
        }
    }

    cout << endl;
}

int main()
{
    int n, workers;

    cout << "Enter number of tasks: ";
    cin >> n;

    vector<int> tasks(n);

    cout << "Enter task times:\n";
    for(int i = 0; i < n; i++)
    {
        cin >> tasks[i];
    }

    cout << "Enter number of workers: ";
    cin >> workers;

    int answer = taskBalancer(tasks, n, workers);

    cout << "\nMinimum Completion Time = " << answer << endl;

    printDistribution(tasks, workers, answer);

    return 0;
}