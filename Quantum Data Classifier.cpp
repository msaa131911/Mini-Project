#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <iomanip>

using namespace std;

struct datapoint {
    double x, y;
    int label;
};

// Quantum Data Classifier
class QuantumDataClassifier {

private:

    // Quantum state
    // |psi> = alpha|0> + beta|1>
    double alpha, beta;

public:

    QuantumDataClassifier() {
        alpha = 1.0;
        beta = 0.0;
    }

    // Classical data -> Quantum state
    void encode(double x, double y) {

        double theta = (x + y) * M_PI / 2.0;

        alpha = cos(theta / 2.0);
        beta = sin(theta / 2.0);
    }

    // Measurement probability of |0>
    double probabilityZero() {
        return alpha * alpha;
    }

    // Measurement probability of |1>
    double probabilityOne() {
        return beta * beta;
    }

    // Classification
    int predict() {

        if (probabilityOne() >= 0.5)
            return 1;
        else
            return 0;
    }

    // Show quantum state
    void showstate() {

        cout << fixed << setprecision(4);

        cout << "Quantum State: "
             << alpha << "|0> + "
             << beta << "|1>" << endl;

        cout << "P(0) = "
             << probabilityZero() << endl;

        cout << "P(1) = "
             << probabilityOne() << endl;
    }
};


int main() {

    QuantumDataClassifier qdc;

    vector<datapoint> dataset = {

        {0.1, 0.2, 0},
        {0.2, 0.3, 0},
        {0.3, 0.2, 0},
        {0.4, 0.3, 0},

        {0.7, 0.8, 1},
        {0.8, 0.7, 1},
        {0.9, 0.8, 1},
        {0.8, 0.9, 1}
    };

    int correct = 0;

    cout << "-------------------------------" << endl;
    cout << "   Quantum Data Classifier" << endl;
    cout << "-------------------------------" << endl;


    for (int i = 0; i < dataset.size(); i++) {

        double x = dataset[i].x;
        double y = dataset[i].y;

        int true_label = dataset[i].label;

        
        qdc.encode(x, y);

        
        int predicted = qdc.predict();


        cout << "\nData Point " << i + 1 << endl;

        cout << "x = " << x
             << ", y = " << y << endl;

        cout << "Actual Class    = "
             << true_label << endl;

        cout << "Predicted Class = "
             << predicted << endl;


        
        qdc.showstate();


        // Check prediction
        if (true_label == predicted) {

            cout << "Result: Correct" << endl;

            correct++;
        }
        else {

            cout << "Result: Wrong" << endl;
        }

        
    }


    // Accuracy
    double accuracy =(double)correct / dataset.size() * 100;


    

    cout << "Correct Predictions: "
         << correct << "/"
         << dataset.size() << endl;

    cout << "Accuracy: "
         << accuracy << "%" << endl;

    


    return 0;
}