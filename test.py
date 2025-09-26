import cv2
from ultralytics import YOLO

def run_yolo_detection():
    """
    Main function to run YOLO object detection on a video file.
    """
    # ---- EDIT THESE VALUES ----
    model_path = "Model/Arc_New_Grayscale_dataset_best_model.pt"
    video_path = "Test_Vid/test_arcsuit.mp4"
    threshold = 0.5  # Confidence threshold

    CONVERT_TO_GRAYSCALE = True

    try:
        model = YOLO(model_path)
        print("YOLO model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file at '{video_path}'")
        return

    print(f"Processing video... Press 'q' to exit.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("End of video or failed to read frame.")
            break
        

        if CONVERT_TO_GRAYSCALE:
            model_input_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if len(model_input_image.shape) == 2:
                model_input_image = cv2.cvtColor(model_input_image, cv2.COLOR_GRAY2BGR)
        else:
            model_input_image = frame

        results = model(model_input_image, conf=threshold)

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                conf = box.conf[0].item()
                cls_id = int(box.cls[0].item())
                class_name = model.names[cls_id]

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                text = f"{class_name}: {conf:.2f}"
                cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


        cv2.imshow('YOLO Object Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()
    print("Processing finished.")


if __name__ == '__main__':
    run_yolo_detection()