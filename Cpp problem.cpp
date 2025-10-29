#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;

    if (num % 2 == 0)
        cout << num << " is Even\n";
    else
        cout << num << " is Odd\n";

    return 0;
}


#👨‍🏫Student Grade Calculator

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter number of subjects: ";
    cin >> n;

    float marks[n], sum = 0;
    for (int i = 0; i < n; i++) {
        cout << "Enter marks of subject " << i + 1 << ": ";
        cin >> marks[i];
        sum += marks[i];
    }

    float avg = sum / n;
    cout << "\nAverage Marks = " << avg << endl;

    if (avg >= 90)
        cout << "Grade: A+" << endl;
    else if (avg >= 80)
        cout << "Grade: A" << endl;
    else if (avg >= 70)
        cout << "Grade: B" << endl;
    else if (avg >= 60)
        cout << "Grade: C" << endl;
    else if (avg >= 50)
        cout << "Grade: D" << endl;
    else
        cout << "Grade: F" << endl;

    return 0;
}


//practics program
#include <iostream>
using namespace std;

int main() {
    int ans = (5/(double)5);
    cout << ans << endl;
    return 0;
}
