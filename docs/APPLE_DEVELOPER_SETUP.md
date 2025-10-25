# Apple Developer & App Store Connect

## Identificadores y app
- [ ] Bundle ID `com.tuempresa.clinyco` creado en Apple Developer
- [ ] App registrada en App Store Connect (SKU `clinyco-ios`)

## Automatización y llaves
- [ ] API Key de App Store Connect generada (Issuer ID, Key ID, archivo .p8)
- [ ] APNs Auth Key (.p8) configurada para notificaciones push de Zendesk

## Metadatos obligatorios
- [ ] Privacy Policy URL cargada en App Store Connect
- [ ] Support URL y Marketing URL actualizadas
- [ ] App Privacy completada con la información de Zendesk Messaging

## Accesos y roles
- [ ] Roles asignados (App Manager/Developer) para quienes compilan y publican
- [ ] Colaboradores de TestFlight invitados con permisos adecuados

## Integración con GitHub Actions
- [ ] Secret `APP_STORE_ISSUER_ID`
- [ ] Secret `APP_STORE_KEY_ID`
- [ ] Secret `APP_STORE_CONNECT_API_P8_BASE64`
- [ ] Secret `MATCH_PASSWORD` (si se usa match)
- [ ] Secret `MATCH_GIT_URL` (si se usa match)

Completa cada casilla una vez que hayas configurado el elemento correspondiente. Esta lista complementa la guía de publicación y el checklist de release.
