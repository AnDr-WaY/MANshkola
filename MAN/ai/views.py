from ultralytics import YOLO
from django.shortcuts import render
from .forms import UploadImageForm
import os

model = YOLO('ai/best.pt')  




# Create your views here.
def main(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()  # Сохраняем изображение
            image_path = uploaded_image.image.path  # Путь к сохранённому файлу

            # Запускаем проверку через нейросеть YOLO
            results = model.predict(source=image_path)  # Используем YOLO
            probs = results[0].probs  
            predicted_class = probs.top1  
            confidence = int(probs.top1conf.item()*100)
            print(predicted_class)
            is_mine = predicted_class == 0
            
            os.remove(image_path)

            return render(request, 'ai/result.html', {'is_mine': is_mine, 'confidence': confidence})
    else:
        form = UploadImageForm()

    return render(request, 'ai/ai.html', {'form': form})
