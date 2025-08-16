import cv2

# Paths
ageProto = r"C:\My project\face_recognition\deploy_age.prototxt"
ageModel = r"C:\My project\face_recognition\age_net.caffemodel"
genderProto = r"C:\My project\face_recognition\gender_deploy.prototxt"
genderModel = r"C:\My project\face_recognition\gender_net.caffemodel"
# Ensure the paths are correct

# Load models
age_net = cv2.dnn.readNetFromCaffe(ageProto, ageModel)
gender_net = cv2.dnn.readNetFromCaffe(genderProto, genderModel)

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Labels
gender_list = ["Male", "Female"]
age_list = ["(0-2)", "(4-6)", "(8-12)", "(15-20)", "(21-30)", "(31-40)", "(41-50)", "(51-60)", "(61-100)"]

# Start webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w].copy()
        blob = cv2.dnn.blobFromImage(face_img, 1.0, (227, 227),
                                     (78.426, 87.769, 114.896), swapRB=False)

        # Gender Prediction
        gender_net.setInput(blob)
        gender_preds = gender_net.forward()
        gender = gender_list[gender_preds[0].argmax()]

        # Age Prediction
        age_net.setInput(blob)
        age_preds = age_net.forward()
        age = age_list[age_preds[0].argmax()]

        # Show result
        label = f"{gender}, {age}"
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, label, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

    # Show output window
    cv2.imshow("Age & Gender Detection", frame)

    # Exit when pressing "q" OR closing window
    if (cv2.waitKey(1) & 0xFF == ord("q")) or \
       (cv2.getWindowProperty("Age & Gender Detection", cv2.WND_PROP_VISIBLE) < 1):
        break

video_capture.release()
cv2.destroyAllWindows()  