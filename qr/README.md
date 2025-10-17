# 🎓 QR Code-Based Attendance System

A simple and effective Python-based QR Code Attendance System designed for educational institutions and training environments. This project enables quick and accurate attendance tracking using QR codes and SQLite, with easy export to CSV for reporting.

---

## 🚀 Features

- 🔧 **QR Code Generator**  
  Generate unique QR codes for students using their Name, Registration ID, and Section.

- 📷 **Attendance Scanner**  
  Scan QR codes in real-time using a webcam and store attendance records in a **SQLite3 database**.

- 📄 **Export to CSV**  
  Easily export all attendance data to a `.csv` file for further processing or reporting.

---

## 🗂️ Project Structure

```bash
├── qr_generator.py       # Generates QR codes for each student
├── qr_scanner.py         # Scans QR code and stores data in SQLite3
├── export_csv.py         # Exports attendance database to CSV
├── /                     # Folder to store generated QR images
├── attendance.db         # SQLite3 database file
└── attendance.csv        # Exported attendance data (generated)
```
🧰 Technologies Used
- Python 3
- OpenCV (cv2)
- qrcode library
- sqlite3
- csv
## 📦 Setup & Usage

### 🔧 Install Required Packages

```bash
pip install opencv-python qrcode
```

---

### 🧾 Generate QR Codes

```bash
python qr_generator.py
```

➡️ Edit the prompts inside the Generate_qr.py **Name**, **Reg ID**, and **Section**.  
📁 QR images will be saved in the `main` folder.

---

### 🎥 Scan and Record Attendance

```bash
python qr_scanner.py
```

➡️ Use your webcam to scan student QR codes.  
🗃️ Entries will be automatically saved in the **SQLite database**.

---

### 📤 Export Attendance Data

```bash
python export_csv.py
```

➡️ Generates an `attendance.csv` file with all recorded entries for further use or reporting.

---

## 📌 Future Improvements

- [ ] Add GUI using **Tkinter** or **PyQt**
- [ ] Admin panel for reviewing and managing records
- [ ] CSV import for **bulk QR generation**
- [ ] Attendance filtering by **date** or **section**

---

## 👨‍💻 Author
<img src="https://github.com/user-attachments/assets/db3e588b-776c-4e75-a504-bef9e299ca72" alt="CTI Banner" width="400"/>
