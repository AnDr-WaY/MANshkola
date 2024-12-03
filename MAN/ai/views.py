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
            uploaded_image = form.save()  
            image_path = uploaded_image.image.path  
            
            results = model.predict(source=image_path)  
            probs = results[0].probs  
            predicted_class = probs.top1  
            confidence = int(probs.top1conf.item()*100)
            is_mine = predicted_class == 0
            
            os.remove(image_path)

            return render(request, 'ai/result.html', {'is_mine': is_mine, 'confidence': confidence})
    else:
        form = UploadImageForm()

    return render(request, 'ai/ai.html', {'form': form})
