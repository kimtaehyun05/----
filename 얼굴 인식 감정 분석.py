import cv2
from fer import FER
import random
import webbrowser
# 감정에 따라 추천할 노래 리스트
emotion_songs = {
    "happy": [
        "https://www.youtube.com/watch?v=ZbZSe6N_BXs",  # Happy - Pharrell Williams
        "https://www.youtube.com/watch?v=JGwWNGJdvx8"   # Shape of You - Ed Sheeran
    ],
    "sad": [
        "https://www.youtube.com/watch?v=RgKAFK5djSk",  # See You Again
        "https://www.youtube.com/watch?v=YQHsXMglC9A"   # Hello - Adele
    ],
    "angry": [
        "https://www.youtube.com/watch?v=04F4xlWSFh0",  # Numb - Linkin Park
        "https://www.youtube.com/watch?v=tAGnKpE4NCI"   # In The End - Linkin Park
    ],
    "surprise": [
        "https://www.youtube.com/watch?v=9bZkp7q19f0",  # Gangnam Style
    ],
    "neutral": [
        "https://www.youtube.com/watch?v=2Vv-BfVoq4g",  # Perfect - Ed Sheeran
    ],
    "fear": [
        "https://www.youtube.com/watch?v=2vjPBrBU-TM",  # Chandelier - Sia
    ],
    "disgust": [
        "https://www.youtube.com/watch?v=hLQl3WQQoQ0",  # Someone Like You - Adele
    ]
}

# 얼굴 및 감정 분석기 초기화
detector = FER(mtcnn=True)
cap = cv2.VideoCapture(0)
print("카메라를 실행합니다. 'q'를 눌러 종료합니다.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = detector.detect_emotions(frame)

    # 감정이 감지되었을 때만 처리
    if result:
        dominant_emotion, score = detector.top_emotion(frame)
        print(f"감지된 감정: {dominant_emotion} (신뢰도: {score:.2f})")
        
        if dominant_emotion in emotion_songs:
            song = random.choice(emotion_songs[dominant_emotion])
            print(f"추천 노래: {song}")
            webbrowser.open(song)
        else:
            print("해당 감정에 대한 추천 노래가 없습니다.")
        break

    # 화면에 얼굴 표시
    cv2.imshow("Emotion Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료
cap.release()
cv2.destroyAllWindows()