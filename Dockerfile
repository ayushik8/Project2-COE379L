FROM tensorflow/tensorflow:2.13.0
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY best_model.h5 .

ENV MODEL_PATH=best_model.h5
ENV PORT=5000

EXPOSE 5000

CMD ["python", "app.py"]