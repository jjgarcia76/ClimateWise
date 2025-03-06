# 🌦 Climate Wise - API de Predicción del Clima

**Climate Wise** es una API desarrollada con **FastAPI** que predice la temperatura basada en la **humedad y la presión**.

## 🚀 ¿Cómo funciona?
La API utiliza un modelo de **Machine Learning** entrenado con datos meteorológicos para hacer predicciones de temperatura.

## 🛠 Endpoints

### 📌 `GET /`
✅ **Descripción:** Verifica que la API esté activa.  
✅ **Ejemplo de respuesta:**
```json
{
  "message": "API Climate Wise está funcionando 🚀"
}
```

### 📌 `POST /predict/`
✅ **Descripción:** Recibe datos de **humedad y presión** y devuelve la predicción de temperatura.  
✅ **Ejemplo de solicitud:**
```json
{
  "humidity": 60.5,
  "pressure": 1012
}
```
✅ **Ejemplo de respuesta:**
```json
{
  "predicted_temperature": 24.99
}
```

## 🚀 Instalación y Ejecución Local
1. **Clona el repositorio**  
   ```bash
   git clone https://github.com/jjgarcia76/ClimateWise.git
   cd ClimateWise
   ```
2. **Instala las dependencias**  
   ```bash
   pip install fastapi uvicorn joblib numpy pydantic scikit-learn
   ```
3. **Ejecuta el servidor**  
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```
4. **Prueba en tu navegador:**  
   - 🌐 **Documentación interactiva:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
   - 📚 **Redoc UI:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---
🚀 **¡Gracias por usar Climate Wise!** 🌦
