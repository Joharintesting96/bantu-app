<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bantu - Penyelesaian Spreadsheet</title>
    <style>
        /* Tetapan Asas & Latar Belakang */
        body {
            margin: 0;
            padding: 0;
            background-color: #0B192C; /* Biru Gelap */
            color: #FFFFFF;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            overflow-x: hidden;
        }

        /* Bekas Aplikasi (Mobile-friendly) */
        .app-container {
            width: 100%;
            max-width: 480px;
            min-height: 100vh;
            padding: 30px 20px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            justify-content: center;
            position: relative;
        }

        /* Tetapan Halaman & Animasi */
        .page {
            display: none; /* Sembunyikan semua page pada asalnya */
            flex-direction: column;
            align-items: center;
            text-align: center;
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.6s ease-out, transform 0.6s ease-out;
        }

        .page.active {
            display: flex;
            opacity: 1;
            transform: translateY(0);
        }

        /* Gaya Teks */
        h2 { font-size: 1.5rem; margin-bottom: 20px; }
        p { font-size: 1.1rem; line-height: 1.6; margin-bottom: 30px; }
        .text-pitch { font-size: 1.2rem; font-weight: 500; min-height: 120px; }

        /* Gaya Kad Katalog */
        .catalog-card {
            background-color: #1A365D;
            border: 1px solid #2B6CB0;
            border-radius: 12px;
            padding: 20px;
            text-align: left;
            margin-bottom: 20px;
            width: 100%;
            box-sizing: border-box;
        }
        .catalog-card h3 { margin-top: 0; color: #63B3ED; font-size: 1.2rem; }
        .catalog-card p { margin-bottom: 10px; font-size: 0.95rem; }

        /* Gaya Butang */
        button, .btn-link {
            background-color: #3182CE;
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 30px;
            font-size: 1.1rem;
            cursor: pointer;
            width: 100%;
            max-width: 300px;
            margin-top: 10px;
            transition: background-color 0.3s, transform 0.2s;
            text-decoration: none;
            display: inline-block;
            box-sizing: border-box;
            text-align: center;
        }
        button:hover, .btn-link:hover {
            background-color: #2B6CB0;
            transform: scale(1.02);
        }
        .btn-outline {
            background-color: transparent;
            border: 2px solid #3182CE;
        }

        /* Input Form */
        textarea {
            width: 100%;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #4A5568;
            background-color: #2D3748;
            color: white;
            font-size: 1rem;
            margin-bottom: 20px;
            box-sizing: border-box;
            resize: none;
        }
        
        /* Imej Logo */
        img.logo { width: 150px; margin-bottom: 30px; border-radius: 12px;}
    </style>
</head>
<body>

<div class="app-container">

    <!-- PAGE 1: LOGO -->
    <div id="page-1" class="page active">
        <img src="watermarked_img_1383082827796455556.jpg" alt="Logo Bantu" class="logo">
        <button onclick="goToPage(2)" id="btn-teruskan-1">Teruskan ></button>
    </div>

    <!-- PAGE 2: LANGUAGE SELECTION -->
    <div id="page-2" class="page">
        <h2>Pilih Bahasa / Select Language</h2>
        <button onclick="setLang('ms')" class="btn-outline">Bahasa Melayu</button>
        <button onclick="setLang('en')" class="btn-outline">English</button>
    </div>

    <!-- PAGE 3: PITCHING SEQUENCE -->
    <div id="page-3" class="page">
        <p id="pitch-text" class="text-pitch"></p>
        <button onclick="nextPitch()" id="btn-teruskan-pitch">Teruskan ></button>
    </div>

    <!-- PAGE 4: PAKEJ 1 -->
    <div id="page-4" class="page">
        <div class="catalog-card">
            <h3 id="pkg1-title">📦 Pakej 1: Baiki Ralat (RM 50)</h3>
            <p id="pkg1-desc">Masalah diselesaikan: Ralat #REF!, #VALUE!, formula terpadam.</p>
        </div>
        <button onclick="goToPage(5)" id="btn-teruskan-pkg1">Teruskan ></button>
    </div>

    <!-- PAGE 5: PAKEJ 2 -->
    <div id="page-5" class="page">
        <div class="catalog-card">
            <h3 id="pkg2-title">⚙️ Pakej 2: Automasi (Bermula RM 100)</h3>
            <p id="pkg2-desc">Hentikan kerja salin-tampal berulang kali, sambungkan Google Form terus ke Sheet.</p>
        </div>
        <button onclick="goToPage(6)" id="btn-teruskan-pkg2">Teruskan ></button>
    </div>

    <!-- PAGE 6: PAKEJ 3 -->
    <div id="page-6" class="page">
        <div class="catalog-card">
            <h3 id="pkg3-title">📊 Pakej 3: Papan Pemuka (Bermula RM 500)</h3>
            <p id="pkg3-desc">Mengubah raw data menjadi laporan visual yang kemas untuk pengurusan.</p>
        </div>
        <button onclick="goToPage(7)" id="btn-teruskan-pkg3">Teruskan ></button>
    </div>

    <!-- PAGE 7: CONTACT -->
    <div id="page-7" class="page">
        <h2 id="contact-title">Selesaikan Masalah Anda</h2>
        <textarea id="contact-input" rows="4" placeholder="Ceritakan masalah fail anda di sini..."></textarea>
        <button onclick="submitForm()" id="btn-submit">Hantar Masalah</button>
        
        <p style="margin: 15px 0;">ATAU</p>
        
        <a href="http://t.me/bantudotcom" target="_blank" class="btn-link" id="btn-telegram">📱 Hubungi di Telegram</a>
    </div>

</div>

<script>
    // --- KAMUS TRANSLATION ---
    const t = {
        'ms': {
            'teruskan': 'Teruskan >',
            'pitch': [
                "Penat menghadap fail Excel yang asyik keluar formula error?",
                "Terpaksa buat kerja kemasukan data berulang kali setiap hujung bulan secara manual?",
                "Kami akan mudahkan urusan pejabat anda. Saya bantu baiki ralat spreadsheet, automasikan tugas manual, dan bina papan pemuka (dashboard) yang kemas serta mudah digunakan.",
                "Jangan malu-malu bagitau problem, benda boleh setel."
            ],
            'pkg1_title': "📦 Pakej 1: Baiki Ralat (RM 50)",
            'pkg1_desc': "Khidmat Pantas Baiki Error Excel & Google Sheet.<br><br>Masalah diselesaikan: Ralat #REF!, #VALUE!, formula terpadam, atau data berterabur.<br><br><i>Terhad kepada 1 file. Penambahan harga untuk fail tambahan.</i>",
            'pkg2_title': "⚙️ Pakej 2: Automasi (Bermula RM 100)",
            'pkg2_desc': "Automasi Aliran Kerja & Templat Pintar.<br><br>Hentikan kerja salin-tampal berulang kali, sambungkan borang Google Form terus ke Sheet, atau bina formula gabungan.",
            'pkg3_title': "📊 Pakej 3: Papan Pemuka (Bermula RM 500)",
            'pkg3_desc': "Papan Pemuka Visual & Antaramuka Mudah.<br><br>Mengubah raw data menjadi laporan visual yang kemas untuk pembentangan kepada pihak pengurusan dan sebagainya.",
            'contact_title': "Selesaikan Masalah Anda",
            'contact_placeholder': "Ceritakan masalah fail anda di sini...",
            'btn_submit': "Hantar Masalah",
            'msg_success': "Mesej dihantar! Kami akan hubungi anda segera."
        },
        'en': {
            'teruskan': 'Continue >',
            'pitch': [
                "Tired of facing Excel files that keep showing formula errors?",
                "Forced to do repetitive manual data entry every month-end?",
                "We will simplify your office tasks. I help fix spreadsheet errors, automate manual tasks, and build neat, easy-to-use dashboards.",
                "Don't be shy to tell us your problem, everything can be settled."
            ],
            'pkg1_title': "📦 Package 1: Fix Errors (RM 50)",
            'pkg1_desc': "Fast Service to Fix Excel & Google Sheet Errors.<br><br>Problems solved: #REF!, #VALUE!, deleted formulas, or messy data.<br><br><i>Limited to 1 file. Extra charges apply for additional files.</i>",
            'pkg2_title': "⚙️ Package 2: Automation (From RM 100)",
            'pkg2_desc': "Workflow Automation & Smart Templates.<br><br>Stop repetitive copy-pasting, connect Google Forms directly to Sheets, or build complex combined formulas.",
            'pkg3_title': "📊 Package 3: Dashboard (From RM 500)",
            'pkg3_desc': "Visual Dashboard & Simple Interface.<br><br>Turn raw data into neat visual reports for management presentations and more.",
            'contact_title': "Solve Your Problem Today",
            'contact_placeholder': "Tell us about your spreadsheet issues here...",
            'btn_submit': "Submit Problem",
            'msg_success': "Message sent! We will contact you shortly."
        }
    };

    let currentLang = 'ms';
    let pitchIndex = 0;

    // --- FUNGSI TUKAR PAGE (DENGAN ANIMASI) ---
    function goToPage(pageNumber) {
        // Cari page yang sedang aktif
        const activePage = document.querySelector('.page.active');
        
        // Buang kelas aktif supaya ia fade out (opacity 0)
        activePage.classList.remove('active');
        
        // Tunggu animasi fade out habis (0.6s), kemudian tunjuk page baru
        setTimeout(() => {
            const nextPage = document.getElementById('page-' + pageNumber);
            nextPage.classList.add('active');
        }, 500); // Masa delay sedikit pantas dari animasi css untuk efek smooth
    }

    // --- FUNGSI SET BAHASA ---
    function setLang(lang) {
        currentLang = lang;
        updateTextContent();
        pitchIndex = 0; // Reset penceritaan
        updatePitchText();
        goToPage(3);
    }

    // --- FUNGSI KEMASKINI TEKS MENGIKUT BAHASA ---
    function updateTextContent() {
        const d = t[currentLang];
        document.getElementById('btn-teruskan-1').innerHTML = d.teruskan;
        document.getElementById('btn-teruskan-pitch').innerHTML = d.teruskan;
        document.getElementById('btn-teruskan-pkg1').innerHTML = d.teruskan;
        document.getElementById('btn-teruskan-pkg2').innerHTML = d.teruskan;
        document.getElementById('btn-teruskan-pkg3').innerHTML = d.teruskan;

        document.getElementById('pkg1-title').innerHTML = d.pkg1_title;
        document.getElementById('pkg1-desc').innerHTML = d.pkg1_desc;
        document.getElementById('pkg2-title').innerHTML = d.pkg2_title;
        document.getElementById('pkg2-desc').innerHTML = d.pkg2_desc;
        document.getElementById('pkg3-title').innerHTML = d.pkg3_title;
        document.getElementById('pkg3-desc').innerHTML = d.pkg3_desc;

        document.getElementById('contact-title').innerHTML = d.contact_title;
        document.getElementById('contact-input').placeholder = d.contact_placeholder;
        document.getElementById('btn-submit').innerHTML = d.btn_submit;
    }

    // --- FUNGSI ANIMASI PITCHING TEKS KELUAR MASUK (PAGE 3) ---
    function updatePitchText() {
        const pitchTextElement = document.getElementById('pitch-text');
        
        // Efek fade out teks lama
        pitchTextElement.style.opacity = 0;
        pitchTextElement.style.transform = "translateY(10px)";
        
        setTimeout(() => {
            // Tukar teks selepas ia ghaib
            pitchTextElement.innerHTML = t[currentLang]['pitch'][pitchIndex];
            
            // Efek fade in teks baru
            pitchTextElement.style.transition = "opacity 0.5s ease, transform 0.5s ease";
            pitchTextElement.style.opacity = 1;
            pitchTextElement.style.transform = "translateY(0)";
        }, 400); // Tunggu 400ms sebelum teks baru muncul
    }

    function nextPitch() {
        pitchIndex++;
        if (pitchIndex < t[currentLang]['pitch'].length) {
            updatePitchText();
        } else {
            goToPage(4); // Ke katalog selepas pitching tamat
        }
    }

    // --- FUNGSI BUTANG HANTAR ---
    function submitForm() {
        const input = document.getElementById('contact-input').value;
        if(input.trim() === "") {
            alert(currentLang === 'ms' ? "Sila isi masalah anda terlebih dahulu." : "Please fill in your problem first.");
            return;
        }
        alert(t[currentLang]['msg_success']);
        document.getElementById('contact-input').value = ""; // Kosongkan form
    }
</script>

</body>
</html>
