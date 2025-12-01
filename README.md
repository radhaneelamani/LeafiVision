# LeafiVision
Deep Learning Based Pest and Disease Detection in Crops
# LeafiVision – Automated Groundnut Pest & Disease Detection Using Custom CNN

LeafiVision is a deep-learning–based image classification system designed to automatically detect major pests and diseases affecting groundnut (peanut) crops. Using a custom Convolutional Neural Network (CNN), the project achieves **97% accuracy** across **8 classes**, offering a lightweight model suitable for real-time or smartphone-based crop diagnosis.

---

## 📑 Table of Contents
- [Introduction](#introduction)  
- [Features](#features)  
- [Dataset](#dataset)  
- [Methodology](#methodology)  
- [Model Architectures](#model-architectures)  
- [Results](#results)   
- [Future Scope](#future-scope)  

---

## 🌱 Introduction
Groundnut (Arachis hypogea) is a globally important oilseed crop grown across 120+ countries. Biotic stresses—particularly leaf diseases and damaging insect pests—can drastically reduce yield and quality. Early diagnosis is essential but difficult for non-experts.

This project provides a **computer-vision–based automated diagnosis system** using a **Custom CNN** trained on field-collected images from ICRISAT. The model distinguishes between multiple diseases, pests, healthy leaves, and even detects when an image is *not* groundnut.

---

## ⭐ Features
- Custom-designed **3-layer** and **6-layer** CNN architectures  
- Achieves **up to 97% accuracy**  
- **8-class classification**:
  - Alternaria Leaf Spot  
  - Late & Early Leaf Spot  
  - Rust  
  - Leaf Hopper & Jassids  
  - Leaf Miner  
  - Tobacco Caterpillar  
  - Healthy  
  - Not Groundnut
- Includes **data augmentation** (random rotation, flipping)  
- Lightweight architecture suitable for **mobile deployment**  
- Trained using **TensorFlow + Keras** on Google Colab  

---

## 🗂 Dataset
- Total images: **4867**
- Collected from **ICRISAT fields** using mobile devices.  
- Additional “Not Groundnut” images sourced from Kaggle datasets.  
- **Split:**  
  - 80% Training  
  - 10% Validation  
  - 10% Testing  

| Class | Description | Images |
|------|-------------|--------|
| 0 | Alternaria Leaf Spot | 663 |
| 1 | Healthy | 590 |
| 2 | Leaf Hopper & Jassids | 771 |
| 3 | Leaf Miner | 849 |
| 4 | Not Groundnut | 510 |
| 5 | Late & Early Leaf Spot | 414 |
| 6 | Rust | 301 |
| 7 | Tobacco Caterpillar | 769 |

---

## 🔧 Methodology
1. **Image Acquisition:** Field collection using mobile cameras  
2. **Manual Preprocessing:** Removing blurry images, mixed infections  
3. **Data Augmentation:** Random flip & rotation  
4. **Model Training:** Multiple custom CNN models  
5. **Evaluation:** Selecting the best performing model  
6. **Prediction:** Softmax confidence scoring on outputs  

---

## 🧠 Model Architectures

### **Model 1 – Custom CNN (3 Layers)**
- Convolutional blocks: 3  
- Filters: 16 → 32 → 64  
- Max pooling layers  
- Dense layer (128 units)  
- Output: 7 classes  

### **Model 2 – Custom CNN (6 Layers)**
- Convolutional blocks: 6  
- Filters: 32, then five layers of 64  
- Max pooling after each convolution  
- Dense layer: 64 units  
- Softmax output: 8 classes  
- Achieved highest accuracy (**97%**)  

---

## 📊 Results

| Model | Layers | Data Augmentation | Epochs | Accuracy | Classes |
|------|--------|-------------------|--------|----------|---------|
| Model 0 | 3 | No | 15 | 89% | 6 |
| Model 1 | 3 | Yes | 15 | 91% | 7 |
| Model 2 | 6 | No | 30 | 93% | 8 |
| **Model 3 (Best)** | **6** | **Yes** | **30** | **97%** | **8** |

---

## 🔮 Future Scope
- Expand dataset with more diseases/pests
- Increase variability in Not Groundnut class using open datasets
- Build a hierarchical classification pipeline:
  - Plant vs Non-plant
  - Groundnut vs Other Plant
  - Healthy vs Diseased
  - Disease/Pest classifier
- Deploy as a mobile application with on-device lightweight model
- Use explainability methods (GradCAM) to visualize disease regions

---
## ✨ Acknowledgments
- ICRISAT for real-field image collection and expert labeling
