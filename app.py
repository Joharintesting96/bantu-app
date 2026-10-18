import streamlit as st

# 1. Konfigurasi Halaman (Mesti diletak di atas sekali)
st.set_page_config(page_title="Bantu - Penyelesaian Spreadsheet", page_icon="📊", layout="centered")

# 2. Suntikan CSS (Latar Belakang Biru Gelap & Animasi Fade)
st.markdown("""
<style>
    /* Warna latar belakang biru gelap & tulisan putih */
    [data-testid="stAppViewContainer"] {
        background-color: #0B192C;
        color: #FFFFFF;
    }
    [data-testid="stHeader"] {
        background-color: transparent;
    }
    
    /* Kelas untuk animasi Fade In */
    .fade-in {
        animation: fadeIn 2s ease-in-out;
        text-align: center;
        font-size: 20px;
        margin-top: 15%;
        margin-bottom: 10%;
        line-height: 1.6;
    }
    
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    /* Cantikkan Butang */
    div.stButton > button {
        border-radius: 8px;
        width: 100%;
        background-color: #1A365D;
        color: white;
        border: 1px solid #4299E1;
        padding: 10px;
    }
    div.stButton > button:hover {
        background-color: #2B6CB0;
        border-color: white;
    }
</style>
""", unsafe_allow_html=True)

# 3. Pengurusan State (Session State) untuk menavigasi page
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'lang' not in st.session_state:
    st.session_state.lang = 'ms'
if 'pitch_step' not in st.session_state:
    st.session_state.pitch_step = 1

def next_page():
    st.session_state.page += 1

def set_lang_and_next(lang):
    st.session_state.lang = lang
    st.session_state.page += 1

def next_pitch():
    if st.session_state.pitch_step < 4:
        st.session_state.pitch_step += 1
    else:
        st.session_state.page += 1
        st.session_state.pitch_step = 1 # reset for safety

# 4. Kamus Terjemahan (Bahasa Melayu & English)
t = {
    'ms': {
        'teruskan': 'Teruskan >',
        'pitch1': 'Penat menghadap fail Excel yang asyik keluar formula error?',
        'pitch2': 'Terpaksa buat kerja kemasukan data berulang kali setiap hujung bulan secara manual?',
        'pitch3': 'Kami akan mudahkan urusan pejabat anda. Saya bantu baiki ralat spreadsheet, automasikan tugas manual, dan bina papan pemuka (dashboard) yang kemas serta mudah digunakan.',
        'pitch4': 'Jangan malu-malu bagitau problem, benda boleh setel.',
        'pkg1_title': '📦 Pakej 1: Baiki Ralat & Formula Spreadsheet (RM 50)',
        'pkg1_desc': '• Khidmat Pantas Baiki Error Excel & Google Sheet\n\n• Masalah diselesaikan: Ralat #REF!, #VALUE!, formula terpadam, atau data berterabur.\n\n• Terhad kepada 1 fail. Sekiranya ada fail tambahan akan ada penambahan harga.',
        'pkg2_title': '⚙️ Pakej 2: Automasi & Templat Khas (Bermula RM 100)',
        'pkg2_desc': '• Automasi Aliran Kerja & Templat Pintar\n\n• Hentikan kerja salin-tampal berulang kali, sambungkan borang Google Form terus ke Sheet, atau bina formula gabungan.',
        'pkg3_title': '📊 Pakej 3: Papan Pemuka (Dashboard) & UI Ringkas (Bermula RM 500)',
        'pkg3_desc': '• Papan Pemuka Visual & Antaramuka Mudah\n\n• Mengubah data mentah (raw data) menjadi laporan visual yang kemas untuk pembentangan kepada pihak pengurusan dan sebagainya.',
        'contact_title': 'Selesaikan Masalah Anda Hari Ini',
        'contact_label': 'Ceritakan masalah fail anda di sini:',
        'btn_submit': 'Hantar Masalah',
        'msg_success': 'Mesej anda telah dihantar! Kami akan hubungi anda segera.',
        'or': 'ATAU',
        'btn_tele': '📱 Hubungi terus di Telegram'
    },
    'en': {
        'teruskan': 'Continue >',
        'pitch1': 'Tired of facing Excel files that keep showing formula errors?',
        'pitch2': 'Forced to do repetitive manual data entry every month-end?',
        'pitch3': 'We will simplify your office tasks. I help fix spreadsheet errors, automate manual tasks, and build neat, easy-to-use dashboards.',
        'pitch4': 'Don\'t be shy to tell us your problem, everything can be settled.',
        'pkg1_title': '📦 Package 1: Fix Spreadsheet Errors (RM 50)',
        'pkg1_desc': '• Fast Service to Fix Excel & Google Sheet Errors\n\n• Problems solved: #REF!, #VALUE! errors, deleted formulas, or messy data.\n\n• Limited to 1 file. Additional files will incur extra charges.',
        'pkg2_title': '⚙️ Package 2: Automation & Custom Templates (From RM 100)',
        'pkg2_desc': '• Workflow Automation & Smart Templates\n\n• Stop repetitive copy-pasting, connect Google Forms directly to Sheets, or build complex combined formulas.',
        'pkg3_title': '📊 Package 3: Dashboard & Simple UI (From RM 500)',
        'pkg3_desc': '• Visual Dashboard & Simple Interface\n\n• Turn raw data into neat visual reports for management presentations and more.',
        'contact_title': 'Solve Your Problem Today',
        'contact_label': 'Tell us about your spreadsheet issues here:',
        'btn_submit': 'Submit Problem',
        'msg_success': 'Your message has been sent! We will contact you shortly.',
        'or': 'OR',
        'btn_tele': '📱 Contact directly via Telegram'
    }
}

# Shortcut untuk bahasa pilihan
lang = st.session_state.lang

# ---------------------------------------------------------
# Page 1: Logo Landing Page
# ---------------------------------------------------------
if st.session_state.page == 1:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    # Masukkan logo (pastikan fail logo berada dalam folder yang sama)
    try:
        st.image("watermarked_img_1383082827796455556.jpg", use_column_width=True)
    except:
        st.warning("Sila pastikan fail gambar logo ada di dalam folder.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    if st.button("Teruskan >", key="p1_next"):
        next_page()
        st.rerun()

# ---------------------------------------------------------
# Page 2: Pilihan Bahasa
# ---------------------------------------------------------
elif st.session_state.page == 2:
    st.markdown('<div class="fade-in">Sila Pilih Bahasa<br><br><small>Please Select Language</small></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Bahasa Melayu"):
            set_lang_and_next('ms')
            st.rerun()
    with col2:
        if st.button("English"):
            set_lang_and_next('en')
            st.rerun()

# ---------------------------------------------------------
# Page 3: Teks Pitching Bersiri (Step 1 to 4)
# ---------------------------------------------------------
elif st.session_state.page == 3:
    step = st.session_state.pitch_step
    
    # Teks dipaparkan berdasarkan step semasa
    teks_semasa = t[lang][f'pitch{step}']
    
    # Menggunakan HTML dengan CSS class fade-in untuk efek yang smooth
    st.markdown(f'<div class="fade-in">{teks_semasa}</div>', unsafe_allow_html=True)
    
    # Ruang kosong ke bawah untuk butang
    for _ in range(5):
        st.write("")
        
    if st.button(t[lang]['teruskan'], key=f"pitch_btn_{step}"):
        next_pitch()
        st.rerun()

# ---------------------------------------------------------
# Page 4: Pakej 1
# ---------------------------------------------------------
elif st.session_state.page == 4:
    st.markdown(f'<div class="fade-in"><h3>{t[lang]["pkg1_title"]}</h3><br>{t[lang]["pkg1_desc"]}</div>', unsafe_allow_html=True)
    st.write("")
    if st.button(t[lang]['teruskan'], key="pkg1_btn"):
        next_page()
        st.rerun()

# ---------------------------------------------------------
# Page 5: Pakej 2
# ---------------------------------------------------------
elif st.session_state.page == 5:
    st.markdown(f'<div class="fade-in"><h3>{t[lang]["pkg2_title"]}</h3><br>{t[lang]["pkg2_desc"]}</div>', unsafe_allow_html=True)
    st.write("")
    if st.button(t[lang]['teruskan'], key="pkg2_btn"):
        next_page()
        st.rerun()

# ---------------------------------------------------------
# Page 6: Pakej 3
# ---------------------------------------------------------
elif st.session_state.page == 6:
    st.markdown(f'<div class="fade-in"><h3>{t[lang]["pkg3_title"]}</h3><br>{t[lang]["pkg3_desc"]}</div>', unsafe_allow_html=True)
    st.write("")
    if st.button(t[lang]['teruskan'], key="pkg3_btn"):
        next_page()
        st.rerun()

# ---------------------------------------------------------
# Page 7: Hubungi Kami / Input Masalah
# ---------------------------------------------------------
elif st.session_state.page == 7:
    st.markdown(f'<h3 style="text-align:center;">{t[lang]["contact_title"]}</h3>', unsafe_allow_html=True)
    
    # Borang Input direct dalam app
    user_issue = st.text_area(t[lang]['contact_label'], height=150)
    
    if st.button(t[lang]['btn_submit']):
        if user_issue:
            st.success(t[lang]['msg_success'])
        else:
            st.error("Sila isi masalah anda terlebih dahulu." if lang=='ms' else "Please fill in your problem first.")
    
    st.markdown(f'<div style="text-align:center; margin: 20px 0;">{t[lang]["or"]}</div>', unsafe_allow_html=True)
    
    # Butang ke Telegram menggunakan fungsi link_button Streamlit
    st.link_button(t[lang]['btn_tele'], "http://t.me/bantudotcom", use_container_width=True)
    
    st.write("")
    # Butang restart jika mereka mahu lihat kembali dari awal
    if st.button("🔄 Kembali ke Mula" if lang=='ms' else "🔄 Back to Start"):
        st.session_state.page = 1
        st.session_state.pitch_step = 1
        st.rerun()
