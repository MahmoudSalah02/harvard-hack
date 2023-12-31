# Misfit Munch

<img src="IMG_1014.GIF">

**Misfit Munch** is a transformative platform designed to tackle the global challenge of food wastage, particularly targeting "ugly" or "wonky" produce. By bridging farmers and consumers, we ensure that produce otherwise dismissed due to its appearance finds its rightful place in our kitchens and plates, rather than being wasted.


## Features

1. **For Farmers**: An exclusive marketplace to showcase and sell their produce, regardless of its appearance.
2. **For Users**: A modern, efficient approach to meal planning:
    - **Fridge Scan**: Snap a photo of your fridge, and let our algorithm label the contents using the Google Cloud Vision API.
    - **Recipe Crafting**: Based on your fridge's content and our farmer partnerships, OpenAI ChatGPT API serves up tailored recipes.
    - **One-Click Purchase**: Fancy a recipe? Get all the ingredients with a single click, bypassing piecemeal shopping.

## Demo

### App Layout
<img width="891" alt="image" src="https://github.com/MahmoudSalah02/harvard-hack/assets/87628210/a672a12f-b95a-4e8d-90b6-27bbdbc53622">

### AI Layer Explained
<img width="891" alt="image" src="https://github.com/MahmoudSalah02/harvard-hack/assets/87628210/16ff047a-0a3e-4781-a0fc-75a646454afa">


## Technology Stack

- Backend: Flask, SQLite
- Image Recognition: Google Cloud Vision API, DeepLabV3
- Recipe Crafting: OpenAI ChatGPT API
- Frontend: HTML, CSS, Javascript

## Installation & Setup

```bash
# Clone the Repository
git clone <github_repo_link>
cd <repository_name>

# Setup Virtual Environment (Optional but Recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install Dependencies
pip install -r requirements.txt

# Setup Google Cloud Credentials
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/keyfile.json"

# Run the Application
flask run

# Open the application in your preferred browser at
http://127.0.0.1:5000/
```

## Contributors

### **Fuka Ikeda**: 
- *Brown 26' Design Engineering*
- Hardware Design + UI/UX

### **Marco Qin**: 
- *Brandeis 24' CS+Math*
- Backend + AI

### **Mahmoud Salah**: 
- *Brandeis 24' CS+Math*
- Frontend + Backend + AI

### **Omari Emmanuel**: 
- *Queen's 26' Data Analytics*
- Content Creation + Frontend

<img width="748" alt="image" src="https://github.com/MahmoudSalah02/harvard-hack/assets/87628210/6e58dbff-e06f-48f6-ab90-62e9f38e5479">


## Future Direction

1. We want to continue working by trying to validate the market and see if there is a strong demand.
2. Understand the local laws of drones and the viability of transporting goods and services using drones, figuring out how to engage with regulatory bodies.
3. Secure funding by applying to grants, which also validates our ideas as well as giving us a head start in purchasing delivery drones 

Misfit Munch is not merely a solution; it's a revolution. We aim to continue refining our platform, actively contributing to the nexus between reducing food wastage and promoting healthier eating.
