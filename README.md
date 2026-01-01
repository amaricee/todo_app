Cara menjalankan aplikasinya

untuk BACKEND
- buat database baru (mysql)
- copy .env.example -> .env
- masukkan db_password (opsional jika pakai)
- masukkan db_name

lalu diterminal:
- masuk ke folder backend 
- python -m venv venv
- source venv/bin/activate (linux/macOS)
- di windows ketik source venv/Scripts/activate (git bash), venv\Scripts\activate.bat (command prompt), venv\Scripts\Activate.ps1 (powerShell)
- pip install -r requirements.txt
- python migrate.py
- python app.py


untuk FRONTEND
- copy .env.example -> .env
- ganti dengan url be anda 
- contoh: http://127.0.0.1:5000/api


lalu diterminal:
- masuk ke folder frontend
- npm install
- npm run dev

sekian hatur tengkyu terima kasih:)