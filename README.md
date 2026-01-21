🚗 Odoo CarRental — Gestión de Reservas








📚 Proyecto Académico — Sistemas de Gestión Empresarial (DAM 2B)
Desarrollo de un módulo personalizado para Odoo 17 orientado a la gestión integral de una empresa de alquiler de vehículos.

📌 Descripción

El módulo gestion_reservas amplía Odoo 17 para cubrir todo el ciclo de alquiler de coches:

Gestión de flota

Reservas con validaciones

Descuentos VIP

Facturación automática

Control de accesos por usuario

Pensado para simular un entorno real de empresa usando buenas prácticas de desarrollo en Odoo.

✨ Funcionalidades
🚘 Gestión de Flota (res.service)

Alta, baja y edición de vehículos

Precio por día configurable

Control de disponibilidad mediante campo active

📅 Reservas (res.booking)

❌ No permite fechas pasadas

✅ Verifica disponibilidad del vehículo

💶 Cálculo automático del precio según duración

⭐ Descuento automático del 10% para clientes VIP

⏱ Cancelación automática de reservas no confirmadas en 24h

💰 Facturación

Generación automática de factura al confirmar la reserva

Integración con módulo account de Odoo

🔐 Seguridad

👤 Clientes: solo ven sus propias reservas

👨‍💼 Administradores: acceso completo a flota, clientes y reservas

📂 Estructura del Módulo
gestion_reservas/
├── models/
│   ├── models.py        # Lógica de negocio (servicios, clientes, reservas)
│   └── __init__.py
├── views/
│   └── views.xml        # Menús, formularios y listas
├── security/
│   └── ir.model.access.csv
├── __manifest__.py      # Dependencias y metadata
└── README.md

🚀 Instalación
✅ Requisitos

Docker

Docker Compose

Odoo 17

🐳 Despliegue con Docker
docker-compose up -d


Servicios:

Odoo → http://localhost:8069

Postgres → puerto interno Docker

⚙️ Instalación del módulo

Accede a http://localhost:8069

Activa Modo Desarrollador

Apps → Actualizar lista de aplicaciones

Instala Gestión Alquiler de Coches

🧠 Metodología de Trabajo

Proyecto organizado usando SCRUM:

Sprint	Objetivo	Estado
1	Modelos y relaciones	✅
2	Lógica de negocio y validaciones	🚧
3	Vistas y seguridad	⏳
4	Pruebas y presentación final	⏳

Roles rotativos:

Scrum Master

Product Owner

Dev Team

🌿 Flujo de Git

Ramas:

main → versión estable

develop → integración del equipo

feature/* → trabajo individual

Flujo:

feature → Pull Request → develop → Pull Request → main


⚠️ main y develop están protegidas (no se permite push directo).

👥 Equipo

Proyecto desarrollado por estudiantes de DAM
Asignatura: Sistemas de Gestión Empresarial

📄 Licencia

Uso académico y educativo.
