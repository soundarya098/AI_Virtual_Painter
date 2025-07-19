# AI_Virtual_Painter
An AI-powered virtual painting app using OpenCV, MediaPipe, and Python.

# 🎨 AI Virtual Painter 🎨

AI Virtual Painter is an interactive computer vision application that allows users to draw in the air using their hand gestures. Built using Python, OpenCV, MediaPipe, and TensorFlow Lite, this tool turns your webcam into a virtual canvas.

It’s designed especially for fun, creative expression and also offers accessibility features that could assist people with limited physical interaction — a great step toward touchless drawing!

# 🧠 Features
✋ Hand Gesture Recognition using MediaPipe
🎨 Dynamic Drawing Canvas with colored brush strokes
🖌️ Adjustable Brush Size based on finger distance
🧽 Eraser Mode activated with a gesture
🌈 Rainbow Brush Mode that cycles through colors
🔊 Voice Feedback announces the selected brush color
🖼️ Save Artwork as PNG image with a single key press
🧠 AI Features (Optional): Placeholder for integrating AI-based shape suggestions

# 📹 How It Works
Uses the webcam to detect hand landmarks.
Tracks the index finger to draw lines on the screen.
Detects pinch gesture (thumb + index finger) to:
Clear the screen
Toggle modes (color selection, eraser, etc.)
Provides auditory feedback using text-to-speech.

# Tech                # Description                                          

 **Python**      -     Core programming language                            
 **OpenCV**      -    Real-time video processing and drawing               
 **MediaPipe**   -     Hand tracking and gesture recognition                
 **NumPy**       -     Efficient numerical operations                       
 **pyttsx3**     -     Voice feedback module for speaking text              
 **TensorFlow Lite** - (Optional) for AI-drawn suggestions (future feature) 

 # 🖼️ Screenshots

<br>![WhatsApp Image 2025-07-19 at 19 01 05_2eedef1a](https://github.com/user-attachments/assets/f94f8415-6eb0-4040-86db-2ad2cbe1ff10)</br>

<br>![WhatsApp Image 2025-07-19 at 19 00 48_f23dc111](https://github.com/user-attachments/assets/eb9f96e3-ebca-4ac5-b622-1d32ccbacce7)</br>

# 🛠️ Setup Instructions

# Step 1: Clone the repository
git clone https://github.com/yourusername/AI_Virtual_Painter.git
cd AI_Virtual_Painter

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the application
python virtual_painter.py

# 📁Files in This Project
 # File                  # Purpose                                    
 
 `virtual_painter.py` - Main application code                      
 `requirements.txt`   - List of all dependencies                   
 `README.md`          - Documentation and project description      
 `/assets/`           -  Screenshots or visual resources (optional) 




