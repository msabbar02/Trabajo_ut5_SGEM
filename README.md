<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Odoo CarRental - Gestión de Reservas</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #24292e;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
        }
        h1, h2, h3 {
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
        }
        h1 { font-size: 2em; margin-bottom: 16px; }
        h2 { font-size: 1.5em; margin-top: 24px; }
        h3 { font-size: 1.25em; margin-top: 20px; }
        
        code {
            background-color: #f6f8fa;
            border-radius: 3px;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
            font-size: 85%;
            padding: 0.2em 0.4em;
        }
        
        pre {
            background-color: #f6f8fa;
            border-radius: 6px;
            padding: 16px;
            overflow: auto;
            line-height: 1.45;
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
        }
        
        blockquote {
            color: #6a737d;
            border-left: 0.25em solid #dfe2e5;
            padding: 0 1em;
            margin: 0;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 10px;
        }
        
        table th, table td {
            border: 1px solid #dfe2e5;
            padding: 6px 13px;
        }
        
        table th {
            background-color: #f6f8fa;
            font-weight: 600;
        }
        
        table tr:nth-child(2n) {
            background-color: #f8f8f8;
        }
        
        .badges img {
            height: 20px;
            margin-right: 5px;
        }
        
        .directory-structure {
            font-family: monospace;
            white-space: pre;
        }
    </style>
</head>
<body>

    <h1>🚗 Odoo CarRental - Gestión de Reservas</h1>

    <div class="badges">
        <img src="https://img.shields.io/badge/Odoo-v17.0-purple?style=flat-square&logo=odoo" alt="Odoo 17">
        <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python" alt="Python">
        <img src="https://img.shields.io/badge/Docker-Enabled-2496ED?style=flat-square&logo=docker" alt="Docker">
        <img src="https://img.shields.io/badge/Status-En_Desarrollo-orange?style=flat-square" alt="Status">
    </div>

    <blockquote>
        <p><strong>Proyecto Académico | Sistemas de Gestión Empresarial (DAM 2B)</strong><br>
        [cite_start]Desarrollo de un módulo personalizado para la gestión integral de una empresa de alquiler de vehículos[cite: 2, 3, 6].</p>
    </blockquote>

    <hr>

    <h2>📋 Tabla de Contenidos</h2>
    <ul>
        <li><a href="#sobre-el-proyecto">Sobre el Proyecto</a></li>
        <li><a href="#caracteristicas">Características Principales</a></li>
        <li><a href="#estructura">Estructura del Módulo</a></li>
        <li><a href="#instalacion">Instalación y Despliegue</a></li>
        <li><a href="#metodologia">Metodología</a></li>
    </ul>

    <h2 id="sobre-el-proyecto">📖 Sobre el Proyecto</h2>
    [cite_start]<p>Este módulo, <code>gestion_reservas</code>[cite: 82], extiende la funcionalidad nativa de Odoo 17 para administrar el ciclo de vida completo del alquiler de coches. Desde la selección del vehículo y la validación de fechas, hasta la facturación automática y el control de clientes VIP.</p>

    <h2 id="caracteristicas">✨ Características Principales</h2>

    <h3>🚘 Gestión de Flota (<code>res.service</code>)</h3>
    <ul>
        [cite_start]<li>Alta, baja y modificación de vehículos con detalles como precio y disponibilidad[cite: 53, 86].</li>
        [cite_start]<li>Control de disponibilidad: Los servicios pueden desactivarse (campo <code>active</code>)[cite: 54].</li>
    </ul>

    <h3>📅 Sistema de Reservas (<code>res.booking</code>)</h3>
    <ul>
        [cite_start]<li><strong>Validaciones:</strong> Bloqueo de fechas pasadas y validación de disponibilidad del servicio[cite: 58, 100, 101].</li>
        <li><strong>Cálculo Automático:</strong> El precio se calcula en tiempo real según la duración y tarifa del coche.</li>
        [cite_start]<li><strong>Descuento VIP:</strong> Aplicación automática del <strong>10% de descuento</strong> si el cliente tiene la marca VIP[cite: 89, 97].</li>
        [cite_start]<li><strong>Cancelación Automática:</strong> Lógica que cancela reservas pendientes tras 24h sin confirmación[cite: 78, 98].</li>
    </ul>

    <h3>💰 Facturación Integrada</h3>
    <ul>
        [cite_start]<li>Generación automática de factura en Odoo al confirmar la reserva[cite: 60, 99].</li>
    </ul>

    <h3>🔒 Seguridad y Permisos</h3>
    <ul>
        [cite_start]<li><strong>Clientes:</strong> Solo pueden ver y gestionar sus propias reservas[cite: 62].</li>
        [cite_start]<li><strong>Administradores:</strong> Acceso total a configuración, flota y todas las reservas[cite: 63].</li>
    </ul>

    <h2 id="estructura">📂 Estructura del Módulo</h2>
    <pre class="directory-structure">
gestion_reservas/
├── models/
[cite_start]│   ├── models.py       # Lógica: Servicios, Clientes (VIP) y Reservas [cite: 17, 85]
│   └── __init__.py
├── views/
[cite_start]│   └── views.xml       # Frontend: Menús, Formularios y Listas [cite: 18, 107]
├── security/
│   └── ir.model.access.csv  # Permisos de acceso
├── __manifest__.py     # Dependencias (account, base)
└── README.md
    </pre>

    <h2 id="instalacion">🚀 Instalación y Despliegue</h2>

    <h3>1. Requisitos</h3>
    <ul>
        <li>Docker y Docker Compose.</li>
        [cite_start]<li>Extensión <strong>WakaTime</strong> instalada en el editor para seguimiento del tiempo[cite: 45].</li>
    </ul>

    <h3>2. Despliegue con Docker</h3>
    <pre><code># Levantar el entorno (Odoo 17 + Postgres 15)
docker-compose up -d</code></pre>

    <h3>3. Instalación en Odoo</h3>
    <ol>
        <li>Accede a <code>http://localhost:8069</code>.</li>
        <li>Activa el <strong>Modo Desarrollador</strong>.</li>
        <li>Actualiza la lista de aplicaciones e instala <strong>"Gestión Alquiler de Coches"</strong>.</li>
    </ol>

    <h2 id="metodologia">📊 Metodología SCRUM</h2>
    [cite_start]<p>El proyecto se organiza en 4 Sprints semanales con roles rotativos (Scrum Master, Product Owner, Dev Team)[cite: 9, 14, 20].</p>

    <table>
        <thead>
            <tr>
                <th>Sprint</th>
                <th>Objetivo</th>
                <th>Estado</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Sprint 1</td>
                [cite_start]<td>Modelos y Relaciones [cite: 21]</td>
                <td>✅ Completado</td>
            </tr>
            <tr>
                <td>Sprint 2</td>
                [cite_start]<td>Lógica de Negocio y Validaciones [cite: 21]</td>
                <td>🚧 En Progreso</td>
            </tr>
            <tr>
                <td>Sprint 3</td>
                [cite_start]<td>Vistas, Seguridad y Permisos [cite: 21]</td>
                <td>⏳ Pendiente</td>
            </tr>
            <tr>
                <td>Sprint 4</td>
                [cite_start]<td>Pruebas y Presentación Final [cite: 21]</td>
                <td>⏳ Pendiente</td>
            </tr>
        </tbody>
    </table>

    <hr>
    [cite_start]<p><em>Proyecto desarrollado según las especificaciones del documento UT5 Desarrollo componentes Odoo[cite: 3].</em></p>

</body>
</html>
