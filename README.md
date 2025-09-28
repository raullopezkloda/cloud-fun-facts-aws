# ☁️ Cloud Fun Facts Generator

Aplicación serverless que combina AWS Lambda, DynamoDB y Bedrock para generar fun facts sobre cloud computing con inteligencia artificial.

<img width="5000" height="4031" alt="Cloud Fun Facts AWS " src="https://github.com/user-attachments/assets/71f7f2a1-6113-48f6-a52a-299510aac351" />


## 🛠️ Servicios AWS utilizados

- **AWS Lambda**: Backend serverless
- **API Gateway**: Endpoint REST  
- **DynamoDB**: Base de datos NoSQL
- **Amazon Bedrock**: IA generativa (Claude Sonnet 4)
- **IAM**: Gestión de permisos

## 🚀 Funcionamiento

1. Usuario accede al sitio web
2. Hace clic en "Generar Fun Fact"
3. API Gateway recibe la solicitud
4. Lambda consulta DynamoDB
5. Bedrock mejora el fact con IA
6. Se devuelve la respuesta ingeniosa

