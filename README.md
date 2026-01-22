<h1 align="center">🚗 Odoo CarRental — Gestión de Reservas</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Odoo-17.0-purple" />
  <img src="https://img.shields.io/badge/Python-3.10+-blue" />
  <img src="https://img.shields.io/badge/Docker-Enabled-2496ED" />
  <img src="https://img.shields.io/badge/Estado-En%20Desarrollo-orange" />
</p>

<p align="center">
  <b>Proyecto Académico — DAM 2B | Sistemas de Gestión Empresarial (UT5)</b><br>
  Módulo personalizado para Odoo 17 orientado a la gestión integral de una empresa de alquiler de vehículos.
</p>

<hr>

<h2>📖 Descripción</h2>

<p>
El módulo <code>gestion_reservas</code> amplía Odoo 17 para cubrir todo el ciclo del alquiler de coches,
simulando un entorno real de empresa y aplicando metodología SCRUM.
</p>

<ul>
  <li>Gestión de servicios (flota)</li>
  <li>Reservas con validaciones</li>
  <li>Clientes VIP con descuento automático</li>
  <li>Facturación automática</li>
  <li>Control de accesos por usuario</li>
</ul>

<hr>

<h2>✨ Funcionalidades</h2>

<h3>🚘 Servicios (<code>res.service</code>)</h3>
<ul>
  <li>Alta, baja y edición de vehículos</li>
  <li>Precio por día configurable</li>
  <li>Activar / desactivar disponibilidad (<code>active</code>)</li>
</ul>

<h3>📅 Reservas (<code>res.booking</code>)</h3>
<ul>
  <li>❌ No permite fechas pasadas</li>
  <li>✅ Verifica disponibilidad del servicio</li>
  <li>💶 Precio automático por duración</li>
  <li>⭐ Descuento VIP del <b>10%</b></li>
  <li>⏱ Cancelación automática tras 24h</li>
</ul>

<h3>💰 Facturación</h3>
<ul>
  <li>Factura automática al confirmar reserva</li>
  <li>Integración con módulo <code>account</code></li>
</ul>

<h3>🔐 Seguridad</h3>
<ul>
  <li>Clientes → solo ven sus reservas</li>
  <li>Admins → acceso completo</li>
</ul>

<hr>

<h2>📂 Estructura del Módulo</h2>

<pre>
gestion_reservas/
├── models/
│   ├── models.py
│   └── __init__.py
├── views/
│   └── views.xml
├── security/
│   └── ir.model.access.csv
├── __manifest__.py
└── README.md
</pre>

<hr>

<h2>🚀 Instalación</h2>

<h3>Requisitos</h3>
<ul>
  <li>Docker</li>
  <li>Docker Compose</li>
  <li>Odoo 17</li>
</ul>

<h3>Despliegue</h3>

<pre>docker-compose up -d</pre>

<p>Acceso: <a href="http://localhost:8069">http://localhost:8069</a></p>

<h3>Instalar módulo</h3>

<ol>
  <li>Activar Modo Desarrollador</li>
  <li>Apps → Actualizar lista</li>
  <li>Instalar <b>Gestión Alquiler de Coches</b></li>
</ol>
<hr>

<h2>🌿 Flujo de Git</h2>

<ul>
  <li><b>main</b> → estable</li>
  <li><b>develop</b> → integración</li>
  <li><b>feature/*</b> → trabajo individual</li>
</ul>

<pre>
feature → Pull Request → develop → Pull Request → main
</pre>

<p>✔ Ramas protegidas</p>

<hr>

<h2>👥 Equipo (4 personas)</h2>

<ul>
  <li>👨‍💻 Mohamed Sabbar</li>
  <li>🎨 Nombre 2 — Frontend</li>
  <li>🧩 Nombre 3 — Backend</li>
  <li>🧑‍✈️ Nombre 4 — Scrum Master</li>
</ul>

<p><i>Roles rotativos en cada sprint.</i></p>

<hr>

<h2>📦 Entregables UT5</h2>

<ul>
  <li>Repositorio Git con historial</li>
  <li>Tablero SCRUM (GitHub Projects)</li>
  <li>Dashboard WakaTime</li>
  <li>Documento de errores y soluciones</li>
  <li>Presentación final</li>
</ul>

<hr>

<p align="center">
  <b>CFGM DAM 2B — Sistemas de Gestión Empresarial</b>
</p>
