# Guía para descargar y preparar el paquete de Clynico

Esta guía explica cómo obtener los archivos listos para subirlos a una cuenta empresarial (por ejemplo, subir el paquete al Firebase Hosting de Clynico o compartirlo mediante un servicio interno).

## 1. Clonar o actualizar el repositorio

Si todavía no tienes el código localmente:

```bash
git clone https://github.com/<tu-organizacion>/principal.git
cd principal
```

Si ya tienes el repositorio, asegúrate de traer los últimos cambios:

```bash
git pull
```

## 2. Crear el archivo comprimido con el script

Dentro de la raíz del repositorio ejecuta:

```bash
python scripts/package_clynico.py
```

Esto generará `clynico_bundle.zip` con todo el contenido de `clynico_app/`, listo para descargar y subir a la consola de Firebase u otro servicio.

### Opciones disponibles

- `--include-cli`: agrega el paquete de línea de comandos `patient_tracking` al zip.
- `--include-docs`: incluye los archivos de documentación almacenados en `docs/`.
- `-o <ruta>` o `--output <ruta>`: define el nombre y ubicación del archivo de salida.

Por ejemplo, para exportar todo en un archivo dentro de `dist/`:

```bash
python scripts/package_clynico.py --include-cli --include-docs -o dist/clynico_enterprise.zip
```

## 3. Verificar y transferir el archivo

Una vez creado el zip:

1. Confirma su tamaño y contenido:
   ```bash
   unzip -l clynico_bundle.zip | head
   ```
2. Descárgalo o súbelo mediante la herramienta de tu empresa (por ejemplo, SFTP, correo seguro o la sección de cargas de Firebase Hosting).

## 4. Subir a Firebase Hosting manualmente

Si en tu cuenta empresarial prefieren subir artefactos ya construidos a Firebase Hosting:

1. En una máquina con Node.js 18+ y las credenciales de Firebase, instala dependencias y genera la build dentro de `clynico_app/`:
   ```bash
   cd clynico_app
   npm install
   npm run build
   ```
2. El directorio `dist/` contendrá los archivos estáticos listos para servir. Puedes comprimirlo aparte si tu flujo lo requiere:
   ```bash
   cd dist
   zip -r ../clynico_app_dist.zip .
   ```
3. Sube `clynico_app_dist.zip` a la ubicación que tu área de infraestructura indique o despliega con `firebase deploy` desde una máquina autorizada.

## 5. Notas adicionales

- El script excluye automáticamente `node_modules/`, carpetas `.git/` y cachés para mantener el paquete ligero.
- Si tu empresa utiliza un repositorio interno, puedes subir el zip generado o el contenido del directorio directamente.
- Considera almacenar también el archivo `.env` (sin subirlo a repositorios públicos) junto con el paquete para facilitar la configuración en la cuenta empresarial.
