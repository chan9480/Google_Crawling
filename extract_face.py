from os import listdir
from PIL import Image
from numpy import asarray
from mtcnn.mtcnn import MTCNN

def extract_face(filename, required_size=(512, 512)) : 
  try :
    images = []
    image = Image.open(filename)
    image = image.convert('RGB')
    pixels = asarray(image)
    detector = MTCNN()
    results = detector.detect_faces(pixels)
    for result in results :      
      if result['confidence'] < 0.99 : continue
      x1, y1, width, height = result['box']
      x1, y1 = abs(x1), abs(y1)      
      x2, y2 = x1 + width, y1 + height
      pad_width = width // 2      
      pad_heigth = height // 2
      face = pixels[max(y1-pad_heigth, 0):min(y2+pad_heigth, pixels.shape[0]),max(x1-pad_width, 0):min(x2+pad_width, pixels.shape[1])]
      image = Image.fromarray(face)
      image = image.resize(required_size)      
      images.append(image)  
    return images
  except :
    return images

if __name__ == '__main__':
    target_files = listdir('.\idols\\')
    print(target_files[1])
    i=0
    for file in target_files:
        extracted_faces = extract_face('.\idols\\' + file)
        for extracted_face in extracted_faces:
            save_path = '.\extracted\\' + str(i)+'.jpg'
            extracted_face.save(save_path)
            i+=1