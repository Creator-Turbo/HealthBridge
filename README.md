# HealthBridge 

### Table of Contents
- [Demo](#demo)
- [Overview](#overview)
- [Motivation](#motivation)
- [Technical Aspect](#technical-aspect)
- [Installation](#installation)
- [Run](#run)
- [Directory Tree](#directory-tree)
- [To Do](#to-do)
- [Bug / Feature Request](#bug--feature-request)
- [Technologies Used](#technologies-used)
- [Team](#team)
- [License](#license)
- [Credits](#credits)

---
## Demo
HealthBridge is a smart healthcare coordination platform designed to connect patients, clinics, hospitals, pharmacies, and NGOs through a unified digital ecosystem for real-time, efficient healthcare delivery.<br>
**Link to Demo:** [comming-soon](#) 





![Poem-Classification](https://img.freepik.com/premium-photo/medical-doctor-with-digital-tablet-medical-network-concept_488220-4946.jpg?w=996)

---

## Overview
HealthBridge bridges the gap between underserved communities and quality healthcare services by offering a digital-first solution with features like:

- Appointment scheduling

- Electronic health record (EHR) access

- Telemedicine services

- Medication reminders

- Real-time healthcare resource tracking

- AI-powered 24/7 chatbot assistance

- Secure and multilingual patient engagement



  The platform supports patients, clinics, hospitals, and outreach programs through personalized interfaces, data-driven tools, and collaborative coordination.
---

## Motivation

Access to healthcare remains a global challenge, especially in marginalized areas. Geographic isolation, lack of infrastructure, communication inefficiencies, and poor resource planning continue to block access to timely care. HealthBridge was created to:

- Connect fragmented healthcare systems

- Optimize medical supply management

- Provide instant communication tools

- Deliver scalable, AI-driven solutions

- Improve health outcomes via timely interventions



---

## Technical Aspect

Frontend
- HTML, CSS, JavaScript

Backend
- Flask: Web framework and API handler

- Appwrite: User authentication, storage, and access control

Database
- MongoDB: NoSQL database for health records, chat logs, and resources

- FAISS / Pinecone: Vector DBs for semantic search and document retrieval

AI & NLP
- LangChain: For LLM orchestration and smart conversations

- AI Chatbot: Handles user queries, bookings, and document navigation

Medical Data Handling
- PyMuPDF, PDFPlumber: Extracts structured data from scanned documents and PDFs

Development Tools
- VS Code, Git, GitHub




---

## Installation
The Code is written in Python 3.10. Install the required packages and libraries by running:

```bash
pip install -r requirements.txt
```

## Run
To run the Flask web app locally:

```bash
python app.py
```



## Directory Tree 
```
📁 HealthBridge/
├── 📄 .env
├── 📄 .gitignore
├── 📄 LICENSE
├── 📄 README.md
├── 📄 app.py
├── 📄 requirements.txt
├── 📄 setup.py
├── 📄 template.py
├── 📁 .github/
├── 📁 .vscode/
├── 📁 data/
├── 📁 Experiments/
├── 📁 logs/
├── 📁 HealthBridge.egg-info/
├── 📁 src/
├── 📁 static/
├── 📁 templates/
└── 📁 venv/
```

## To Do

-  Integration with IoT and wearable devices

-  Blockchain-based medical record storage

 - Multilingual and accessible UI enhancements

-  Predictive analytics for disease outbreak and risk monitoring

- AI-powered clinical decision support tools

-  Virtual health communities for chronic care and mental health

## Bug / Feature Request
If you encounter any bugs or want to request a new feature, please open an issue on GitHub. Contributions are welcome!

## Technologies Used
- 🧩 Flask – Lightweight web framework for building the backend API
- 🧱 Appwrite – Backend server for authentication, database, and storage
- 🍃 MongoDB – NoSQL database for storing structured user and chat data
- 🌲 FAISS / Pinecone – Vector databases for efficient semantic search and retrieval
- 🦜🔗 LangChain – LLM orchestration and chaining prompts/tools
- 📄 PyMuPDF, PDFPlumber – PDF parsing libraries for extracting medical content
- 🖥️ HTML / 🎨 CSS / ⚡ JavaScript – Frontend stack for building a responsive user interface
- 🧠 Git + 🐙 GitHub – Version control and collaboration tools
- 🖊️ VS Code – Primary code editor for development



![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://i.imgur.com/Ggvqguk.png" width=170>](https://python.langchain.com/docs/introduction/) 
[<img target="_blank" src="https://icon2.cleanpng.com/20180829/okc/kisspng-flask-python-web-framework-representational-state-flask-stickker-1713946755581.webp" width=170>](https://flask.palletsprojects.com/en/stable/) 
[<img target="_blank" src="https://i.imgur.com/hWZ8OWK.png" width=170>](https://docs.pinecone.io/guides/get-started/overview) 

[<img target="_blank" src="https://logowik.com/content/uploads/images/hugging-face1720994339.logowik.com.webp" width=170>](https://huggingface.co/docs) 
[<img target="_blank" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEc9A_S6BPxCDRp5WjMFEfXrpCu1ya2OO-Lw&s" width=170>](https://developer.mozilla.org/en-US/docs/Web/HTML) 
[<img target="_blank" src="https://cdn-icons-png.flaticon.com/512/919/919826.png" width=170>](https://developer.mozilla.org/en-US/docs/Web/CSS) 



---

## Team
This project was developed by:


| [![Bablu](https://github.com/Creator-Turbo/images-/blob/main/resized_image.png?raw=true)](https://your-resume-link.com) | [![Anjali](https://github.com/Creator-Turbo/images-/blob/main/resized_image.png?raw=true)](https://resume-link2.com) | [![Ravi](https://github.com/Creator-Turbo/images-/blob/main/resized_image.png?raw=true)](https://resume-link3.com) | [![Sneha](https://github.com/Creator-Turbo/images-/blob/main/resized_image.png?raw=true)](https://resume-link4.com) |
|:--:|:--:|:--:|:--:|
| **Bablu Kumar Pandey**<br>*Terema Developer* | **Anjali Sharma**<br>*Backend Developer* | **Ravi Verma**<br>*NLP Engineer* | **Sneha Das**<br>*UI/UX Designer* |



## License

This project is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this software under the terms of the MIT License. For more details, see the [LICENSE](LICENSE) file included in this repository.

## Credits

- WHO, UNDP, and global health research for insights

- Open-source tools and libraries from the Python, Flask, and AI communities

- Render.com for free deployment support

- LangChain and Hugging Face for AI framework support


