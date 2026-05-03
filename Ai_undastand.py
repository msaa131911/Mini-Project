import cv2
import numpy as np

class CVApp:

    def camera(self):
        self.camera = cv2.VideoCapture(0)

        while True:
            ret, frame = self.camera.read()

            if not ret:
                print("camera not open")
                break

            cv2.imshow("camera", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.camera.release()
        cv2.destroyAllWindows()


    def img_red(self):
        path = input("path: ")

        if path == "":
            print("image path empty")
            return

        img = cv2.imread(path)

        if img is None:
            print("image load hoy nai")
        else:
            print(img)


    def rew_colm(self):
        path1 = input("path1: ")
        path2 = input("path2: ")

        cap1 = cv2.VideoCapture(path1)
        cap2 = cv2.VideoCapture(path2)
        cap3 = cv2.VideoCapture(0)

        while True:
            ret1, f1 = cap1.read()
            ret2, f2 = cap2.read()
            ret3, f3 = cap3.read()

            if not (ret1 and ret2 and ret3):
                print("video end or error")
                break

            f1 = cv2.resize(f1, (400, 400))
            f2 = cv2.resize(f2, (400, 400))
            f3 = cv2.resize(f3, (400, 400))

            h_img = np.hstack((f1, f2, f3))
            v_img = np.vstack((h_img, h_img, h_img))

            cv2.imshow("Multi Video Grid", v_img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap1.release()
        cap2.release()
        cap3.release()
        cv2.destroyAllWindows()


class sk_model(CVApp):
    import pandas as pd

    def input_data(self):
        path = input("CSV file path: ")

        try:
            df = pd.read_csv(path)
        except:
            print(" File load hoy nai")
            return

        print(" Data loaded successfully")
        print("Columns:", list(df.columns))

        while True:
            cmd = input("\nCommand dao (type 'exit' to stop): ")

            if cmd == "exit":
                break

            elif cmd == "show":
                print(df.head())

            elif cmd == "shape":
                print("Shape:", df.shape)

            elif cmd == "columns":
                print(df.columns)

            elif cmd == "describe":
                print(df.describe())

            elif cmd.startswith("mean"):
                col = cmd.split(" ")[1]
                print("Mean:", df[col].mean())

            elif cmd.startswith("value_counts"):
                col = cmd.split(" ")[1]
                print(df[col].value_counts())

            else:
                print(" Unknown command")

    
    
    


        