# 🚗 Car Selling Website – Chatbot Backend

A **website-aware chatbot backend** built with **FastAPI (Python)** that assists users on a car-selling website by answering questions **strictly using website data stored in Supabase**.

The chatbot can:
- Recommend cars within a given budget
- Answer questions about available cars
- Provide showroom locations
- Answer FAQs and website-related queries
- Integrate seamlessly with a **Next.js frontend**

---

## 🧠 Key Features

- ✅ FastAPI backend (Python 3.12)
- ✅ Supabase (PostgreSQL) as the data source
- ✅ Rule-based + data-driven chatbot (no hallucinations)
- ✅ Clean, scalable project architecture
- ✅ Future-ready for NLP / RAG / AI enhancements
- ✅ Secure environment-based configuration

---


---

## 🛠️ Tech Stack

| Layer | Technology |
|------|-----------|
Backend | FastAPI |
Language | Python 3.12 |
Database | Supabase (PostgreSQL) |
Validation | Pydantic v2 |
Server | Uvicorn |
Frontend | Next.js (separate repo) |

---

## 📦 Dependencies (Locked Versions)

```txt
fastapi==0.124.4
uvicorn[standard]==0.38.0
supabase==2.27.0
pydantic==2.12.5
python-dotenv==1.2.1

