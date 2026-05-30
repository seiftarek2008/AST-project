from utils.model_loader import load_model

model = load_model()

def predict_sign(frame):

    results = model(frame)

    best_label = None
    best_conf = 0

    for result in results:

        for box in result.boxes:

            conf = float(box.conf[0])

            class_id = int(box.cls[0])

            if conf > best_conf:

                best_conf = conf

                best_label = model.names[class_id]

    return best_label, best_conf