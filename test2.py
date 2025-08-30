import os
import shutil
from deepface import DeepFace  # مكتبة تحدد الجنس عبر الذكاء الاصطناعي

def filter_and_copy_male_images(ffhq_path, output_dir="male_images", num=2500):
    """
    تصفية صور الرجال من FFHQ Dataset وحفظها في مجلد جديد.
    
    :param ffhq_path: المسار إلى مجلد FFHQ.
    :param output_dir: مجلد الحفظ (سيتم إنشاؤه تلقائيًا).
    :param num: عدد الصور المطلوبة.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    all_images = [f for f in os.listdir(ffhq_path) if f.endswith(('.png', '.jpg'))]
    
    male_count = 0
    for img_file in all_images:
        if male_count >= num:
            break 
            
        img_path = os.path.join(ffhq_path, img_file)
        
        try:
            analysis = DeepFace.analyze(img_path, actions=['gender'])
            gender = analysis[0]['dominant_gender']
            
            if gender == 'Man':
                shutil.copy(img_path, os.path.join(output_dir, img_file))
                male_count += 1
                print(f"Copied {male_count}/{num} male images: {img_file}")
                
        except Exception as e:
            print(f"Error processing {img_file}: {e}")

filter_and_copy_male_images(
    ffhq_path=r"C:\path\to\ffhq-256x256", #FFHQ Dataset
    output_dir="male_profile_pics",
    num=2500
)