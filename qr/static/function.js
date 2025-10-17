// DOMContentLoaded: modal setup
document.addEventListener('DOMContentLoaded', () => {
    const qrModal = document.getElementById('qrModal');
    const closeModal = document.getElementById('closeModal');
    let modalTimer; 

    // Open QR modal
    function openModal(qrSrc) {
        if (!qrModal) return;
        document.getElementById('modalQrImage').src = qrSrc;
        qrModal.style.display = 'block';

        if (modalTimer) clearTimeout(modalTimer);

        // Auto-close after 15 minutes
        modalTimer = setTimeout(() => {
            qrModal.style.display = 'none';
            document.getElementById('modalQrImage').src = '';
        }, 900000);
    }

    // Close QR modal
    function hideModal() {
        if (!qrModal) return;
        qrModal.style.display = 'none';
        document.getElementById('modalQrImage').src = '';
        if (modalTimer) clearTimeout(modalTimer);
    }

    if (closeModal) closeModal.addEventListener('click', hideModal);
    if (qrModal) {
        window.addEventListener('click', (e) => {
            if (e.target === qrModal) hideModal();
        });
    }
});

// -----------------------
// Open/Close Add Teacher Modal
// -----------------------
function openAddModal() {
    document.getElementById('addModal').style.display = 'flex';
}

function closeAddModal() {
    document.getElementById('addModal').style.display = 'none';
}

// -----------------------
// Submit Add Teacher
// -----------------------
async function submitAddTeacher() {
    const name = document.getElementById('teacherName').value.trim();
    const subject = document.getElementById('teacherSubject').value.trim();
    const form_link = document.getElementById('teacherFormLink').value.trim();

    if (!name || !subject || !form_link) {
        alert('All fields are required');
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/add-teacher', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, subject, form_link })
        });

        const data = await response.json();
if (data.error) {
    alert(data.error);
    return;
}

// Add teacher card dynamically
addTeacherCard(data.teacher_id, data.name, data.subject);


        // Clear form and close modal
        closeAddModal();
        document.getElementById('teacherName').value = '';
        document.getElementById('teacherSubject').value = '';
        document.getElementById('teacherFormLink').value = '';

    } catch (err) {
        console.error(err);
        alert('Error adding teacher');
    }
}

// -----------------------
// Add Teacher Card to Dashboard
// -----------------------
function addTeacherCard(id, name, subject) {
    const grid = document.getElementById('teacherGrid');

    const card = document.createElement('div');
    card.className = 'teacher-card';
    card.dataset.teacherId = id;
    card.innerHTML = `
        <div class="card-header">
            <h3 class="teacherName">${name}</h3>
            <div class="subject">${subject}</div>
        </div>
        <div class="card-actions">
            <button class="generateQrBtn" onclick="generateQr(this)">Generate QR</button>
        </div>
    `;

    grid.appendChild(card);
}

// -----------------------
// Unified QR Generation
// -----------------------
async function generateQr(btn) {
    try {
        const card = btn.closest('.teacher-card');
        const teacherId = card.dataset.teacherId;
        const teacherName = card.querySelector('.teacherName')?.innerText || 'Unknown';
        const subjectName = card.querySelector('.subject')?.innerText || 'Unknown';

        // Step 1: Fetch form link from backend
        const res = await fetch(`http://127.0.0.1:5000/get-form-link/${teacherId}`);
        const data = await res.json();
        if (!res.ok || !data.form_link) {
            alert(`Form link not found for Teacher ID: ${teacherId}`);
            return;
        }

        // Step 2: Generate QR via backend
        const qrResponse = await fetch('http://127.0.0.1:5000/generate-qr', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data: data.form_link })
        });

        if (!qrResponse.ok) throw new Error('Failed to generate QR');

        const blob = await qrResponse.blob();
        const qrSrc = URL.createObjectURL(blob);

        // Step 3: Show QR modal
        document.getElementById('qrTeacherName').innerText = "Teacher Name: " + teacherName;
        document.getElementById('qrsubject').innerText = "Subject Name: " + subjectName;
        document.getElementById('modalQrImage').src = qrSrc;
        document.getElementById('qrModal').style.display = 'block';

    } catch (err) {
        alert('Error generating QR: ' + err.message);
        console.error(err);
    }
}
