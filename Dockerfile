# Użyj oficjalnego obrazu z Pythonem 3.11
FROM python:3.11-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj pliki
COPY . .

# Zainstaluj zależności
RUN pip install --upgrade pip && pip install -r requirements.txt

# Uruchom bota
CMD ["python", "bot.py"]
